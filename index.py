from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)

#obtenemos la conexion, objeto/variable cur (cursor)
miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
cur = miConexion.cursor()

#creacion de clave secreta para sesiones. Argumentar (investigar?)
app.secret_key = 'mysecretkey'
#-----------------------------------------------------------------------------
# RUTA 1_Inicio
@app.route('/')             # Comentario: El objeto app.funcion (ruta index /)
def home():                 # definir metodo home()
 
    return render_template('pagina1.html')
#-----------------------------------------------------------------------------
# RUTA 2_Cliente
@app.route('/pagina2', methods=["GET", "POST"])
def pagina2():                # definir metodo pagina()
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()

    #establecemos consulta SQL
    sql = "SELECT * FROM cliente"
    #ejecutar consulta
    cur.execute(sql)
    print(cur)

    return render_template("pagina2.html", clientes = cur)

@app.route('/agregar_cliente', methods=["GET","POST"])
def pagina2_agregar_cliente():
    if request.method=='POST':
        tipo_documento=request.form['tipo_documento']
        id_cliente=request.form['id_cliente']
        nom_cliente=request.form['nom_cliente']
        apell_cliente=request.form['apell_cliente']
        edad_client=request.form['edad_cliente']
        peso_cliente=request.form['peso_cliente']
        tsangre_cliente=request.form['tsangre_cliente']
        condmedica_cliente=request.form['condmedica_cliente']
        cel_cliente=request.form['cel_cliente']
        correo_cliente=request.form['correo_cliente']
        id_rutina=request.form['id_rutina']
        id_maquina=request.form['id_maquina']
        id_producto=request.form['id_producto']
        
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
        cur = miConexion.cursor()

            
            #establecemos consulta SQL
        sql = "INSERT INTO cliente (tipo_documento, id_cliente, nom_cliente, apell_cliente, edad_client, peso_cliente, tsangre_cliente, condmedica_cliente ,cel_cliente, correo_cliente, id_rutina, id_maquina, id_producto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (tipo_documento, id_cliente, nom_cliente, apell_cliente, edad_client, peso_cliente, tsangre_cliente, condmedica_cliente, cel_cliente, correo_cliente, id_rutina , id_maquina, id_producto)
            
        #ejecutar consulta SQL - cur (objeto/variable)
        cur.execute(sql, val)
        #guardamos en la BD pitbull_gym
        miConexion.commit()
        #cerrar conexion
        #miConexion.close

        #flash('Registro insertado.')

    return redirect(url_for('pagina2'))

@app.route('/borrarcliente/<string:id>')
def borrar_clientes(id):
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
        cur = miConexion.cursor()

        #establecemos consulta SQL
        sql = "DELETE FROM cliente WHERE id_cliente= {0}".format(id)
        #ejecutar consulta
        cur.execute(sql)
        #guardamos en la BD
        miConexion.commit()
        #cerrar conexion
        #miConexion.close


        #flash('Registro eliminado.')

        return redirect(url_for('pagina2'))

@app.route('/editarcliente/<string:id>')
def editar_clientes(id):                # definir metodo pagina()
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
        cur = miConexion.cursor()       

        #establecemos consulta SQL
        sql = "SELECT * FROM cliente WHERE id_cliente= {0}".format(id)
            
        #ejecutar consulta
        cur.execute(sql)
        #los datos que se traen de la consulta se guardan en data
        data = cur.fetchall()
        #verificando en la terminal los datos a modificar
        print(data)
    
        #llamando a la vista donde se va a mostrar el registro a modificar
        #se va a utilizar la variable cat en la vista para mostrar los datos
        return render_template("editar_cliente.html", cat = data[0])

