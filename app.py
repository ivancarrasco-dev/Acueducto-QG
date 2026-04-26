import os
import locale
from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename

# Intentar configurar locale en español
try:
    locale.setlocale(locale.LC_TIME, 'es_CO.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    except:
        pass

app = Flask(__name__)
app.secret_key = "acueducto_vereda_2026_seguro"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///acueducto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

PDF_FOLDER = 'static/documentos'
app.config['PDF_FOLDER'] = PDF_FOLDER

db = SQLAlchemy(app)

MESES = {
    1:'enero', 2:'febrero', 3:'marzo', 4:'abril',
    5:'mayo', 6:'junio', 7:'julio', 8:'agosto',
    9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'
}
MESES_CORTO = {
    1:'Ene', 2:'Feb', 3:'Mar', 4:'Abr',
    5:'May', 6:'Jun', 7:'Jul', 8:'Ago',
    9:'Sep', 10:'Oct', 11:'Nov', 12:'Dic'
}

@app.template_filter('fecha_es')
def fecha_es(dt):
    return f"{dt.day:02d}/{dt.month:02d}/{dt.year}"

@app.template_filter('fecha_larga_es')
def fecha_larga_es(dt):
    return f"{dt.day} {MESES_CORTO[dt.month]}, {dt.year}"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PDF_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def allowed_pdf(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

# --- MODELOS ---
class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    imagen = db.Column(db.String(200), nullable=True)
    fecha = db.Column(db.DateTime, default=datetime.now)

class Mensaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    asunto = db.Column(db.String(100))
    mensaje = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now)

class Documento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    categoria = db.Column(db.String(50), nullable=False, default='General')
    ruta = db.Column(db.String(200), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now)

with app.app_context():
    db.create_all()

# --- LOGIN ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        if usuario == 'admin' and password == 'Acueducto2026':
            session['admin'] = True
            flash("Inicio de sesión exitoso. Bienvenido al panel.")
            return redirect(url_for('admin_noticias'))
        else:
            flash("Usuario o contraseña incorrectos. Intente de nuevo.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin', None)
    flash("Sesión cerrada correctamente.")
    return redirect(url_for('index'))

# --- RUTAS PÚBLICAS ---
@app.route('/')
def index():
    noticias = Noticia.query.order_by(Noticia.id.desc()).limit(3).all()
    return render_template('index.html', noticias=noticias)

@app.route('/noticias')
def noticias():
    noticias = Noticia.query.order_by(Noticia.id.desc()).all()
    return render_template('noticias.html', noticias=noticias)

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/enviar_contacto', methods=['POST'])
def enviar_contacto():
    nombre = request.form['nombre']
    correo = request.form['correo']
    asunto = request.form['asunto']
    contenido = request.form['mensaje']
    nuevo_mensaje = Mensaje(nombre=nombre, correo=correo, asunto=asunto, mensaje=contenido)
    db.session.add(nuevo_mensaje)
    db.session.commit()
    flash("¡Gracias! Su mensaje ha sido enviado a la administración.")
    return redirect(url_for('index'))

@app.route('/noticias')
def todas_noticias():
    noticias = Noticia.query.order_by(Noticia.id.desc()).all()
    return render_template('noticias.html', noticias=noticias)

@app.route('/transparencia')
def transparencia():
    documentos = Documento.query.order_by(Documento.fecha.desc()).all()
    return render_template('transparencia.html', documentos=documentos)

@app.route('/documentos/<filename>')
def ver_documento(filename):
    return send_from_directory(app.config['PDF_FOLDER'], filename)

# --- ADMINISTRACIÓN ---
@app.route('/admin')
def admin_noticias():
    if 'admin' not in session:
        flash("Por favor, inicie sesión para acceder a esta área.")
        return redirect(url_for('login'))
    noticias = Noticia.query.order_by(Noticia.id.desc()).all()
    documentos = Documento.query.order_by(Documento.fecha.desc()).all()
    return render_template('admin.html', noticias=noticias, documentos=documentos)

@app.route('/admin/noticia/nueva', methods=['POST'])
def crear_noticia():
    if 'admin' not in session:
        return redirect(url_for('login'))
    titulo = request.form['titulo']
    contenido = request.form['contenido']
    imagen_filename = None
    archivo = request.files.get('imagen')
    if archivo and allowed_file(archivo.filename):
        filename = secure_filename(archivo.filename)
        archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        imagen_filename = filename
    nueva_n = Noticia(titulo=titulo, contenido=contenido, imagen=imagen_filename)
    db.session.add(nueva_n)
    db.session.commit()
    flash("Noticia publicada con éxito.")
    return redirect(url_for('admin_noticias'))

@app.route('/admin/noticia/editar/<int:id>', methods=['POST'])
def editar_noticia(id):
    if 'admin' not in session:
        return redirect(url_for('login'))
    noticia = Noticia.query.get_or_404(id)
    noticia.titulo = request.form['titulo']
    noticia.contenido = request.form['contenido']
    archivo = request.files.get('imagen')
    if archivo and allowed_file(archivo.filename):
        filename = secure_filename(archivo.filename)
        archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        noticia.imagen = filename
    db.session.commit()
    flash("Noticia actualizada correctamente.")
    return redirect(url_for('admin_noticias'))

@app.route('/admin/noticia/borrar/<int:id>')
def borrar_noticia(id):
    if 'admin' not in session:
        return redirect(url_for('login'))
    noticia = Noticia.query.get_or_404(id)
    db.session.delete(noticia)
    db.session.commit()
    flash("Noticia eliminada correctamente.")
    return redirect(url_for('admin_noticias'))

@app.route('/admin/documento/subir', methods=['POST'])
def subir_documento():
    if 'admin' not in session:
        return redirect(url_for('login'))
    nombre = request.form['nombre']
    categoria = request.form['categoria']
    archivo = request.files.get('archivo')
    if not archivo or not allowed_pdf(archivo.filename):
        flash("Error: solo se permiten archivos PDF.")
        return redirect(url_for('admin_noticias'))
    filename = secure_filename(archivo.filename)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
    filename = timestamp + filename
    archivo.save(os.path.join(app.config['PDF_FOLDER'], filename))
    nuevo_doc = Documento(nombre=nombre, categoria=categoria, ruta=filename)
    db.session.add(nuevo_doc)
    db.session.commit()
    flash("Documento subido correctamente.")
    return redirect(url_for('admin_noticias'))

@app.route('/admin/documento/borrar/<int:id>')
def borrar_documento(id):
    if 'admin' not in session:
        return redirect(url_for('login'))
    doc = Documento.query.get_or_404(id)
    ruta_fisica = os.path.join(app.config['PDF_FOLDER'], doc.ruta)
    if os.path.exists(ruta_fisica):
        os.remove(ruta_fisica)
    db.session.delete(doc)
    db.session.commit()
    flash("Documento eliminado correctamente.")
    return redirect(url_for('admin_noticias'))

if __name__ == '__main__':
    app.run(debug=True)