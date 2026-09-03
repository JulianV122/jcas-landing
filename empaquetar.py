# -*- coding: utf-8 -*-
"""
Prepara la carpeta 'publicar/' con lo que el sitio realmente necesita.

Uso:  python empaquetar.py

Recorre index.html y los CSS, se queda solo con los archivos referenciados y
descarta los formatos de fuente antiguos (.eot/.ttf/.svg/.woff), que solo hacían
falta para Internet Explorer. Resultado: ~8 MB en vez de 67 MB.

Después de ejecutarlo, sube el CONTENIDO de la carpeta 'publicar'.
"""
import re
import io
import os
import glob
import shutil

SEP = chr(92)  # backslash


def rutas_referenciadas(archivo):
    """Devuelve las rutas que aparecen en href/src/data-bg-src y url(...)."""
    try:
        txt = io.open(archivo, encoding='utf-8', errors='ignore').read()
    except OSError:
        return []
    refs = re.findall(r'(?:href|src|data-bg-src)\s*=\s*["\']([^"\']+)["\']', txt)
    refs += re.findall(r'url\(\s*["\']?([^)"\']+)["\']?\s*\)', txt)
    return refs


def resolver(base, ruta):
    ruta = ruta.split('?')[0].split('#')[0].strip()
    if not ruta or ruta.startswith(('http', 'data:', 'mailto:', 'tel:', '//')):
        return None
    p = os.path.normpath(os.path.join(os.path.dirname(base), ruta)).replace(SEP, '/')
    return p if os.path.isfile(p) else None


def recolectar():
    usados, pendientes, vistos = set(), ['index.html'], set()
    while pendientes:
        actual = pendientes.pop()
        if actual in vistos:
            continue
        vistos.add(actual)
        usados.add(actual)
        for r in rutas_referenciadas(actual):
            destino = resolver(actual, r)
            if destino:
                # Formatos de fuente antiguos: los omitimos (ver limpiar_font_face)
                if destino.lower().endswith(('.eot', '.ttf', '.otf', '.woff')):
                    continue
                usados.add(destino)
                if destino.endswith(('.css', '.html')):
                    pendientes.append(destino)
    # Los iconos se piden desde el CSS: llevamos solo el formato moderno.
    for raiz, _, files in os.walk('assets/fonts'):
        for f in files:
            if f.lower().endswith('.woff2'):
                usados.add(os.path.join(raiz, f).replace(SEP, '/'))
    return usados


def limpiar_font_face(css):
    """Quita de los @font-face las referencias a formatos que ya no copiamos."""
    txt = io.open(css, encoding='utf-8', errors='ignore').read()

    def solo_woff2(m):
        partes = re.findall(r'url\([^)]*\)\s*format\("[^"]*"\)', m.group(0))
        woff2 = [p for p in partes if '.woff2' in p]
        return 'src:' + ','.join(woff2) if woff2 else m.group(0)

    nuevo = re.sub(r'src:(?:url\([^)]*\)\s*format\("[^"]*"\)[,\s]*)+', solo_woff2, txt)
    if nuevo != txt:
        io.open(css, 'w', encoding='utf-8').write(nuevo)
        return True
    return False


def main():
    usados = recolectar()
    destino = 'publicar'
    if os.path.isdir(destino):
        # En Windows la carpeta puede estar abierta en el Explorador; si no se
        # puede borrar entera, vaciamos lo que se pueda y escribimos encima.
        shutil.rmtree(destino, ignore_errors=True)
        for raiz, _, files in os.walk(destino):
            for f in files:
                try:
                    os.remove(os.path.join(raiz, f))
                except OSError:
                    pass

    total = 0
    for f in sorted(usados):
        d = os.path.join(destino, f)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        shutil.copy2(f, d)
        total += os.path.getsize(f)

    # Solo tocamos el CSS de los iconos; style.css se deja intacto.
    for css in glob.glob(destino + '/assets/css/fontawesome*.css'):
        limpiar_font_face(css)

    total = sum(os.path.getsize(os.path.join(r, x))
                for r, _, fs in os.walk(destino) for x in fs)
    print('Archivos: %d' % len(usados))
    print('Carpeta "%s": %.1f MB  -> lista para subir' % (destino, total / 1024 / 1024))


if __name__ == '__main__':
    main()
