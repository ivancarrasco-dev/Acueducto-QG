import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "clave_secreta_sena"

# Configuración de Base de Datos y Archivos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Máximo 16MB por PDF
db = SQLAlchemy(app)

# Asegurar que la carpeta de subidas existe
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Modelo de la Base de Datos
class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)

class Documento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ruta = db.Column(db.String(200), nullable=False)

# Crear las tablas al iniciar
with app.app_context():
    db.create_all()

# --- RUTAS ---

@app.route('/')
def index():
    todas_noticias = Noticia.query.order_by(Noticia.id.desc()).all()
    return render_template('index.html', noticias=todas_noticias)

@app.route('/transparencia', methods=['GET', 'POST'])
def transparencia():
    if request.method == 'POST':
        # Lógica para subir PDF
        file = request.files['archivo']
        nombre_doc = request.form['nombre']
        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            nuevo_doc = Documento(nombre=nombre_doc, ruta=filename)
            db.session.add(nuevo_doc)
            db.session.commit()
            flash("Documento subido con éxito")
            return redirect(url_for('transparencia'))
    
    documentos = Documento.query.all()
    return render_template('transparencia.html', documentos=documentos)

if __name__ == '__main__':
    app.run(debug=True)