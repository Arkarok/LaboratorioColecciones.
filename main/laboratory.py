import statistics
from custom_functions import temperature_methods

print("Bienvenido al Observatorio Nacional de Meteorologia (ONM)")
guajira=[31,34,35,34,33,33,32,34,32,35,36,33]
narigno=[19,22,20,18,21,23,21,19,22,17,22,21]
santander=[30,28,27,28,27,29,30,28,31,26,29,28]
print("Punto A")
prom_1=temperature_methods.promedio_temperature(guajira)
prom_2=temperature_methods.promedio_temperature(narigno)
prom_3=temperature_methods.promedio_temperature(santander)
print("El promedio de las temperaturas en el departamento de la guajira es de: ",prom_1)
print("El promedio de las temperaturas en el departamento de narigno es de: ",prom_2)
print("El promedio de las temperaturas en el departamento de santander es de: ",prom_3)
print("Punto B")
nacional=[31,34,35,34,33,33,32,34,32,35,36,33,19,22,20,18,21,22,21,19,22,17,22,21,30,28,27,28,27,29,30,28,31,26,29,28]
prom_nacional=temperature_methods.promedio_temperature(nacional)
print("El promedio de temperatura en los tres departamentos fue de: ",prom_nacional)
print("Punto C")
mess=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
cal_1=temperature_methods.temperature_best(guajira)
cal_2=temperature_methods.temperature_best(narigno)
cal_3=temperature_methods.temperature_best(santander)
mes_1=guajira.index(cal_1)
mes_2=narigno.index(cal_2)
mes_3=santander.index(cal_3)
print("El mes mas caliente en la guajira fue de ",mess[mes_1]," con un valor de: ",cal_1)
print("El mes mas caliente en narigno fue de ",mess[mes_2]," con un valor de: ",cal_2)
print("El mes mas caliente en santander fue de ",mess[mes_3]," con un valor de: ",cal_3)
print("Punto D")
cal_T=[cal_1,cal_2,cal_3]
prom_cal=temperature_methods.promedio_temperature(cal_T)
print("El promedio de la temperatura en el mes mas caliente de los tres departamentos fue: ",prom_cal)
print("Punto E")
prom_T=[prom_1,prom_2,prom_3]
t_prom=temperature_methods.temperature_best(prom_T)
print("El promedio mas caliente en los tres departamentos fue de: ",t_prom)
print("Punto F")
d={0:"enero",1:"febrero",2:"marzo",3:"abril",4:"mayo",5:"junio",6:"julio",7:"agosto",8:"septiembre",9:"octubre",10:"noviembre",11:"diciembre",12:"enero",13:"febrero",14:"marzo",15:"abril",16:"mayo",17:"junio",18:"julio",19:"agosto",20:"septiembre",21:"octubre",22:"noviembre",23:"diciembre",24:"enero",25:"febrero",26:"marzo",27:"abril",28:"mayo",29:"junio",30:"julio",31:"agosto",32:"septiembre",33:"octubre",34:"noviembre",35:"diciembre"}
mayord=temperature_methods.temperature_best(cal_T)
depa=["guajira","narigno","santander"]
posi=cal_T.index(mayord)
mes_f=nacional.index(mayord)
print("La temperatura mas caliente en todo el agno fue de ",mayord," encontrada en el departamendo de ",depa[posi]," en el mes de ",d[mes_f])
print("Punto G")
s1=statistics.stdev(guajira)
s2=statistics.stdev(narigno)
s3=statistics.stdev(santander)
print("La desviacion estandar en la temperatura de la guajira fue de: ",s1)
print("La desviacion estandar en la temperatura de narigno fue de: ",s2)
print("La desviacion estandar en la temperatura de santander fue de: ",s3)
