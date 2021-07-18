from cryptography.fernet import Fernet
from pathlib import Path

def leerArchivo(archivo):
    stream=open(archivo,"rb")
    print(stream.read())

def escribirArchivo(linea,archivo):
    with open(archivo,'a') as file: #argumento "a" es igual a append de agregar
        file.write("\n"+linea)

def generarClave():
    archivo=r'key.key'
    objetoArchivo=Path(archivo)
    if not objetoArchivo.is_file():
        clave=Fernet.generate_key()

        with open("key.key","wb") as key_file:
            key_file.write(clave)

def cargarClave():
    return open("key.key","rb").read()

def encriptar(archivo,clave):
    f=Fernet(clave)
    with open(archivo,"rb") as file:
        file_data=file.read()

    #Se encriptan los datos del archivo
    datos_encriptados=f.encrypt(file_data)

    with open(archivo,"wb") as file:
        file.write(datos_encriptados)

def desencriptar(archivo,clave):
    f=Fernet(clave)
    with open(archivo,"rb") as file:
        datos_encriptados=file.read()

    #se desencriptan los datos
    datos=f.decrypt(datos_encriptados)

    with open(archivo,"wb") as file:
        file.write(datos)


    