@app.route('/actualizarcliente/<string:id>', methods=["POST"])
def actualizar_cliente(id):  # definir metodo pagina()
    #capturar datos del formulario
    if request.method=='POST':
        tipo_documento=request.form['tipo_documento']
        id_cliente=request.form['id_cliente']
        nom_cliente=request.form['nom_cliente']
        apell_cliente=request.form['apell_cliente']
        edad_client=request.form['edad_cliente']
        peso_cliente=request.form['peso_cliente']
        tsangre_cliente=request.form['tsangre_cliente']
        condmedica_cliente=request.form['condmedica_cliente']
        cel_cliente=request.form['cel_cliente']
        correo_cliente=request.form['correo_cliente']
        id_rutina=request.form['id_rutina']
        id_maquina=request.form['id_maquina']
        id_producto=request.form['id_producto']
    
    
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()
    
    #establecemos consulta SQL
    sql = "UPDATE cliente SET tipo_documento=%s, nom_cliente=%s, apell_cliente=%s, edad_client=%s, peso_cliente=%s,tsangre_cliente=%s,condmedica_cliente=%s,cel_cliente=%s,correo_cliente=%s,id_rutina=%s,id_maquina=%s,id_producto=%s WHERE id_cliente=%s "
    val = (tipo_documento , nom_cliente, apell_cliente, edad_client, peso_cliente,tsangre_cliente,condmedica_cliente,cel_cliente,correo_cliente,id_rutina,id_maquina,id_producto, id_cliente)
        
    #ejecutar consulta SQL - cur (objeto/variable)

    #ejecutar consulta
    cur.execute(sql, val)
        #guardamos en la BD

    miConexion.commit()
        #cerrar conexion
        #miConexion.close    

    return redirect(url_for("pagina2"))










#-----------------------------------------------------------------------
# RUTA 3_instructor
@app.route('/pagina3', methods=["GET", "POST"])
def pagina3():                # definir metodo pagina()

    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()

    #establecemos consulta SQL
    sql = "SELECT * FROM instructor"
    #ejecutar consulta
    cur.execute(sql)
    print(cur)

    return render_template("pagina3.html", instructor = cur)



@app.route('/agregar_instructor', methods=["GET","POST"])
def pagina3_agregar_instructor():

    if request.method=='POST':
        id_instructor=request.form['id_instructor']
        nom_instructor=request.form['nom_instructor']
        apell_instructor=request.form['apell_instructor']
        edad_instructor=request.form['edad_instructor']
        cel_instructor=request.form['cel_instructor']
        correo_instructor=request.form['correo_instructor']
        exp_instructor=request.form['exp_instructor']
        id_cliente=request.form['id_cliente']

        
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
        cur = miConexion.cursor()

        #establecemos consulta SQL
        sql = "INSERT INTO instructor (id_instructor ,nom_instructor, apell_instructor ,edad_instructor ,cel_instructor, correo_instructor, exp_instructor, id_cliente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (id_instructor, nom_instructor, apell_instructor, edad_instructor, cel_instructor, correo_instructor, exp_instructor, id_cliente)
 
        #ejecutar consulta SQL - cur (objeto/variable)
        cur.execute(sql, val)
        #guardamos en la BD
        miConexion.commit()
        #cerrar conexion
        #miConexion.close
        #flash('Registro insertado.')

    return redirect(url_for('pagina3'))

@app.route('/borrarinstructor/<string:id>')
def borrar_instructor(id):

    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()

    #establecemos consulta SQL
    sql = "DELETE FROM instructor WHERE id_instructor= {0}".format(id)
    #ejecutar consulta
    cur.execute(sql)
    #guardamos en la BD
    miConexion.commit()
    #cerrar conexion
    #miConexion.close

    #flash('Registro eliminado.')

    return redirect(url_for('pagina3'))



@app.route('/editarinstructor/<string:id>')
def editar_instructor(id):                # definir metodo pagina()

    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()       

    #establecemos consulta SQL
    sql = "SELECT * FROM instructor WHERE id_instructor= {0}".format(id)
         
    #ejecutar consulta
    cur.execute(sql)
    #los datos que se traen de la consulta se guardan en data
    data = cur.fetchall()
    #verificando en la terminal los datos a modificar
    print(data)
   
    #llamando a la vista donde se va a mostrar el registro a modificar
    #se va a utilizar la variable cat en la vista para mostrar los datos
    return render_template("editar_instructor.html", cat = data[0])



