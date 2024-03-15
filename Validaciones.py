def validarNombre (nombre: str) -> bool:
    """Funcion para validar nombres/apellidos de usuarios, simple o compuestos"""
    nombres = nombre.split()
    for n in nombres:
        if not n.isalpha():
            return False
    return True

def validarDNI (dni: int) -> bool:
    """Funcion para validar DNI"""
    if dni.isdigit():
        dni=int(dni)
        if dni > 3000000 and dni < 99999999:
            return True
    return False

def validarMail (mail: str) -> bool:
    mail_Inv = True
    arroba = False
    punto = False
    mails= mail
    while mail_Inv:
        for caracter in mails:
            if caracter == '@':
                arroba=True
            elif caracter =="." and arroba == True:
                punto= True
            elif punto== True and arroba== True:
                return True
        if mail_Inv == True:
                return False

                      