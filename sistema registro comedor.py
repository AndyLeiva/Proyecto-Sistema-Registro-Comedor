#modulos importados 
import sqlite3 as sql #MODULO PARA BASES DE DATOS SQL
import time # MODULO PARA EL TIEMPO DE REGISTRO
import getpass # MODULO PARA LAS CONTRASEÑAS

#FUNCION PARA LA CONEXION DE LA BASE DE DATOS
def crearBD():
    conexion = sql.connect("Estudiantes.db")
    cursor = conexion.cursor()
    conexion.close()

#FUNCION PARA CREAR LAS TABLAS DE LA BASE DE DATOS
def crearTabla():
    conexion = sql.connect("Estudiantes.db")
    cursor = conexion.cursor()   
#Datos del estudiante | Tabla de Estudiantes
#Columnas: Cedula, Nombre, Sección
    cursor.execute(
    """CREATE TABLE Estudiantes (
        cedula integer,
        nombre text,
        seccion text
    )"""
    )
#Se guarda la entrada del estudiante 
#Columnas: Cedula, Nombre, Sección, Fecha y Hora
# Tabla de Registro de ingreso de los estudiantes al comedor
    cursor.execute(
        """CREATE TABLE Registros (
            cedula integer,
            nombre text,
            seccion text,
            fecha text,
            hora text

        )"""
    )
    conexion.commit()
    conexion.close()


#FUNCION PARA AGREGAR EL ESTUDIANTE EN LA TABLA ESTUDIANTES 
# | DATOS(CEDULA, NOMBRE COMPLETO, SECCION)
def insertardatos(cedula, nombre, seccion): 
    conexion = sql.connect("Estudiantes.db")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO Estudiantes VALUES({cedula}, '{nombre}', '{seccion}')"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()

