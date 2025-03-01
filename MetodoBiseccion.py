import numpy as np  # Se importa NumPy para funciones matemáticas avanzadas.

def metodoBiseccion(f, a, b, tol=1e-6, max_iter=100):  
    """
    Método numérico de bisección para encontrar raíces de una función continua.

    Parámetros:
    f (función): Función matemática a evaluar.
    a (float): Límite inferior del intervalo.
    b (float): Límite superior del intervalo.
    tol (float, opcional): Tolerancia de error para detener el método. Valor por defecto 1e-6.
    max_iter (int, opcional): Número máximo de iteraciones permitidas. Valor por defecto 100.

    Retorna:
    float: Aproximación de la raíz de la función en el intervalo dado.
    """

    # Verifica que la función tenga signos opuestos en los extremos del intervalo.
    if f(a) * f(b) >= 0:  
        raise ValueError("El intervalo no cumple el criterio de cambio de signo.")  

    iteraciones = 0  # Contador de iteraciones

    while (b - a) / 2 > tol and iteraciones < max_iter:  
        c = (a + b) / 2  # Calcula el punto medio

        if f(c) == 0:  # Si f(c) es exactamente 0, se ha encontrado la raíz exacta.
            print("Valor encontrado.")
            return c  

        # Verifica si el signo de f(c) es el mismo que f(a) o f(b)
        if f(c) * f(a) <= 0:  
            b = c  # Se actualiza el límite superior
        else:  
            a = c  # Se actualiza el límite inferior

        iteraciones += 1  # Se incrementa el contador de iteraciones

    return (a + b) / 2  # Retorna la mejor aproximación de la raíz encontrada.

def miFuncion(x):
    """
    Función de ejemplo para aplicar el método de bisección.
    Puedes modificar esta función según sea necesario.
    """
    return x**3 + 4*x**2 - 10  

# Ejemplo de uso del método de bisección
raiz = metodoBiseccion(miFuncion, 1, 2)  
print(f"La raíz aproximada es: {raiz}")