@app.route('/actualizarinstructor/<string:id>', methods=["POST"])
def actualizar_instructor(id):                # definir metodo pagina()

    if request.method=='POST':

        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
        cur = miConexion.cursor()

        #capturar datos del formulario
        id_instructor=request.form['id_instructor']
        nom_instructor=request.form['nom_instructor']
        apell_instructor=request.form['apell_instructor']
        edad_instructor=request.form['edad_instructor']
        cel_instructor=request.form['cel_instructor']
        correo_instructor=request.form['correo_instructor']
        exp_instructor=request.form['exp_instructor']
        id_cliente=request.form['id_cliente']
           
        #establecemos consulta SQL
        sql = "UPDATE instructor SET nom_instructor = %s, apell_instructor = %s, edad_instructor= %s,cel_instructor= %s,correo_instructor = %s,exp_instructor = %s,id_cliente = %s WHERE id_instructor= %s"
        val = (nom_instructor, apell_instructor, edad_instructor,cel_instructor,correo_instructor,exp_instructor,id_cliente, id_instructor)
        
        #ejecutar consulta
        cur.execute(sql, val)
        #guardamos en la BD
        miConexion.commit()
        #cerrar conexion
        #miConexion.close    

        return redirect(url_for("pagina3"))










#-----------------------------------------------------------------------------
# RUTAS 4 de maquina

@app.route('/pagina4', methods=["GET", "POST"])
def pagina4():                # definir metodo pagina()
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()

    #establecemos consulta SQL
    sql = "SELECT * FROM maquina"
    #ejecutar consulta
    cur.execute(sql)
    print(cur)

    return render_template("pagina4.html", maquina = cur)

@app.route('/agregar_maquina', methods=["GET","POST"])
def pagina4_agregar_maquina():
    if request.method=='POST':
        id_maquina=request.form['id_maquina']
        nom_maquina=request.form['nom_maquina']
        numserie_maquina=request.form['numserie_maquina']
        modelo_maquina=request.form['modelo_maquina']
        peso_maquina=request.form['peso_maquina']
        utilidad_maquina=request.form['utilidad_maquina']
               

        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
        cur = miConexion.cursor()
        
        #establecemos consulta SQL  
        sql = "INSERT INTO maquina (nom_maquina,numserie_maquina,modelo_maquina,peso_maquina,utilidad_maquina, id_maquina) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nom_maquina , numserie_maquina,modelo_maquina,peso_maquina,utilidad_maquina, id_maquina)
        

        #ejecutar consulta SQL - cur (objeto/variable)
        cur.execute(sql, val)
        #guardamos en la BD
        miConexion.commit()
        #cerrar conexion
        #miConexion.close

        #flash('Registro insertado.')

    return redirect(url_for('pagina4'))


@app.route('/borrarmaquina/<string:id>')
def borrar_maquina(id):
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()

    #establecemos consulta SQL
    sql = "DELETE FROM maquina WHERE id_maquina= {0}".format(id)
    #ejecutar consulta
    cur.execute(sql)
    #guardamos en la BD
    miConexion.commit()
    #cerrar conexion
    #miConexion.close


    #flash('Registro eliminado.')

    return redirect(url_for('pagina4'))

@app.route('/editarmaquina/<string:id>')
def editar_maquina(id):                # definir metodo pagina()
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()

    #establecemos consulta SQL
    sql = "SELECT * FROM maquina WHERE id_maquina = {0}".format(id)
         
    #ejecutar consulta
    cur.execute(sql)
    #los datos que se traen de la consulta se guardan en data
    data = cur.fetchall()
    #verificando en la terminal los datos a modificar
    print(data)
   
    #llamando a la vista donde se va a mostrar el registro a modificar
    #se va a utilizar la variable cat en la vista para mostrar los datos
    return render_template("editar_maquina.html", fac = data[0])

