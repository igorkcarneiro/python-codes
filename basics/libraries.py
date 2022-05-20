import datetime
now = datetime.datetime.now()
print ("Data e hora atual: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

from math import pi
r = float(input ("Digite o raio do círculo: "))
print ("A área do círculo de raio " + str(r) + " é: " + str(pi * r**2))

import sys
print("Versão do Python:")
print (sys.version)

import calendar
a = int(input("Digite o ano: "))
m = int(input("Digite o mês: "))
print(calendar.month(a, m))

import math
p1 = [4, 0]
p2 = [6, 6]
dist = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
print("Calculo de distância entre dois pontos: ")
print(dist)