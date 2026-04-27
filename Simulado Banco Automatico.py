# =========================================================
# PROYECTO: SECUREBANK ATM - SISTEMA DE GESTIÓN BANCARIA
# =========================================================
# DESCRIPCIÓN: 
# Simulador de cajero con validación de seguridad (PIN) e 
# integridad de transacciones (control de saldo).
#
# LO QUE APRENDÍ:
# 1. Validación de Saldo: Implementé un control para que el usuario
#    no pueda retirar más dinero del disponible.
# 2. Corrección de f-strings: Solucioné el error de visualización 
#    añadiendo la 'f' antes de las comillas para mostrar variables.
# 3. Estructura de Menú: Uso de un bucle while infinito controlado 
#    por una opción de salida.
#
# DESAFÍOS: 
# Lo más difícil fue conectar la lógica de bloqueo de intentos 
# con el menú principal del cajero sin que se reiniciara el saldo.
# =========================================================

saldo = 1000.0
intentos = 3
clave = "1234"
acceso = True
while intentos > 0:
    intento=input("introduce la clave: ")
    if intento==clave:
        acceso = True
        print("Bienvenido")
        break
    else:
        intentos = intentos -1
        
        if intentos == 2:
            print ("te quedan 2 intentos ")
        elif intentos==1:
            print ("te queda 1 intento ")
    if intentos == 0:
        print("aplicacion bloqueada")
        break

if acceso == True:
    while True: 
            print (f"Tu saldo es de: {saldo}")
            print("1. Ingresar dinero")
            print("2. Retirar dinero")
            print("3. Salir")
            opcion = input ("elige una opcion: ")
            if opcion == "1":
                ingreso = float(input("¿cuanto dinero quieres ingresar?: "))
                saldo = saldo + ingreso
                print(f"Ingreso realizado. Tu saldo actual es: {saldo}")

            elif opcion == "2":
                retiro = float(input("¿cuanto dinero quieres retirar?: "))
        
                if retiro <= saldo:
                    saldo = saldo - retiro
                    print(f"Retiro realizado. Tu saldo actual es: {saldo}")
        
                elif retiro <= saldo:
                
                    print("ERROR: Saldo insuficiente.")


            elif opcion == "3":
                print("Cerrando sesion...")
                break
    