@app.route('/actualizarmaquina/<string:id>', methods=["POST"])
def actualizar_maquina(id):                # definir metodo pagina()
    if request.method=='POST':
        #capturar datos del formulario
        id_maquina=request.form['id_maquina']
        nom_maquina=request.form['nom_maquina']
        numserie_maquina=request.form['numserie_maquina']
        modelo_maquina=request.form['modelo_maquina']
        peso_maquina=request.form['peso_maquina']
        utilidad_maquina=request.form['utilidad_maquina']
               
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
        cur = miConexion.cursor()
        
        #establecemos consulta SQL
        sql = "UPDATE maquina SET  nom_maquina = %s,numserie_maquina= %s,modelo_maquina= %s,peso_maquina= %s,utilidad_maquina= %s  WHERE id_maquina= %s"
        val = (nom_maquina, numserie_maquina, modelo_maquina, peso_maquina, utilidad_maquina, id_maquina)
        
        #ejecutar consulta
        cur.execute(sql, val)
        #guardamos en la BD
        miConexion.commit()
        #cerrar conexion
        #miConexion.close    

        return redirect(url_for("pagina4"))

#-----------------------------------------------------------------------------
# RUTA 5_Producto
@app.route('/pagina5', methods=["GET", "POST"])
def pagina5():                # definir metodo pagina()
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()

    #establecemos consulta SQL
    sql = "SELECT * FROM producto"
    #ejecutar consulta
    cur.execute(sql)
    print(cur)

    return render_template("pagina5.html", producto = cur)

@app.route('/agregar_producto', methods=["GET","POST"])
def pagina5_agregar_producto():
    if request.method=='POST':
        id_producto=request.form['id_producto']
        nom_producto=request.form['nom_producto']
        valor_producto=request.form['valor_producto']
        utilidad_producto=request.form['utilidad_producto']
        
        
        

        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
        cur = miConexion.cursor()

        sql = "INSERT INTO producto (id_producto,nom_producto,valor_producto,utilidad_producto) VALUES (%s, %s, %s, %s)"
        val = (id_producto,nom_producto,valor_producto,utilidad_producto)
        

        #ejecutar consulta SQL - cur (objeto/variable)
        cur.execute(sql, val)
        #guardamos en la BD
        miConexion.commit()
        #cerrar conexion
        #miConexion.close

        #flash('Registro insertado.')

    return redirect(url_for('pagina5'))

@app.route('/borrarproducto/<string:id>')
def borrar_producto(id):
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()

    #establecemos consulta SQL
    sql = "DELETE FROM producto WHERE id_producto= {0}".format(id)
    #ejecutar consulta
    cur.execute(sql)
    #guardamos en la BD
    miConexion.commit()
    #cerrar conexion
    #miConexion.close


    #flash('Registro eliminado.')

    return redirect(url_for('pagina5'))

@app.route('/editarproducto/<string:id>')
def editar_producto(id):                # definir metodo pagina()
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()

    #establecemos consulta SQL
    sql = "SELECT * FROM producto WHERE id_producto= {0}".format(id)
         
    #ejecutar consulta
    cur.execute(sql)
    #los datos que se traen de la consulta se guardan en data
    data = cur.fetchall()
    #verificando en la terminal los datos a modificar
    print(data)
   
    #llamando a la vista donde se va a mostrar el registro a modificar
    #se va a utilizar la variable cat en la vista para mostrar los datos
    return render_template("editar_producto.html", pro = data[0])

@app.route('/actualizarproducto/<string:id>', methods=["POST"])
def actualizar_producto(id):                # definir metodo pagina()
    if request.method=='POST':
        #capturar datos del formulario
        id_producto=request.form['id_producto']
        nom_producto=request.form['nom_producto']
        valor_producto=request.form['valor_producto']
        utilidad_producto=request.form['utilidad_producto']
        

        
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
        cur = miConexion.cursor()
        
        #establecemos consulta SQL
        sql = "UPDATE producto SET nom_producto = %s, valor_producto = %s, utilidad_producto = %s WHERE id_producto= %s"
        val = (nom_producto, valor_producto, utilidad_producto, id_producto)
        
        #ejecutar consulta
        cur.execute(sql, val)
        #guardamos en la BD
        miConexion.commit()
        #cerrar conexion
        #miConexion.close    

        return redirect(url_for("pagina5"))
    
    #-----------------------------------------------------------------------------
