#import numpy as np   <= Puedes quitar el comentario a esta linea.


def metodoBiseccion(f, a, b, tol=1e-6, max_iter=100): #Se definen las variables de entrada, la funcion a analizar y el intervalo 
    #Se verifica que los valores en los puntos sean opuestos.
    if f(a) * f(b)>=0: #
        raise ValueError ("El intervalo no cumple el cambio de signo") #Caso contrario se cierra el programa
        
    
    tier=0 #Empezamos a contar la iteraciones
    while(b-a)/2 > tol and tier <max_iter: #Mientras no alcancemos las iteraciones, o el valor objetivo
        c=(a+b)/2 #Establecemos C como el punto medio
        if(f(c)==0): #Si es el valor que estabamos buscando terminamos el programa
            print("Valor encontrado")
        if f(c)*f(a)  <=0: #Si C cumple la condicion con a se cambia b por c
            b=c
        else: #Si no se cambia a por c
            a=c
        iter=+1 #Se actualiza el contador
    return (a + b) / 2 #Retornamos el valor iterado 

def miFuncion(x):
    return x**3+4*x**2-10 #Aca puedes cambiar y poner la funcion que quieras

    #Si quieres agregar funciones más complejas utiliza la libreria NUMPY

#Demostracion de uso
raiz=metodoBiseccion(miFuncion,1,2) 
print(f"La raíz aproximada es: {raiz}")