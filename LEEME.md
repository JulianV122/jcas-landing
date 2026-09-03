# J'CAS Sala de Belleza — Landing page

Landing page de una sola página construida sobre la plantilla **Rasm**, adaptada a la
identidad de J'CAS (negro carbón + dorado champán).

## Cómo verla

Abre `index.html` en el navegador. Para que el mapa y las fuentes carguen bien, lo ideal es
levantar un servidor local desde esta carpeta:

```bash
python -m http.server 5555
```

Y entrar a `http://localhost:5555`.

## Qué contiene

| Sección | Ancla | Contenido |
|---|---|---|
| Hero | `#hero` | Slider de 3 mensajes + botón a WhatsApp |
| Cinta animada | — | Listado de servicios en movimiento |
| Nosotros | `#nosotros` | Texto de presentación + contadores |
| Servicios | `#servicios` | 6 tarjetas: barbería, peluquería, color, tratamientos, uñas, faciales. **Al hacer clic se abre un carrusel con las fotos de ese servicio** |
| Micropigmentación | `#micropigmentacion` | Sección oscura: cejas, labios, líneas de ojos, BB Glow |
| Uñas | `#unas` | Sección dedicada con galería de diseños |
| Galería | `#galeria` | 11 fotos reales del salón con lightbox |
| Reseñas | — | 3 tarjetas (hay que llenarlas con reseñas reales) |
| Ubicación | `#ubicacion` | Dirección, horario, WhatsApp y **mapa de Google embebido** |
| CTA final + footer | — | Cierre con botón de WhatsApp |

Además hay un **botón flotante de WhatsApp** siempre visible (313 761 2054).

---

## Ya está puesto

- **Fotos reales del salón** en hero, "Nosotros", galería (6 fotos) y fondo del CTA.
- **Fotos de servicios** tomadas del Instagram del salón (barbería, peluquería, color,
  tratamientos, manicura) + la cabina de estética para faciales.
- **Horario**: lunes a sábado, 8:00 a.m. – 6:00 p.m.
- **Instagram** en el footer: `@jcas_saladebelleza`.
- **Mapa**: apunta a la ficha real "J'CAS Sala de Belleza" en Google Maps.
- Todas las fotos optimizadas (máx. 1400 px de lado, ~2,7 MB en total).
- **Logo real** en header, menú móvil, footer, preloader y favicon. Como el archivo original
  (`assets/img/Logo.jpeg`) tiene fondo negro y no serviría sobre el header claro, se recortó
  en un medallón circular con transparencia (`assets/img/jcas/logo-medallon.png`) y se
  acompaña del nombre en tipografía para que sea legible en tamaños pequeños.
  Si algún día consigues el logo en vectorial o PNG con fondo transparente, reemplaza ese
  archivo.

## ⚠️ Pendientes antes de publicar

### 1. Las reseñas son inventadas

Los tres testimonios de la sección "Reseñas" (Laura M., Daniela R., Catalina G.) **son
textos de ejemplo, no son clientas reales**. Publicarlos como si fueran auténticos es
publicidad engañosa y en Colombia lo sanciona la SIC (Estatuto del Consumidor, Ley 1480).

Antes de subir el sitio, cámbialos por comentarios reales. La forma más rápida: escríbeles
por WhatsApp a tres clientas frecuentes pidiéndoles una frase y permiso para publicarla con
su nombre. En `index.html` busca `testi-grid_text` para encontrarlos.

### 2. Derechos de imagen de las fotos

Cuatro tarjetas de servicios y varias fotos muestran **rostros de clientas reales** tomadas
del Instagram del salón. Que estén publicadas en Instagram no equivale a autorización para
usarlas en la página web. Conviene pedirles permiso por escrito (basta un mensaje de
WhatsApp) o reemplazarlas por fotos sin rostro identificable.

Las que **no** tienen este problema: barbería (silla vacía), color (de espaldas), manicura
(solo manos) y faciales (cabina vacía).

### 3. Faltan fotos en varias galerías

Cada tarjeta de servicio abre un carrusel. Hoy tienen: barbería 3, manicura 3, peluquería 2,
color 2, tratamientos 2, **faciales solo 1** (la cabina vacía, ni siquiera un procedimiento).

La sección de Uñas tiene 3 diseños y un cuarto recuadro que dice "Aquí van más diseños".

Lo que más falta, en orden: fotos de limpieza facial, de cejas micropigmentadas y más
diseños de uñas.

**Cómo agregar fotos a un carrusel de servicio:** guarda la foto en
`assets/img/jcas/servicios/` (por ejemplo `manicura_4.jpg`) y en `index.html`, dentro de la
tarjeta correspondiente, añade una línea al bloque `jcas-service_gallery`:

```html
<a href="assets/img/jcas/servicios/manicura_4.jpg" title="Manicura y pedicura"></a>
```

El contador de fotos se actualiza solo. La **primera** foto de la lista es la portada de la
tarjeta, así que ponla de primera si quieres cambiar la portada.

