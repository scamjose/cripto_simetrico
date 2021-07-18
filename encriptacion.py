import archivos

opcion=0
archivo="foto.jpeg"
archivos.generarClave()
clave=archivos.cargarClave()


while opcion !=5:
    print("\nSeleccione una opción\n")
    print("1.-Leer Archivo\n2.-Agregar texto al archivo\n3.-Encriptar\n4.-Desencriptar\n5.-Salir")
    opcion=int(input("Ingresa una opción: "))

    if opcion==1:
        print("El contenido del archivo es: ")
        archivos.leerArchivo(archivo)
    elif opcion==2:
        linea=input("Introduce el texto que desea agregar al archivo: ")
        archivos.escribirArchivo(linea,archivo)
    elif opcion==3:
        print("Encriptando archivo...")
        archivos.encriptar(archivo,clave)
        print("Archivo encriptado")
    elif opcion==4:
        print("Desencriptando archivo...")
        archivos.desencriptar(archivo,clave)
        print("Archivo desencriptado")
    elif opcion==5:
        exit()
    else:
        print("\nOpción incorrecta")