#funciones Para aplicación de agenda 
#+++++ Examen de Recuperación +++++++
#Integrantes: 
#  Alan Martínez Ruiz   2183076595
#  Tania Salazar Ramírez  2183033769
# Roles: Alan integración de la aplicación y diseño de las funciones
#        Tania realización del frontend e investigación de docuemntación, creación del XML, DTD y XSL

from lxml import etree



def AgregarXML(nombre, apellido, telefono, celular, correo, codigoPostal, estado, direccion):
    
    docXml = etree.parse("xml/agenda.xml")
    arbol = docXml.getroot()
    
    #Se crea el  nodo (contacto) y los subnodos (subelementos) del XML
    
    contacto = etree.Element("contacto")
    contacto.append(etree.Element("nombre"))
    contacto.append(etree.Element("apellido"))
    contacto.append(etree.Element("telefono"))
    contacto.append(etree.Element("celular"))
    contacto.append(etree.Element("correo"))
    contacto.append(etree.Element("codigoPostal"))
    contacto.append(etree.Element("estado"))
    contacto.append(etree.Element("direccion"))
    
    #Se asigna el texto ingresado desde el formulario a cada etiqueta 
    contacto[0].text = nombre
    contacto[1].text = apellido
    contacto[2].text = telefono
    contacto[3].text = celular
    contacto[4].text = correo
    contacto[5].text = codigoPostal
    contacto[6].text = estado
    contacto[7].text = direccion

    #Agregamos los el elemento (contacto) a la raiz de nuestro arbol (agenda)
    arbol.append(contacto)
    
    #Los agregamos al archivo xml de agenda
    docXml.write("xml/agenda.xml",  pretty_print=True, xml_declaration = True, encoding="utf-8")

def buscarContacto(nombre, apellido):
    doc = etree.parse('xml/agenda.xml')
    arbol = doc.getroot()

    #Para obtener todos los nodos "contacto"
    contactos = arbol.findall("contacto")

    #Hacemos un reocrrido en cada contacto de agenda hasta obtener el deseado por el usuario
    for c in contactos:
        #Se busca que los datos de entrada coincidan para obtener la información de ese contacto
        if c.find("nombre").text == nombre and c.find("apellido").text == apellido:
            print("Se encontró")
            telefono = c.find("telefono").text
            celular = c.find("celular").text
            correo = c.find("correo").text
            codigoPostal = c.find("codigoPostal").text
            estado = c.find("estado").text
            direccion = c.find("direccion").text
            print(telefono, celular, correo, codigoPostal, estado, direccion)
            
            #Regresamos los datos del contacto que se encontró y los imprimimos en consola previamente(aquí los quería regresar para imprimirlos en la aplicación)
            #Pero no me confundí usar el metodo get para poderlos mandar al template y que se mostrarán. Es la segunda vez que uso flask y estoy aprendiendo
            return(c, doc, telefono, celular, correo, codigoPostal, estado, direccion)

def Bcontacto(nombre, apellido):
    doc = etree.parse('xml/agenda.xml')
    arbol = doc.getroot()

    #Se obtiene el nodo (contacto) con los nodos hijos 
    contactos = arbol.findall("contacto")

    # para cada contacto en la lista de contactos 
    for c in contactos:
        #Buscamos si los parámetros dados por el usuario ocorrespondne a alguno dentro de nuestra agenda
        if c.find("nombre").text == nombre and c.find("apellido").text == apellido:
            #Se manda el mensaje si se ha encontrado 
            print("Encontrado!")
            return c, doc

def eliminarContacto(nombre, apellido):
    if Bcontacto(nombre, apellido) != 0:
        #Se busca dentro de la agenda 
        c, doc = Bcontacto(nombre, apellido)
        # se obtiene la raiz 
        raiz = doc.getroot()
        #Se elimina el nodo raiz (contacto seleccionado)
        raiz.remove(c)  
        #Se guardan los cambios
        doc.write("xml/agenda.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")  
    
    
    else:
        return 0

def impresion():
    dom = etree.parse('xml/agenda.xml')
    transform = etree.XSLT(etree.parse('xml/estilo.xsl'))
    nuevodom = transform(dom)
    resultado = etree.tostring(nuevodom, pretty_print=True, encoding="utf-8")
    #Se manda a escribir en un template vacio para que se pueda visualizar en la aplicación 
    g = open(f"templates/impresion.html", "wb")
    g.write(resultado)
    g.close()


def modificarContacto(nombre, apellido, nuevotelefono, nuevoCelular, nuevomail, nuevoCP, nuevoestado, nuevodireccion):
    if Bcontacto(nombre, apellido) != 0:
        # si no regresa un 0 es porque si se encuentra el contacto por lo que se obtienen sus datos
        c, doc = Bcontacto(nombre, apellido)
        # se cambia el valor por los valores que mandaron en el formulario
        c.find("telefono").text = nuevotelefono
        c.find("celular").text = nuevoCelular
        c.find("correo").text = nuevomail
        c.find("codigoPostal").text = nuevoCP
        c.find("estado").text = nuevoestado
        c.find("direccion").text = nuevodireccion
        doc.write("xml/agenda.xml", pretty_print=True, xml_declaration=True, encoding="utf-8")
    else:
        
        return 0
    
def validarXML():
    doc = etree.parse("xml/agenda.xml")
    dtd = etree.DTD("xml/agenda.dtd")   
    arbol = doc.getroot()
    print(f"La validacion del archivo  es {dtd.validate(arbol)} ")
    #Regresa true si es valido y false si no lo es
    return dtd.validate(arbol)  