import os
vecUser=["User1", "User2", "User3"]
vecClaves=["123", "Boca", "River"]
vecSaldos=[10000, 20000, 30000]
vecResumen=[]
fin= False
saldo=0
msj= ""
opcion=0

while (fin== False):
    print("Ingresar usuario: ") #Ingreso de datos
    usuario= input("")
    print("Ingresar clave: ")
    clave= input("")
    
    for i in range(0, len(vecUser)): #Verificación. Se recorre con el for
        if(usuario== vecUser[i] and clave== vecClaves[i]):
            fin= True
            saldo= vecSaldos[i]
            indice= i
    if (fin== False):
        print("Usuario incorrecto")

#cuando fin= True
print("Bienvenido al sistema")
fin= False
while(fin== False): #Ahora comenzamos con las tareas que puede hacer el usuario
    car= input("Presione una tecla para continuar")
    os.system("cls")
    msj= "1. Extracción 2.Depósito. 3.Consultar Saldo, 4. Resumen 10.Salir"
    print(msj)
    opcion=int(input(""))
    if (opcion== 10):
        fin= True
    if (opcion==3):
        msj= "Su saldo es "+ str(saldo)
        print(msj)
    if (opcion==2):
        print("Ingresar monto a depositar: ")
        monto= int(input(""))
        saldo= saldo+ monto
        vecSaldos[indice]= saldo
        msj="Depósito "+ str(monto)
        vecResumen.append(msj)
    if (opcion==1):
        print("Ingresar monto a extraer: ")
        monto= int(input(""))
        if (monto <= saldo):
            saldo=saldo- monto
            msj="Extracción: "+ str(monto)
            vecSaldos[indice]= saldo
            print(msj)
            vecResumen.append(msj)
        else: 
            msj="No puede superar el monto de " + str(saldo)
            print(msj)
    if (opcion==4):
        for i in range(0, len(vecResumen)):
            print(vecResumen[i])