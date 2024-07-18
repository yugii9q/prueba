import random
import csv
import statistics


trabajadores = ["Juan Pérez",
                "María García",
                "Carlos López",
                "Ana Martínez",
                "Pedro Rodríguez",
                "Laura Hernández",
                "Miguel Sánchez",
                "Isabel Gómez",
                "Francisco Díaz",
                "Elena Fernández"]

sueldo_tra = []

sueldo_tra = {empleado:round(random.randrange(300000, 2500000),-5) for empleado in trabajadores}

def clasificar_sueldos():
    menores = {}
    medios = {}
    mayores = {}
    print("Sueldos menores a $800.000 TOTAL:", menores)
    print("Sueldos entre $800.000 y 2.000.000 TOTAL:", medios)
    print("Sueldos mayores a $2.000.000", mayores)


def ver_estadisticas():
    print("Sueldo mas alto: ",max(sueldo_tra),"$",max(list(sueldo_tra.values())))
    print("Sueldo mas bajo: ",min(sueldo_tra),"$",min(list(sueldo_tra.values())))
    print("Promedio de sueldos en pesos: $", round(sum(list(sueldo_tra.values())) / len(list(sueldo_tra.values()))))
    print("La media geometrica en pesos es: $", round(statistics.geometric_mean(list(sueldo_tra.values()))))

def reporte_sueldos():
    print("Nombre empleado" , " ","Sueldo base" , " "  ,"Descuento salud" , " " ,"Descuento afp" , " " ,"Sueldo líquido")
    with open('reporte_sueldos.csv','w',newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre empleado" , "Sueldo base" , "Descuento salud" ,"Descuento afp" , "Sueldo líquido "])

        for empleado, sueldo_bruto in sueldo_tra.items():
            fonasa = round(sueldo_bruto * 0.07)
            afp = round(sueldo_bruto * 0.12)
            sueldo_li = round(sueldo_bruto - fonasa - afp)

            escritor.writerow([empleado,sueldo_bruto,fonasa,afp,sueldo_li]) 

            print(empleado , sueldo_bruto , fonasa,afp , sueldo_li , sep= '  ')

    print("Copia csv lista.")

def exit_program():
    print("\nFinalizando programa...")
    print("Desarrollado por Sayen Sepulveda")
    print("Rut: 21727446-k")


def ejecutar_opcion(opcion):
 
    if opcion == '1':
        print("Sueldos Asignados:")
        print(sueldo_tra)
 
    elif opcion == '2':
        clasificar_sueldos()
 
    elif opcion == '3':
        ver_estadisticas()
 
    elif opcion == '4':
        reporte_sueldos()
 
    elif opcion == '5':
        exit_program()
        menu == False
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 6.")
menu = True 
while menu == True :
    print("\nMenú")
    print("1.Asignar sueldos")
    print("2.Clasificacion de sueldos")
    print("3.Ver estadisticas")
    print("4.Reporte de sueldos")
    print("5.Salir")

    opcion = input("¿Qué operación desea realizar?: ")
    ejecutar_opcion(opcion)

