vfrom types import MethodType
from flask import Flask, render_template, request, url_for, make_response
from funciones import AgregarXML, buscarContacto, eliminarContacto, impresion, modificarContacto, validarXML

# objeto apara crear rutas
app = Flask(__name__)

@app.route('/')
def inicio():
    title = "Hola Mundo"
    return render_template('inicio.html', title=title)

@app.route('/base', methods=['GET', 'POST'])
def formulario_1():
    if request.method == 'POST':
        nombre = request.form['Fnombre']
        apellido = request.form['Fapellido']
        telefono = request.form['Ftelefono']
        celular = request.form['Fcelular']
        correo = request.form['Fcorreo']
        codigoPostal = request.form['FcodigoPostal']
        estado = request.form['Festado']
        direccion = request.form['Fdireccion']
        AgregarXML(nombre, apellido, telefono, celular, correo, codigoPostal, estado, direccion)
        validarXML()
        
        
    return render_template('base.html')  

@app.route('/mensaje')
def mensaje():
    return render_template('mensaje.html')

@app.route('/mensaje2')
def mensaje2():
    return render_template('mensaje2.html')

@app.route('/invalido')
def invalido():
    return render_template('invalido.html')  

@app.route('/resultado')
def resultado():
    return render_template('resultado.html') 

@app.route('/eliminado')
def eliminado():
    return render_template('eliminado.html') 

@app.route('/formulario_eliminar_contacto', methods=['GET', 'POST'])
def formulario_2():
    if request.method =='POST':
        nombre = request.form['Dnombre']
        apellido = request.form['Dapellido']

        eliminarContacto(nombre, apellido)
        return render_template('eliminado.html')

    return render_template('formulario_eliminar_contacto.html')  

@app.route('/formulario_buscar_contacto', methods=['GET', 'POST'] )
def formulario_3():
    if request.method =='POST':
        nombre = request.form['Bnombre']
        apellido = request.form['Bapellido']
        
        buscarContacto(nombre, apellido)      

    return render_template('formulario_buscar_contacto.html')  

@app.route('/formulario_modificar_contacto', methods=['GET', 'POST'] )
def formulario_4():
    if request.method == 'POST':
        nombre = request.form['Fnombre']
        apellido = request.form['Fapellido']
        nuevotelefono = request.form['Ftelefono']
        nuevoCelular = request.form['Fcelular']
        nuevomail = request.form['Fcorreo']
        nuevoCP = request.form['FcodigoPostal']
        nuevoestado = request.form['Festado']
        nuevodireccion = request.form['Fdireccion']

        modificarContacto(nombre, apellido, nuevotelefono, nuevoCelular, nuevomail, nuevoCP, nuevoestado, nuevodireccion)
        return render_template('mensaje2.html')

    return render_template('formulario_modificar_contacto.html')  

@app.route('/impresion')
def impresionAgenda():
    impresion()
    return render_template('impresion.html')



# ctrl+shift+r para recargar sin cache
if __name__ == '__main__':
    app.run(debug=True)