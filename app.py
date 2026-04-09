import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "clave_secreta_sena"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)

# --- MODELOS ---
class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    contenido = db.Column(db.Text)

class Documento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    ruta = db.Column(db.String(200))

# NUEVA TABLA PARA EL FORMULARIO
class Mensaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    correo = db.Column(db.String(100))
    asunto = db.Column(db.String(100))
    mensaje = db.Column(db.Text)

with app.app_context():
    db.create_all()

# --- RUTAS ---

@app.route('/')
def index():
    todas_noticias = Noticia.query.all()
    return render_template('index.html', noticias=todas_noticias)

# NUEVA RUTA PARA PROCESAR EL CONTACTO
@app.route('/enviar_contacto', methods=['POST'])
def enviar_contacto():
    nombre = request.form['nombre']
    correo = request.form['correo']
    asunto = request.form['asunto']
    contenido = request.form['mensaje']
    
    nuevo_mensaje = Mensaje(nombre=nombre, correo=correo, asunto=asunto, mensaje=contenido)
    db.session.add(nuevo_mensaje)
    db.session.commit()
    
    flash("¡Gracias! Tu mensaje ha sido enviado a la asociación.")
    return redirect(url_for('index'))

@app.route('/transparencia', methods=['GET', 'POST'])
def transparencia():
    if request.method == 'POST':
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