#FUNCION PARA CONSULTAR LA TABLA ESTUDIANTE | DATOS(CEDULA, NOMBRE, SECCION)
def consultaEstudiante():
    conexion = sql.connect("Estudiantes.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM Estudiantes"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print("INFORMACIÓN DE LOS ESTUDIANTES\n\n",datos)


#FUNCION PARA CONSULTAR LA TABLA REGISTRO | DATOS(CEDULA, NOMBRE, SECCION, FECHA, HORA)
def consultaRegistro():
    conexion = sql.connect("Estudiantes.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM Registros"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print("INFORMACIÓN DE LOS ESTUDIANTES\n\n",datos)
    
#FUNCION PARA QUE EL PROGRAMA BUSQUE EL ESTUDIANTE POR MEDIO DE LA CEDULA
def buscarDatos(cedula):
    conexion = sql.connect("Estudiantes.db")
    cursor = conexion.cursor()
    instruccion1 = f"SELECT * FROM Estudiantes WHERE cedula = {cedula}"
    cursor.execute(instruccion1)
    consulta = cursor.fetchall()
    conexion.commit()
    conexion.close()
    
    
    if consulta == []: #CONDICION PARA ENCONTRAR EL ESTUDIANTE EN LA BASE DE DATOS
        print("ESTE ESTUDIANTE NO ESTÁ REGISTRADO EN EL SISTEMA")
    else:
        #print("ESTUDIANTE:\n",consulta)
        datosEstudiante = list(consulta[0])
#VARIABLES PARA EXTRACCION DE LOS DATOS A REGISTRAR
        cedula = datosEstudiante[0]
        nombre = datosEstudiante[1]
        seccion = datosEstudiante[2]
        fecha = time.strftime("%x")
        hora = time.strftime("%X")

        print("=================================\n")
        print("Nombre del estudiante: ", nombre)
        print("Sección: ", seccion)
        print("Fecha: ", fecha)
        print("Hora: ", hora)
        print("\n================================")
        print("ACCESO REGISTRADO CORRECTAMENTE")
        print("\n================================")
        

        
        
        
#FUNCION PARA QUE LOS DATOS SE REGISTREN EN LA BASE DE DATOS AUTOMMÁTICAMENTE
        def insertarRegistros(cedula, nombre, seccion, fecha, hora): #TABLA DE REGISTROS
            conexion = sql.connect("Estudiantes.db")
            cursor = conexion.cursor()
            instruccion = f"INSERT INTO Registros VALUES({cedula}, '{nombre}', '{seccion}', '{fecha}', '{hora}')"
            cursor.execute(instruccion)
            conexion.commit()
            conexion.close()

        insertarRegistros(cedula, nombre, seccion, fecha, hora)
        
            

#MAIN | DONDE SE ENCUENTRA EL MENU PRINCIPAL PARA EJECUTAR 
# LAS FUNCIONES DEL SISTEMA DE REGISTRO DE COMEDOR
if __name__ == "__main__":
    print("Sistema Registro Comedor")
    try:                    
        crearBD()
        crearTabla()
        print("SE HA CREADO LA BASE DE DATOS")
        creacionBD = 1
    
    except sql.OperationalError as e:
        pass
    

while True:
    print("====================================")
    print("1-Registrar el ingreso del estudiante al comedor")
    print("2-Agregar estudiante nuevo al sistema")
    print("3-Consultar sistema")
    
    print("====================================")
    print("4-Cerrar sistema")
    print("====================================")

    opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")

    if opcion == "1": # FUNCION PARA REGISTRAR EL ESTUDIANTE MEDIANTE LA INSERCION 
                        #DEL NUMERO DE CEDULA 

        
        while True:
            print("======================================")
            print("Control de ingreso al Comedor")
            print("======================================")
            print("Sistema para registrar al estudiante a la hora de ingreso al comedor")
            

            cedula = int(input("Ingrese la Cedula del estudiante: "))
            buscarDatos(cedula)
            opcion = input("Presione la letra S para salir al menu principal \nEnter para continuar...\n")
            opcion = opcion.upper()
        

            if opcion == "S":
                break

    elif opcion == "2": # FUNCION PARA AGREGAR A UN NUEVO ESTUDIANTE AL SISTEMA 
        while True: 
            print("======================================")
            print("Agregar nuevos estudiante al sistema")
            print("======================================\n")
            print("TOMAR EN CUENTA LO SIGUIENTE")
            print("-CEDULA EN NUMEROS ENTEROS SIN GUIONES,")
            print("\n-SECCION COMO ESTE EJEMPLO (10-1) ")
            print("\n-NOMBRE CON MAYÚSCULAS, MINÚSCULAS Y TILDES SI ESTE LO CONLLEVA")
            print("========================================")
            
            cedula = int(input("Ingrese la Cedula del estudiante: "))
            nombre = input("Ingrese el nombre y apellidos del estudiante: ")
            seccion = input("Ingrese la seccion del estudiante: ")

            insertardatos(cedula, nombre, seccion)

            opcionSalir = input("Presione la letra S para salir al menu principal \nEnter para continuar...\n")
            opcionSalir = opcionSalir.upper()
            if opcionSalir == "S":
                break

    elif opcion == "3": #FUNCION PARA HACER CONSULTAS A LA BASE DE DATOS 
        while True:
            print("======================================")
            print("Consulta en el sistema")
            print("======================================")
            print("1-CONSULTAR DATOS DEL ESTUDIANTE")
            print("2-CONSULTAR REGISTROS DEL INGRESO AL COMEDOR")
            
            opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
            
            if opcion == "1":
                consultaEstudiante()
            elif opcion == "2":
                consultaRegistro()
            
            opcionSalir = input("\nPresione la letra S para salir al menu principal \nEnter para continuar...\n")
            opcionSalir = opcionSalir.upper()
            if opcionSalir == "S":
                break
            
            
    


    elif opcion == "4":

        #FUNCION PARA CERRAR EL SISTEMA DE REGISTRO DEL COMEDOR
        break
    
                





        
               