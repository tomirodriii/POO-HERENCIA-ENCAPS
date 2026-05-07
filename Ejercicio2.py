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

