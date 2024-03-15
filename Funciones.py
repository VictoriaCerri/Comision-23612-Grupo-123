import os
os.chdir(os.path.dirname(__file__))
import Validaciones as Vl

def CargarMatriz (archivo: str) -> list:
    with open(archivo) as file:
        stream = file.read() # Accedo al contenido, nos devuelve un string
    listaRegistros = stream.split('\n')
    matriz = []
    for registro in listaRegistros:
        matriz.append(registro.split(','))
    return matriz

def CargarTXT (archivo: str, matriz: list) -> None:
    stream = ''
    for fila in matriz:
        stream += ','.join(fila)  + '\n'
    stream = stream.removesuffix('\n')
    with open(archivo,'w') as file:
        file.write(stream)
        
def limpiar():
    """
    Limpia la pantalla de la terminal
    """
    if os.name == 'nt':
        os.system('cls') # Para Windows
    else:
        os.system('clear') # Para Linux
    return 

def decorar():
    print("*"*10)
    print("*"*5,"crud de usuarios","*"*5)
    print("*"*10)


def leeNombre(dato: str) -> str:
    """
    Función para ingresar nombre y que me permita validar que sea solo letras y espacios
    """
    while True:
        entrada = input(f'Ingrese su {dato}: ')
        if Vl.validarNombre(entrada):
            return entrada
        else:
            print(f'El {dato} es incorrecto, inténtelo nuevamente...')

def leerMail():
    while True:
        entrada= input('Ingrese su mail: ')
        if Vl.validarMail(entrada):
            return entrada
        else:
            print('El mail ingresado es incorrecto, inténtelo nuevamente...')
        
def leeDni() -> bool:
    """
    Valida que el dato ingresado sea entero
    """
    while True:
        entrada = input(f'Ingrese su dni: ')
        if Vl.validarDNI(entrada):
            return entrada
        else:
            print('El DNI es incorrecto, inténtelo nuevamente...')

def agregarUsuario():
    dni=leeDni()
    apellido=leeNombre('apellido')
    nombre= leeNombre('nombre')
    mail=leerMail()
    return[dni,apellido,nombre,mail]

def buscarRegistro (datoAbuscar: str, matriz: list) -> list:
    for registro in matriz:
        if datoAbuscar in registro:
            return registro
    raise ValueError(f'El usuario con DNI {datoAbuscar} no existe') 

def imprimeUsuario(campos:list, registro: list) -> None:
    for campo, dato in zip (campos, registro):
        print(f'{campo} -> {dato}')
    input(f'Presione Enter para continuar...')
def imprimirUsuarios(registros:list) -> None:
    for i in registros:
        acumulador=""
        for j in i:
            if ','.join(j) != ",":
                acumulador+=j + ' | '                
        print(acumulador)   
        
def buscarIndice (datoAbuscar: str, matriz: list) -> list:
    indice=0
    for registro in matriz:
        if datoAbuscar in registro:
            return indice
        indice+=1
    raise ValueError(f'El usuario con DNI {datoAbuscar} no existe')            

def modificarUsuario():
    dni=leeDni()
    apellido=leeNombre('apellido')
    nombre=leeNombre('nombre')
    mail=leerMail()
    return [f'{dni}, {apellido}, {nombre}, {mail}']
    

def eliminarUsuario(datoAbuscar:str, matriz: list)->list:
   for registro in matriz:
       if datoAbuscar in registro:
          return registro
   raise ValueError(f'El usuario con DNI {datoAbuscar} no existe')




