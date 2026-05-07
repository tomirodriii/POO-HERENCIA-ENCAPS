# EJERCICIO 2: CUENTA BANCARIA 
# Objetivo: Practicar encapsulamiento y herencia.
# Clases a implementar:
#    1. Clase base: CuentaBancaria
#           Atributos encapsulados: _saldo, _titular
#           Métodos:
#                __init__(titular, saldo_inicial)
#                depositar(monto)
#                retirar(monto)
#                get_saldo()
#   2. Clase hija: CuentaAhorro (hereda de CuentaBancaria)
#           Atributo encapsulado: _tasa_interes
#           Métodos:
#                __init__(titular, saldo_inicial, tasa_interes)
#                aplicar_interes()

import os 
os.system("cls")

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo = saldo_inicial
        
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"{self._titular} depositó {monto}. Nuevo saldo: {self._saldo}")
        else:
            print("Monto de depósito debe ser positivo.")
            
    def retirar(self, monto):
        if monto > 0:
            if monto <= self._saldo:
                self._saldo -= monto
                print(f"{self._titular} retiró {monto}. Nuevo saldo: {self._saldo}")
            else:
                print("Fondos insuficientes para retirar.")
        else:
            print("Monto de retiro debe ser positivo.")
            
    def get_saldo(self):
        return self._saldo
    
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular, saldo_inicial)
        self._tasa_interes = tasa_interes
        
    def aplicar_interes(self):
        interes = self._saldo * self._tasa_interes
        self._saldo += interes
        print(f"Interés aplicado a {self._titular}. Interés: {interes}. Nuevo saldo: {self._saldo}")
        
# Crear instancia de CuentaAhorro
cuenta_ahorro = CuentaAhorro("Juan Pérez", 1000, 0.05)
# Mostrar saldo inicial
print(f"Saldo inicial de {cuenta_ahorro._titular}: {cuenta_ahorro.get_saldo()}")
# Realizar operaciones
cuenta_ahorro.depositar(500)
cuenta_ahorro.retirar(200)
cuenta_ahorro.aplicar_interes()

