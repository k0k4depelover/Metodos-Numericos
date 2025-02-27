def metodoBiseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b)>=0:
        raise ValueError ("El intervalo no cumple el cambio de signo") 
    
    tier=0
    while(b-a)/2 > tol and tier <max_iter:
        c=(a+b)/2
        if(f(c)==0):
            print("Valor encontrado")
        if f(c)*f(a)  <=0:
            b=c
        else:
            a=c
        iter=+1
    return (a + b) / 2

def miFuncion(x):
    return x**3+4*x**2-10

raiz=metodoBiseccion(miFuncion,1,2)
print(f"La raíz aproximada es: {raiz}")