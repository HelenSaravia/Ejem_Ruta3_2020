# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:27:56 2020

@author: Docente Superate
"""
a = "Hello World"
b = 20
c = 20.5
d = True
e = ["apple", "banana", "cherry"]
f = ("apple", "banana", "cherry")
g = {"apple", "banana", "cherry"}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

#tambien podemos crear variables con un tipo especifico
h= int(2.5)
j=float(3)
k=str("en hora buena!")
m= str("iniciamos a programar")


print(h)
#si usamos el simbolo + con numeros se hace una operacion
print(h+j)

#si usamo el simbolo + con textos los une
print(k+ m)

#esto nos daria un error, 
# print(k+j)