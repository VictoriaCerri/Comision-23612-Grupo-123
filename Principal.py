import os
workdir = os.path.dirname(__file__)
os.chdir(workdir)

import Funciones as Fn
import Validaciones as Vl

archivoDato= 'datos.txt'
matriz= Fn.CargarMatriz(archivoDato)
campos=matriz[0]



while True:
    matriz= Fn.CargarMatriz(archivoDato)
    Fn.limpiar()
    Fn.decorar()
    print("\nMenú:\n [1] Buscar usuario por DNI \n [2] Listar todos los registros \n [3] Agregar un registro \n [4] Modificar un registro \n [5] Eliminar un registro \n [6] Salir" )
    opcion= input(f'\n seleccione una opción y presione ENTER  ')
    if opcion == "1":
        try:
            dniBuscar = input("Ingrese el DNI a buscar: ")
            registro = Fn.buscarRegistro(dniBuscar,matriz)  
            Fn.imprimeUsuario(campos, registro)
        except ValueError:
            input(f'El DNI: {dniBuscar} no existe. ')
            
    
    elif opcion == "2": 
        Fn.imprimirUsuarios(matriz)
        input("Presione ENTER para continuar...")

    elif opcion== "3":
        matriz.append(Fn.agregarUsuario())
        Fn.CargarTXT(archivoDato,matriz)
        input("Registro agregado exitosamanete, presione ENTER para continuar...")     
    elif opcion == "4":       
        try:
            print()
            dniBuscar = input("Ingrese el DNI a buscar: ")
            registro = Fn.buscarRegistro(dniBuscar,matriz)
            print()
            Fn.imprimeUsuario(campos,registro)
            print()
            indice = Fn.buscarIndice(dniBuscar,matriz)  
            matriz[indice]= Fn.modificarUsuario()
            Fn.CargarTXT(archivoDato,matriz)
            input("Registro modificado exitosamente, presione ENTER para continuar...") 
        except ValueError:
            input(f'El DNI: {dniBuscar} no existe. ')    
        
    elif opcion == "5": 
        dni= Fn.leeDni()
        try:
            matriz.remove(Fn.eliminarUsuario(dni,matriz))
            Fn.CargarTXT(archivoDato,matriz) 
            print('Registro eliminado exitosamente...')
            input('Presione enter para continuar') 
        except:
            print('El dni no existe, intente nuevamente...')
        
    elif opcion == "6": 
        print("Muchas gracias por usar el sistema...")
        break
    else:
        input('\n' 'Ingrese un número entre el 1 y el 6' '\n')

