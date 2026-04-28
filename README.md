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
| Quiénes Somos — misión, visión, historia | ✅ |
| Sección de Servicios | ✅ |
| Noticias y avisos a la comunidad | ✅ |
| Información de contacto con formulario | ✅ |
| Transparencia con documentos PDF | ✅ |
| Diseño responsive para celulares | ✅ |
| Formulario con notificación al correo | ✅ |
| Publicación y actualización de noticias | ✅ |
| Subida de documentos PDF | ✅ |
| Integración con redes sociales | ⏳ Pendiente (links del cliente) |
| Panel de administración | ✅ |

---

## 🚀 Características Principales

### Portal Público
- **Inicio** — Hero con imagen del municipio, últimas 4 noticias con modal de lectura y botón "Ver todos los avisos"
- **Quiénes Somos** — Descripción, misión, visión y 7 valores institucionales con información oficial de la asociación
- **Servicios** — 6 servicios detallados: suministro, mantenimiento, control de calidad, facturación, emergencias y nuevas conexiones
- **Transparencia** — Documentos PDF organizados por categoría con buscador en tiempo real
- **Noticias** — Historial completo de avisos con modal de lectura
- **Contacto** — Formulario con envío al correo via FormSubmit + mapa de Google Maps de la vereda

### Panel de Administración
- Acceso protegido con usuario y contraseña
- **Noticias** — Crear, editar y eliminar avisos con imagen opcional + buscador
- **Documentos PDF** — Subir y eliminar documentos por categoría + buscador
- Organizado en tabs para mayor eficiencia
- Optimizado para uso en celular

### Diseño y UX
- **Fuente Montserrat** — moderna y legible
- **Paleta institucional** — Azul cian `#4A90E2`, Verde bosque `#50C878`, Blanco humo `#F5F5F5`, Gris carbón `#333333`
- **Accesible para adultos mayores** — texto grande, alto contraste, botones amplios
- **Menú hamburguesa** en móvil con animación
- **Notificaciones popup** — verdes para éxito, rojas para error, desaparecen en 10 segundos
- **Fechas en español** — filtros Jinja personalizados

---

## 🛠️ Tecnologías

| Capa | Tecnología |
|---|---|
| Backend | Python 3.x + Flask |
| Frontend | HTML5, CSS3, JavaScript vanilla |
| Base de datos | SQLite3 |
| ORM | SQLAlchemy |
| Tipografía | Google Fonts — Montserrat |
| Íconos | Font Awesome 6 |
| Formulario de contacto | FormSubmit |
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
│   ├── uploads/            # Imágenes subidas para noticias
│   └── documentos/         # Archivos PDF subidos desde el panel admin
│
└── templates/
    ├── base.html           # Plantilla base: navbar, footer, popups, scripts
    ├── index.html          # Inicio con hero, noticias y modal
    ├── noticias.html       # Historial completo de avisos
    ├── nosotros.html       # Quiénes somos
    ├── servicios.html      # Servicios del acueducto
    ├── transparencia.html  # Documentos PDF con buscador
    ├── contacto.html       # Formulario + mapa
    ├── login.html          # Acceso administrativo
    └── admin.html          # Panel de administración
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

---

## 🌐 Rutas

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Inicio (últimas 4 noticias) |
| GET | `/noticias` | Historial completo |
| GET | `/nosotros` | Quiénes somos |
| GET | `/servicios` | Servicios |
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

---

## 👨‍💻 Desarrollador

**Iván Carrasco** — Tecnólogo en Análisis y Desarrollo de Software, SENA  
San Antonio del Tequendama, Cundinamarca, Colombia — 2026