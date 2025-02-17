from gaussian_gcd import gaussian_division

def extended_gaussian_gcd(a, b, verbose=False):
    """
    Algoritmo de Euclides extendido para enteros gaussianos.
    
    Retorna una tupla (g, u, v) tal que:
        g = gcd(a, b)  y  g = a*u + b*v.
    
    Parámetros:
    - a, b: enteros gaussianos.
    - verbose: si True, imprime los pasos del algoritmo.
    """
    if b == 0:
        if verbose:
            print(f"Base: gcd({a}, {b}) = {a}")
        return a, 1, 0

    q = gaussian_division(a, b)
    r = a - q * b
    if verbose:
        print(f"{a} = ({q}) * {b} + {r}")
    
    g, u1, v1 = extended_gaussian_gcd(b, r, verbose)
    # Se tiene: r = a - q*b, y: g = b*u1 + r*v1 = a*v1 + b*(u1 - q*v1)
    u = v1
    v = u1 - q * v1
    return g, u, v

def verify_gcd(a, u, b, v, g):
    """
    Verifica paso a paso que g = a*u + b*v.
    """
    print("Verificación:")
    print(f"{a}*{u} + {b}*{v} = {a*u} + {b*v}")
    resultado = a*u + b*v
    print(f"{a}*{u} + {b}*{v} = {resultado}")
    if resultado == g:
        print("El resultado es Correcto!")
    else:
        print("Algo salió mal :(")

if __name__ == "__main__":
    # Ejemplo de uso
    a = complex(11, 3)
    b = complex(1, 8)

    print("Algoritmo de Euclides extendido para enteros gaussianos:\n")
    g, u, v = extended_gaussian_gcd(a, b, verbose=True)
    print("\nResultado:")
    print(f"gcd({a}, {b}) = {g}")
    print(f"Coeficientes: u = {u},  v = {v}")
    verify_gcd(a, u, b, v, g)