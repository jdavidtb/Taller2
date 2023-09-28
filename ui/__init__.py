from modelo import Cuenta, cuentaClientes

def menu():
    print("1. Crear Cuenta")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Mostrar Datos de Cuenta")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def ui():
    while True:
        opcion = menu()
        if opcion == 1:
            numero_cuenta = int(input("Ingrese el número de cuenta: "))
            documento_identidad = int(input("Ingrese el documento de identidad: "))
            nombre = input("Ingrese el nombre del cliente: ")
            saldo = float(input("Ingrese el saldo inicial: "))
            cuenta = Cuenta(numero_cuenta, documento_identidad, nombre, saldo)
            cuentaClientes.append(cuenta)
            print("Cuenta creada exitosamente!")
        elif opcion == 2:
            numero_cuenta = int(input("Ingrese el número de cuenta: "))
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            for cuenta in cuentaClientes:
                if cuenta._numero_cuenta == numero_cuenta:
                    cuenta.depositarDinero(cantidad)
                    print("Depósito realizado!")
                    break
            else:
                print("Cuenta no encontrada!")
        elif opcion == 3:
            numero_cuenta = int(input("Ingrese el número de cuenta: "))
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            for cuenta in cuentaClientes:
                if cuenta._numero_cuenta == numero_cuenta:
                    if cuenta.retirarDinero(cantidad):
                        print("Retiro realizado!")
                    else:
                        print("Saldo insuficiente!")
                    break
            else:
                print("Cuenta no encontrada!")
        elif opcion == 4:
            numero_cuenta = int(input("Ingrese el número de cuenta: "))
            for cuenta in cuentaClientes:
                if cuenta._numero_cuenta == numero_cuenta:
                    print(cuenta.mostrarDatos())
                    break
            else:
                print("Cuenta no encontrada!")
        elif opcion == 5:
            print("Adiós!")
            break
