#!/usr/bin/env python

#Importaciones

import csv
import funciones
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, session, send_file
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager
from forms import LoginForm, ProductoForm, ClienteForm, RegistrarForm, CambiarForm

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'un string que funcione como llave'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

archivo = 'ventas.csv'

funciones.validar_archivo(archivo)

registros = funciones.generar_clase(archivo)

#Ruteos

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/farmasoft')
def index2():
    if 'username' in session:
        return render_template('index2.html')
    else:
        flash('Para Acceder debe Loguearse')
        return redirect(url_for('ingresar'))



@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    formulario = LoginForm()

    if formulario.validate_on_submit():
        with open('usuarios') as archivo:
            archivo_csv = csv.reader(archivo)
            registro = next(archivo_csv)
            while registro:
                if formulario.usuario.data == registro[0] and formulario.password.data == registro[1]:
                    session['username'] = formulario.usuario.data
                    return redirect(url_for('ultimos'))
                registro = next(archivo_csv, None)
            else:
                flash('fallo al loguearse')
                return redirect(url_for('ingresar'))
    return render_template('login.html', formulario=formulario)



@app.route('/logout', methods=['GET'])
def logout():
    if 'username' in session:
        session.pop('username')
        return render_template('logged_out.html')
    else:
        return redirect(url_for('index'))



@app.route('/ultimos', methods=['GET', 'POST'])
def ultimos():
    if 'username' in session:   
        ultimas = 5
        ul_ventas = []
        registros = funciones.generar_clase(archivo)
        registros_reverse = registros.reverse()
        while ultimas > len(registros):
            ultimas -= 1
        x = 0
        for x in range(ultimas):
            ul_ventas.append(registros[x])
            x +=1
        return render_template('ultimos.html',ul_ventas=ul_ventas)
    else:
        return redirect(url_for('ingresar'))




@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if 'username' in session:
        formulario = ClienteForm()
        if formulario.validate_on_submit():
            cliente = formulario.cliente.data.upper()
            if funciones.min_caracteres(cliente) == -1:
                flash('Debe Ingresar mas de 3 Caracteres')
                return render_template('productos.html', form = formulario)
            else:
                clientes = funciones.clientes(registros,cliente)
                if len(clientes) == 0:
                    flash('No se Encontro ningun cliente')
                elif len(clientes) == 1:
                    cliente_unico = funciones.buscar_cli_o_prod(registros,cliente, None)
                    funciones.exportar(cliente_unico,'productos')
                    return render_template('productos.html', form = formulario, listar = cliente_unico, cliente= formulario.cliente.data.upper())
                else:
                    return render_template('productos.html', form = formulario, clientes = clientes)
        return render_template('productos.html', form = formulario)
    else:
        return redirect(url_for('ingresar'))


#Ruteo para multiples resultados de producto

@app.route('/productos/<clientes>', methods=['GET', 'POST'])
def productos2(clientes):
    if 'username' in session:
            cliente = clientes
            cliente_unico = funciones.buscar_cli_o_prod(registros,cliente, None)
            funciones.exportar(cliente_unico,'productos')
            return render_template('productos2.html', listar = cliente_unico, cliente= cliente)
    else:
        return redirect(url_for('ingresar'))

#Ruteo para multiples resultados de cliente

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if 'username' in session:
        formulario = ProductoForm()
        if formulario.validate_on_submit():
            producto = formulario.producto.data.upper()
            if funciones.min_caracteres(producto) == -1:
                flash('Debe Ingresar mas de 3 Caracteres')
                return render_template('prod_clientes.html', form = formulario)
            else:
                productos = funciones.productos(registros,producto)
                if len(productos) == 0:
                    flash('No se Encontro ningun producto')
                elif len(productos) == 1:
                    producto_unico = funciones.buscar_cli_o_prod(registros,producto, True)
                    funciones.exportar(producto_unico,'clientes')
                    return render_template('clientes.html', form = formulario, listar = producto_unico, producto= formulario.producto.data.upper())
                else:
                    return render_template('clientes.html', form = formulario, productos = productos)
        return render_template('clientes.html', form=formulario)
    else:
        return redirect(url_for('ingresar'))



@app.route('/clientes/<productos>', methods=['GET', 'POST'])
def clientes2(productos):
    if 'username' in session:
        producto = productos
        producto_unico = funciones.buscar_cli_o_prod(registros,producto, True)
        funciones.exportar(producto_unico,'clientes')
        return render_template('clientes2.html', listar = producto_unico, producto = producto)
    else:
        return redirect(url_for('ingresar'))





@app.route('/mas_vendidos', methods=['GET', 'POST'])
def mas_vendidos():
    if 'username' in session:
        cantidad = 5
        producto = funciones.mas_vendidos(registros = registros, cantidad=cantidad)
        funciones.exportar(producto,'vendidos')
        return render_template('prod_vendidos.html', produc = producto)
    else:
        return redirect(url_for('ingresar'))




@app.route('/clientes_vip', methods=['GET', 'POST'])
def clientes_vip():
    if 'username' in session:
        cantidad = 3
        clientes = funciones.clientes_vip(registros = registros, cantidad=cantidad)
        funciones.exportar(clientes,'vips')
        return render_template('mej_clientes.html', produc = clientes)
    else:
        return redirect(url_for('ingresar'))



@app.errorhandler(404)
def no_encontrado(e):
    if 'username' in session:
        return render_template('404.html'), 404
    else:
        flash('ERROR:404 Recurso NO ENCONTRADO')
        return redirect(url_for('ingresar'))

@app.errorhandler(500)
def error_interno(e):
    if 'username' in session:
        return render_template('500.html'), 500
    else:
        flash('ERROR:500 Error Interno')
        return redirect(url_for('ingresar'))

#-------------------------------------------------------------------

#Agregado para Final

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    formulario = RegistrarForm()
    if formulario.validate_on_submit():
        existe = funciones.existe(formulario.usuario.data)
        if existe == True:
            flash('El Usuario ya Existe!!!')
            return redirect(url_for('registrar'))
        elif existe == False:
            if formulario.password.data == formulario.password_check.data:
                with open('usuarios', 'a+') as archivo:
                    archivo_csv = csv.writer(archivo)
                    registro = [formulario.usuario.data, formulario.password.data]
                    archivo_csv.writerow(registro)
                flash('Usuario creado correctamente')
                return redirect(url_for('ingresar'))
            else:
                flash('Las passwords deben ser iguales')
    return render_template('registrar.html', form=formulario,fecha_actual=datetime.utcnow())


@app.route('/cambiar', methods=['GET', 'POST'])
def cambiar():
    if 'username' in session:
        formulario = CambiarForm()
        if formulario.validate_on_submit():
            if formulario.password.data == formulario.password_check.data:
                usuario = session['username'] 
                funciones.cambiarclave(usuario, formulario.password.data)
                flash('Se cambio con exito la clave')
                return redirect(url_for('ingresar'))
            else:
                flash('Las passwords deben ser iguales')
                return render_template('cambiar.html', formulario=formulario)
        return render_template('cambiar.html', formulario=formulario)
    else:
        return redirect(url_for('ingresar'))


@app.route('/exportar/')
def export():
    if 'username' in session:
        nombre = 'resultado_' + datetime.today().strftime('%Y%m%d_%H%M%S')+ '.csv'
        return send_file('consulta.csv', as_attachment=True, attachment_filename=nombre, cache_timeout=8)
    else:
        return redirect(url_for('ingresar'))



if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    manager.run()
