from .gaussian_gcd import gaussian_division

def recursive_process(a, b, add_step):
    """
    Implementa el algoritmo de Euclides extendido para los enteros gaussianos.
    
    Parámetros:
    - a, b: Números complejos representando enteros gaussianos.
    - add_step: Función para registrar los pasos de ejecución.
    
    Retorna:
    - (g, u, v): Donde g es el máximo común divisor de (a, b),
    y (u, v) son los coeficientes de Bézout tales que g = a*u + b*v.
    """
    if b == 0:
        add_step(f"Base: gcd({a}, {b}) = {a}")
        return a, 1, 0

    q = gaussian_division(a, b)
    r = a - q * b
    
    add_step(f"{a} = ({q}) * {b} + {r}")
    
    g, u1, v1 = recursive_process(b, r, add_step)
    u = v1
    v = u1 - q * v1
    return g, u, v

def extended_gaussian_gcd(a, b, verbose=False):
    """
    Algoritmo de Euclides extendido para enteros gaussianos.
    
    Retorna:
        (g, u, v, steps)
    
    Donde:
    - g = gcd(a, b)
    - u, v son los coeficientes de Bézout: g = a*u + b*v
    - steps es una lista de los pasos de ejecución del algoritmo.
    
    Parámetros:
    - a, b: enteros gaussianos.
    - verbose: si True, imprime los pasos del algoritmo.
    """
    steps = ["Iniciando cálculo..."]
    
    # Ejecutar la recursión con seguimiento de pasos
    g, u, v = recursive_process(a, b, lambda step: steps.append(step))
    # Agregar información final
    steps.append("Resultado:")
    steps.append(f"gcd({a}, {b}) = {g}")
    steps.append(f"Coeficientes: u = {u}, v = {v}")
    steps.extend(verify_gcd(a, u, b, v, g))

    if verbose:
        for step in steps:
            print(step)
    
    return g, u, v, steps

def verify_gcd(a, u, b, v, g):
    """
    Verifica paso a paso que g = a*u + b*v.
    """
    steps = []
    steps.append("Verificación:")
    steps.append(f"{a}*{u} + {b}*{v} = {a*u} + {b*v}")
    resultado = a*u + b*v
    steps.append(f"{a}*{u} + {b}*{v} = {resultado}")
    if resultado == g:
        steps.append("El resultado es Correcto!")
    else:
        steps.append("Algo salió mal :(")
    return steps

def use_example():
    # Ejemplo de uso
    a = complex(6, 9)
    b = complex(5, 1)

    print("Algoritmo de Euclides extendido para enteros gaussianos:\n")
    extended_gaussian_gcd(a, b, verbose=True)

if __name__ == "__main__":
    use_example()