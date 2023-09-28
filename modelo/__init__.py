class Cuenta:
    def __init__(self, numero_cuenta, documento_identidad, nombre, saldo):
        self._numero_cuenta = numero_cuenta
        self.documento_identidad = documento_identidad
        self.nombre = nombre
        self.saldo = saldo

    def depositarDinero(self, cantidad):
        retencion = cantidad * 0.19
        deposito_neto = cantidad - retencion
        self.saldo += deposito_neto

    def retirarDinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        else:
            return False

    def mostrarDatos(self):
        return f"Número de Cuenta: {self._numero_cuenta}, Documento de Identidad: {self.documento_identidad}, Nombre: {self.nombre}, Saldo Actual: {self.saldo}"

cuentaClientes = []
