# 💧 Sistema Web - Asociación de Acueducto Rural Quebrada Grande

Portal web oficial de la **Asociación de Usuarios del Acueducto Vereda Quebrada Grande**, San Antonio del Tequendama, Cundinamarca. Desarrollado para facilitar la comunicación con la comunidad, garantizar la transparencia administrativa y modernizar la gestión del servicio de agua potable.

---

## 🌐 Vista General

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?style=flat&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-3-blue?style=flat&logo=sqlite)
![Responsive](https://img.shields.io/badge/Responsive-Mobile--First-green?style=flat)

---

## ✅ Cumplimiento de Requerimientos del Cliente

| Requerimiento | Estado |
|---|---|
| Sitio informativo para la comunidad | ✅ |
| Inicio con presentación general | ✅ |
| Quiénes Somos — misión, visión, valores | ✅ |
| Historia de la asociación | ⏳ Pendiente (texto del cliente) |
| Sección de Servicios | ✅ |
| Noticias y avisos a la comunidad | ✅ |
| Historial completo de noticias | ✅ |
| Galería fotográfica | ✅ |
| Información de contacto con formulario | ✅ |
| Transparencia con documentos PDF | ✅ |
| Diseño responsive para celulares | ✅ |
| Formulario con notificación al correo | ✅ |
| Subida de documentos PDF | ✅ |
| Integración redes sociales / contacto | ✅ |
| Panel de administración | ✅ |
| Mapa de ubicación | ✅ |

---

## 🚀 Características Principales

### Portal Público
- **Inicio** — Hero con imagen del municipio, últimas 4 noticias con modal de lectura y botón "Ver todos los avisos"
- **Quiénes Somos** — Descripción oficial, misión, visión y 7 valores institucionales
- **Servicios** — 6 servicios detallados con información real de la asociación
- **Noticias** — Historial completo de avisos con modal de lectura
- **Galería** — Fotos organizadas en 3 categorías: Imágenes históricas, Imágenes PNUD y CAR, Imágenes de asamblea
- **Transparencia** — Documentos PDF organizados por categoría con buscador en tiempo real
- **Contacto** — Formulario con envío al correo `acueductoqgrande@hotmail.com` vía FormSubmit + mapa de Google Maps + datos de contacto completos

### Información de Contacto Real
- 📧 acueductoqgrande@hotmail.com
- 💬 WhatsApp Usuarios: 313 866 4738
- 💬 WhatsApp Tesorería: 302 845 2511
- 📞 Reporte de daños: 318 567 1803 (Luis Cano — Fontanero)

### Panel de Administración
- Acceso protegido con usuario y contraseña
- **Tab Noticias** — Crear, editar y eliminar avisos con imagen opcional + buscador
- **Tab Documentos PDF** — Subir y eliminar documentos por categoría + buscador
- **Tab Galería** — Subir y eliminar fotos por categoría
- Optimizado para uso en celular, sin footer para mayor espacio
- Cursor automático en el campo de título al entrar

### Diseño y UX
- **Fuente Montserrat** — moderna y legible
- **Paleta del logo institucional** — Azul acero `#2d4a6e`, Verde `#50C878`, Blanco humo `#F5F5F5`, Gris carbón `#333333`
- **Logo oficial** del cliente en navbar (horizontal) y footer (isotipo)
- **Favicon** con ícono oficial `.ico`
- **Accesible para adultos mayores** — texto grande, alto contraste, botones amplios
- **Menú hamburguesa** en móvil con animación y hover
- **Hover con línea animada** en enlaces del navbar
- **Notificaciones popup** — verdes para éxito, rojas para error, desaparecen en 10 segundos
- **Fechas en español** — filtros Jinja personalizados
- **CSS separado** en `static/css/style.css`

### Optimización de Rendimiento
- Google Fonts cargado de forma asíncrona (no bloquea el render)
- Font Awesome cargado de forma asíncrona
- Imagen hero optimizada con `preload` y resolución adaptada
- Imágenes de galería con `loading="lazy"`

---

## 🛠️ Tecnologías

| Capa | Tecnología |
|---|---|
| Backend | Python 3.x + Flask |
| Frontend | HTML5, CSS3 separado, JavaScript vanilla |
| Base de datos | SQLite3 |
| ORM | SQLAlchemy |
| Tipografía | Google Fonts — Montserrat |
| Íconos | Font Awesome 6 |
| Formulario de contacto | FormSubmit → acueductoqgrande@hotmail.com |
| Mapa | Google Maps Embed (sin API Key) |

---

## 📁 Estructura del Proyecto

```
acueducto/
│
├── app.py                  # Aplicación Flask, rutas y filtros de fecha
├── README.md
│
├── instance/
│   └── acueducto.db        # Base de datos SQLite (se genera automáticamente)
│
├── static/
│   ├── css/
│   │   └── style.css       # Estilos globales del proyecto
│   ├── media/              # Logos e ícono del cliente
│   │   ├── icono.ico
│   │   ├── logo_horizontal_sin_fondo.png
│   │   └── isotipo_sin_fondo.png
│   ├── uploads/            # Imágenes subidas para noticias y galería
│   └── documentos/         # Archivos PDF subidos desde el panel admin
│
└── templates/
    ├── base.html           # Plantilla base: navbar, footer, popups, scripts
    ├── index.html          # Inicio con hero, noticias y modal
    ├── noticias.html       # Historial completo de avisos
    ├── nosotros.html       # Quiénes somos
    ├── servicios.html      # Servicios del acueducto
    ├── galeria.html        # Galería fotográfica por categorías
    ├── transparencia.html  # Documentos PDF con buscador
    ├── contacto.html       # Formulario + info de contacto + mapa
    ├── login.html          # Acceso administrativo
    └── admin.html          # Panel de administración (tabs)
```

---

## 📋 Requisitos Previos

- Python 3.8 o superior
- Pip

---

## 🔧 Instalación

```bash
# 1. Clonar o descargar el proyecto
cd acueducto

# 2. Crear entorno virtual
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Instalar dependencias
pip install flask flask-sqlalchemy werkzeug

# 4. Ejecutar
python app.py
```

Abrir en el navegador: `http://127.0.0.1:5000`

La base de datos y las carpetas `static/uploads/` y `static/documentos/` se crean automáticamente al iniciar.

---

## 🔐 Acceso al Panel

| Campo | Valor |
|---|---|
| URL | `/login` |
| Usuario | `admin` |
| Contraseña | `Acueducto2026` |

> ⚠️ Cambiar la contraseña en `app.py` antes de publicar en producción.

---

## 🗄️ Modelos de Base de Datos

**Noticia** — `id`, `titulo`, `contenido`, `imagen`, `fecha`

**Mensaje** — `id`, `nombre`, `correo`, `asunto`, `mensaje`, `fecha`

**Documento** — `id`, `nombre`, `categoria`, `ruta`, `fecha`

**Foto** — `id`, `categoria`, `descripcion`, `ruta`, `fecha`

---

## 🌐 Rutas

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Inicio (últimas 4 noticias) |
| GET | `/noticias` | Historial completo de avisos |
| GET | `/nosotros` | Quiénes somos |
| GET | `/servicios` | Servicios |
| GET | `/galeria` | Galería fotográfica |
| GET | `/transparencia` | Documentos públicos |
| GET | `/documentos/<filename>` | Ver/descargar PDF |
| GET | `/contacto` | Formulario de contacto |
| POST | `/enviar_contacto` | Guardar mensaje |
| GET/POST | `/login` | Acceso al panel |
| GET | `/logout` | Cerrar sesión |
| GET | `/admin` | Panel de administración |
| POST | `/admin/noticia/nueva` | Crear noticia |
| POST | `/admin/noticia/editar/<id>` | Editar noticia |
| GET | `/admin/noticia/borrar/<id>` | Eliminar noticia |
| POST | `/admin/documento/subir` | Subir PDF |
| GET | `/admin/documento/borrar/<id>` | Eliminar PDF |
| POST | `/admin/foto/subir` | Subir foto a galería |
| GET | `/admin/foto/borrar/<id>` | Eliminar foto |

---

## 👨‍💻 Desarrollador

**Iván Carrasco** — Tecnólogo en Análisis y Desarrollo de Software, SENA
San Antonio del Tequendama, Cundinamarca, Colombia — 2026