**Cómo agregar diseños a la sección de Uñas:** en `index.html` busca `jcas-nails_more` y
reemplaza ese bloque por una copia de uno de los `col-6` que están arriba, cambiando la ruta
de la imagen. Para más de 4, sigue copiando bloques `col-6`.

### 4. Contadores

Busca `AJUSTA ESTOS NÚMEROS` en `index.html`. Hoy dicen 15 servicios / 100% productos /
6 estilistas / 6 días.

### 5. Dato a confirmar

El Instagram del salón dice **"Calle 23 # 54-25"**, pero el flyer y Google Maps dicen
**"Carrera 23 #54-25"** (la Avenida Santander es la Carrera 23). La página usa *Carrera*.
Vale la pena corregir el Instagram si es un error.

### 6. Facebook y TikTok

En el footer solo quedaron Instagram y WhatsApp. Si el salón tiene esas redes, se agregan
al lado.

---

## Cambiar una foto

Todas las imágenes viven en `assets/img/jcas/`. Para cambiar cualquiera, sobrescribe el
archivo respetando el nombre. Tamaños de referencia:

| Carpeta | Uso | Tamaño |
|---|---|---|
| `hero/` | fondo del slider principal | vertical u horizontal, 1400 px de lado largo |
| `servicios/` | las 6 tarjetas | vertical, ~600×700 |
| `galeria/` | mosaico de la galería | 1400 px de lado largo |
| `general/` | "Nosotros" y fondo del CTA | 1400 px de lado largo |

## Cómo publicar la página en internet

### Paso 1 — Preparar los archivos

```
python empaquetar.py
```

Esto crea la carpeta **`publicar/`** con solo lo necesario: 8 MB en vez de los 67 MB del
proyecto completo (descarta imágenes de la plantilla que no usamos y formatos de fuente
que solo servían para Internet Explorer). Ejecútalo cada vez que hagas cambios.

### Paso 2 — Subirla a Netlify (gratis)

1. Entra a **https://app.netlify.com/drop**
2. Arrastra la carpeta **`publicar`** completa a la zona punteada de la página.
3. En menos de un minuto te da una dirección tipo `nombre-aleatorio.netlify.app`.
   **Ya está en internet**, con HTTPS incluido.
4. Crea una cuenta gratis (con tu correo o con Google) para que la página no se borre y
   puedas administrarla.
5. En **Site configuration → Change site name** cámbiale el nombre a algo como
   `jcas-saladebelleza`, y quedará en `jcas-saladebelleza.netlify.app`.

El plan gratuito da 100 GB de tráfico al mes — muchísimo más de lo que un salón necesita.

**Para actualizar la página después:** corre `python empaquetar.py` otra vez y arrastra la
carpeta en **Deploys → arrastra tu carpeta aquí**. Reemplaza la versión anterior.

### Paso 3 (opcional) — Dominio propio

`jcas-saladebelleza.netlify.app` funciona perfecto, pero para un negocio conviene algo como
`jcassaladebelleza.com`. Se compra en Namecheap, GoDaddy o Hostinger (un `.com` cuesta unos
USD 12 al año; un `.com.co` ronda los 60.000 COP anuales).

Una vez comprado: en Netlify entra a **Domain management → Add a domain**, escribe tu
dominio y Netlify te indica qué registros DNS poner en el panel de donde lo compraste. El
certificado HTTPS lo genera solo y gratis.

### Después de publicar

- Pon el link en la **biografía de Instagram** y en la **ficha de Google Maps** del salón
  (Google Business Profile → Editar perfil → Sitio web). Eso último ayuda bastante a que
  aparezcas cuando alguien busque "salón de belleza Manizales".
- Comparte el link por WhatsApp: la vista previa ya está configurada con el logo y una
  descripción.

### Otras opciones

**Cloudflare Pages** (`pages.cloudflare.com`) funciona igual de bien y también es gratis.
**GitHub Pages** es gratis pero requiere manejar Git. Un hosting tradicional con cPanel
también sirve: subes el contenido de `publicar/` a la carpeta `public_html` por FTP.

---

## Estructura de archivos

```
JCAS/
├─ index.html              ← la página completa
├─ empaquetar.py           ← genera la carpeta lista para subir
├─ publicar/               ← lo que se sube a internet (se regenera solo)
├─ LEEME.md                ← este archivo
└─ assets/
   ├─ css/
   │  ├─ style.css         ← plantilla original (no tocar)
   │  └─ jcas.css          ← colores y componentes propios de J'CAS
   ├─ js/                  ← scripts de la plantilla
   └─ img/
      └─ jcas/             ← TODAS las imágenes de J'CAS van aquí
         ├─ hero/
         ├─ servicios/
         ├─ galeria/
         ├─ general/
         └─ logo-*.svg
```

Los colores de la marca están al inicio de `assets/css/jcas.css`:
`--theme-color: #C9A063` (dorado champán) y `--black-color: #0B0A09` (negro).
Cambiando esas dos variables se recolorea toda la página.
