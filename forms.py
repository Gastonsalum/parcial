#Archivos con las clases de formulario

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

# Clase de formulario de ingreso de producto

class ProductoForm(FlaskForm):
    producto = StringField('Ingrese el nombre del producto ', validators=[Required()])
    enviar = SubmitField('Buscar')

# Clase de formulario de ingreso de cliente

class ClienteForm(FlaskForm):
    cliente = StringField('Ingrese el nombre del cliente ', validators=[Required()])
    enviar = SubmitField('Buscar')

# Clase de formulario de ingreso de Login

class LoginForm(FlaskForm):
    usuario = StringField('Nombre de usuario', validators=[Required()])
    password = PasswordField('Contraseña', validators=[Required()])
    enviar = SubmitField('Ingresar')

#------------------------------------------------------------------------

# Clase de formulario para realizar el registro de usuario nuevo

class RegistrarForm(LoginForm):
    password_check = PasswordField('Verificar Contraseña', validators=[Required()])
    enviar = SubmitField('Registrarse')

#Clase de formulario para realizar el cambio de contraseña de usuario Existente

class CambiarForm(FlaskForm):
    password = PasswordField('Contraseña Nueva', validators=[Required()])
    password_check = PasswordField('Verificar Contraseña', validators=[Required()])
    enviar = SubmitField('Aceptar')

