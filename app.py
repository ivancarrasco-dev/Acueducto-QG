import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Clave secreta genérica e independiente
app.secret_key = "acueducto_vereda_2026_seguro"

# Configuración de Base de Datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///acueducto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- MODELOS DE BASE DE DATOS ---
class Noticia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now)

class Mensaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    asunto = db.Column(db.String(100))
    mensaje = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now)

with app.app_context():
    db.create_all()

# --- SISTEMA DE LOGIN ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        
        # Credenciales de administrador
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
    noticias = Noticia.query.order_by(Noticia.id.desc()).all()
    return render_template('index.html', noticias=noticias)

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

# --- RUTAS DE ADMINISTRACIÓN (PROTEGIDAS) ---
@app.route('/admin')
def admin_noticias():
    if 'admin' not in session:
        flash("Por favor, inicie sesión para acceder a esta área.")
        return redirect(url_for('login'))
        
    noticias = Noticia.query.order_by(Noticia.id.desc()).all()
    mensajes = Mensaje.query.order_by(Mensaje.id.desc()).all()
    return render_template('admin.html', noticias=noticias, mensajes=mensajes)

@app.route('/admin/noticia/nueva', methods=['POST'])
def crear_noticia():
    if 'admin' not in session:
        return redirect(url_for('login'))
        
    titulo = request.form['titulo']
    contenido = request.form['contenido']
    nueva_n = Noticia(titulo=titulo, contenido=contenido)
    db.session.add(nueva_n)
    db.session.commit()
    
    flash("Noticia publicada con éxito.")
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

if __name__ == '__main__':
    app.run(debug=True)