# RUTA 6_rutina
@app.route('/pagina6', methods=["GET", "POST"])
def pagina6():                # definir metodo pagina()
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()

    #establecemos consulta SQL
    sql = "SELECT * FROM rutina"
    #ejecutar consulta
    cur.execute(sql)
    print(cur)

    return render_template("pagina6.html", rutina = cur)

@app.route('/agregar_rutina', methods=["GET","POST"])
def pagina6_agregar_rutina():
    if request.method=='POST':
        id_rutina=request.form['id_rutina']
        aliment_rutina=request.form['aliment_rutina']
        intensidad_rutina=request.form['intensidad_rutina']
        dias_rutina=request.form['dias_rutina']
        
        
        

        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
        cur = miConexion.cursor()

        sql = "INSERT INTO rutina (id_rutina,aliment_rutina,intensidad_rutina,dias_rutina) VALUES (%s, %s, %s, %s)"
        val = (id_rutina,aliment_rutina,intensidad_rutina,dias_rutina)
        

        #ejecutar consulta SQL - cur (objeto/variable)
        cur.execute(sql, val)
        #guardamos en la BD
        miConexion.commit()
        #cerrar conexion
        #miConexion.close

        #flash('Registro insertado.')

    return redirect(url_for('pagina6'))

@app.route('/borrarrutina/<string:id>')
def borrar_rutina(id):

    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()
    
    
    #establecemos consulta SQL
    sql = "DELETE FROM rutina WHERE id_rutina= {0}".format(id)
    #ejecutar consulta
    cur.execute(sql)
    #guardamos en la BD
    miConexion.commit()
    #cerrar conexion
    #miConexion.close


    #flash('Registro eliminado.')

    return redirect(url_for('pagina6'))

@app.route('/editarrutina/<string:id>')
def editar_rutina(id):                # definir metodo pagina5()
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
    cur = miConexion.cursor()

    #establecemos consulta SQL
    sql = "SELECT * FROM rutina WHERE id_rutina= {0}".format(id)
         
    #ejecutar consulta
    cur.execute(sql)
    #los datos que se traen de la consulta se guardan en data
    data = cur.fetchall()
    #verificando en la terminal los datos a modificar
    print(data)

    #llamando a la vista donde se va a mostrar el registro a modificar
    #se va a utilizar la variable cat en la vista para mostrar los datos
       
    return render_template("editar_rutina.html", fac = data[0])
       
       

@app.route('/actualizarrutina/<string:id>', methods=["POST"])
def cambiar_rutina(id):                # definir metodo pagina5()
    if request.method=='POST':
        #capturar datos del formulario
        id_rutina=request.form['id_rutina']
        aliment_rutina=request.form['aliment_rutina']
        intensidad_rutina=request.form['intensidad_rutina']
        dias_rutina=request.form['dias_rutina']
           
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='', db='pitbull_gym' )
        cur = miConexion.cursor()

        #establecemos consulta SQL
        sql = "UPDATE rutina SET aliment_rutina = %s,intensidad_rutina = %s,dias_rutina = %s WHERE id_rutina= %s"
        val = (aliment_rutina,intensidad_rutina,dias_rutina, id_rutina)
        #ejecutar consulta
        cur.execute(sql, val)
        #guardamos en la BD
        miConexion.commit()
        #cerrar conexion
        #miConexion.close    

        return redirect(url_for("pagina6"))








#-----------------------------------------------------------------------------
if __name__ == '__main__':  # Validar el archivo principal para correr la aplicacion
    app.run(debug=True)
