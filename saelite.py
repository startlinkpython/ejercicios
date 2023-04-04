print("Calcula la distancia de un satélite artificial ")
print("respecto a la Tierra según tarda en llegar su señal")
print("dato c y UA")
c=float(input("vel. luz c[m/s]: "))
UAm=float(input("valor UA[m]: "))
print("Introducir el dato (separar horas, minutos y segundos")
print()

#introducir tiempo en horas
th=int(input("horas th= "))

#introducir tiempo en minutos
tm=int(input("minutos tm= "))

#introducir tiempo en segundos
ts=int(input("segundos ts= "))

#pasar los tiempos a segundos
ths=th*3600
tms=tm*60

#tiempo total en [s]
tt=ths+tms+ts
dm=c*tt
print("distancia [km]= ", dm/1000)

#cálculo de la distancia en UA
dUA=dm/UAm
print("distancia [UA]= ", dUA)
print()
