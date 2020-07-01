# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:06:33 2020

@author: Docente Superate
"""
"""
Ejemplo de variables y operadores
Calule el monto neto de un credito, donde se tiene por monto bruto $5,000
a una tasa de interes del 12% y con una bonificacion del 5%, debe calcular
el monto del interes, el importe de la bonificacion y el monto neto del credito
"""
monto_bruto = 5000
tasa_interes = 12
tasa_bonificacion = 5

monto_interes = (monto_bruto * tasa_interes)/ 100

importe_bonificacion = (monto_bruto * tasa_bonificacion )/ 100

monto_neto = (monto_bruto - importe_bonificacion) + monto_interes

print("El monto neto es $", monto_neto)
print( "El interes generado es $", monto_interes)
print("La bonificacion es $", importe_bonificacion)