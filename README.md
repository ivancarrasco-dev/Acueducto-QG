# Sistema de Gestión e Información - Acueducto Rural 💧

Sistema web integral desarrollado para la **Asociación de Acueducto Rural Quebrada Grande** (San Antonio del Tequendama). Facilita la transparencia administrativa y mejora la comunicación con la comunidad mediante una plataforma moderna, rápida y adaptable a dispositivos móviles.

---

## 🚀 Características Principales

### Portal Público
- **Inicio:** Presentación general con noticias y avisos a la comunidad en formato de tarjetas. Al hacer clic en una noticia se abre un modal con el contenido completo.
- **Quiénes Somos:** Misión, visión y valores de la asociación.
- **Servicios:** Descripción detallada de los 6 servicios prestados: suministro de agua, mantenimiento de redes, control de calidad, facturación, atención de emergencias y nuevas conexiones.
- **Transparencia:** Listado público de documentos oficiales (Actas, Tarifas, Informes Financieros, Calidad del Agua, Contratos) organizados por categoría, disponibles para descarga en PDF.
- **Contacto:** Formulario con envío automático al correo de la administración mediante FormSubmit.

### Panel de Administración
- Acceso protegido con usuario y contraseña.
- **Gestión de noticias:** Crear, editar y eliminar avisos con imagen opcional.
- **Gestión de documentos PDF:** Subir y eliminar documentos clasificados por categoría. Solo accesible desde el panel.
- **Bandeja de mensajes:** Visualización de todos los mensajes enviados por la comunidad desde el formulario de contacto.

### Diseño y Usabilidad
- **100% Responsive:** Adaptado para celulares, tablets y pantallas grandes.
- **Menú hamburguesa** en móvil con animación y cierre automático al navegar.
- **Grid de noticias adaptable:** 1 columna en celular, 2 en tablet, 3 en pantallas grandes.
- **Footer completo** con navegación, información de contacto y enlaces a redes sociales.

---

## 🛠️ Tecnologías Utilizadas

| Capa | Tecnología |
|---|---|
| Backend | Python 3.x + Flask |
| Frontend | HTML5, Tailwind CSS, JavaScript vanilla |
| Base de datos | SQLite3 |
| ORM | SQLAlchemy |
| Íconos | Font Awesome 6 |
| Formulario de contacto | FormSubmit |

---

## 📁 Estructura del Proyecto

```
acueducto/
│
├── app.py                  # Aplicación principal Flask y todas las rutas
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
    ├── base.html           # Plantilla base: navbar, footer, flashes
    ├── index.html          # Página de inicio con noticias
    ├── nosotros.html       # Quiénes somos
    ├── servicios.html      # Servicios del acueducto
    ├── transparencia.html  # Documentos públicos PDF
    ├── contacto.html       # Formulario de contacto
    ├── login.html          # Acceso al panel de administración
    └── admin.html          # Panel de administración (protegido)
```

---

## 📋 Requisitos Previos

- Python 3.8 o superior
- Pip (gestor de paquetes de Python)

---

## 🔧 Instalación y Configuración

1. **Descargar o clonar el proyecto:**
   ```bash
   cd acueducto
   ```

2. **Crear y activar entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install flask flask-sqlalchemy werkzeug
   ```

4. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

5. **Abrir en el navegador:**
   ```
   http://127.0.0.1:5000
   ```

La base de datos y las carpetas de archivos se crean automáticamente al iniciar por primera vez.

---

## 🔐 Acceso al Panel de Administración

| Campo | Valor |
|---|---|
| URL | `/login` |
| Usuario | `admin` |
| Contraseña | `Acueducto2026` |

> **Recomendación:** Cambiar la contraseña en `app.py` antes de publicar el sitio en producción.

---

## 🗄️ Modelos de Base de Datos

**Noticia** — Almacena los avisos publicados en el inicio.
- `id`, `titulo`, `contenido`, `imagen` (opcional), `fecha`

**Mensaje** — Almacena los mensajes enviados desde el formulario de contacto.
- `id`, `nombre`, `correo`, `asunto`, `mensaje`, `fecha`

**Documento** — Almacena los documentos PDF subidos desde el panel admin.
- `id`, `nombre`, `categoria`, `ruta`, `fecha`

---

## 🌐 Rutas de la Aplicación

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Página de inicio |
| GET | `/nosotros` | Quiénes somos |
| GET | `/servicios` | Servicios del acueducto |
| GET | `/transparencia` | Documentos públicos |
| GET | `/documentos/<filename>` | Ver/descargar un PDF |
| GET | `/contacto` | Formulario de contacto |
| POST | `/enviar_contacto` | Guardar mensaje en BD |
| GET/POST | `/login` | Acceso al panel |
| GET | `/logout` | Cerrar sesión |
| GET | `/admin` | Panel de administración |
| POST | `/admin/noticia/nueva` | Crear noticia |
| POST | `/admin/noticia/editar/<id>` | Editar noticia |
| GET | `/admin/noticia/borrar/<id>` | Eliminar noticia |
| POST | `/admin/documento/subir` | Subir PDF |
| GET | `/admin/documento/borrar/<id>` | Eliminar PDF |

---

## ✅ Cumplimiento de Requerimientos del Cliente

| Requerimiento | Estado |
|---|---|
| Sitio informativo para la comunidad | ✅ |
| Sección Inicio | ✅ |
| Sección Quiénes Somos (misión y visión) | ✅ |
| Sección Servicios | ✅ |
| Noticias y avisos | ✅ |
| Información de contacto | ✅ |
| Sección de Transparencia con PDFs | ✅ |
| Diseño responsive para celulares | ✅ |
| Formulario de contacto con notificación | ✅ |
| Publicación y actualización de noticias | ✅ |
| Subida de documentos PDF | ✅ |
| Integración con redes sociales | ⏳ Pendiente (links del cliente) |
| Panel de administración | ✅ |
| Historia de la asociación | ⏳ Pendiente (texto del cliente) |

---

## 👨‍💻 Desarrollador

Desarrollado por **Iván Carrasco** — Tecnólogo en Análisis y Desarrollo de Software, SENA.