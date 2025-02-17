from math import ceil, floor

def gaussian_division_candidates(a, b):
    """
    Dado a y b (enteros gaussianos), calcula a/b en el campo complejo y
    retorna una lista de candidatos q = x + yi, con x, y enteros, tales que:
    |Re(a/b) - x| <= 0.5  y  |Im(a/b) - y| <= 0.5.\n
    Podriamos usar un simple round para reducir calculos, pero me gusta mas asi, se puede apreciar mejor 
    el proceso que se hace en el algoritmo.
    """
    q = a / b
    A, B = q.real, q.imag
    candidates = []
    for x in [floor(A), ceil(A)]:
        for y in [floor(B), ceil(B)]:
            if abs(A - x) <= 0.5 and abs(B - y) <= 0.5:
                candidates.append(complex(x, y))
    return candidates

def gaussian_division(a, b):
    """
    Realiza la división euclidiana óptima de enteros gaussianos,
    retornando el cociente q que minimiza el residuo |a - b*q|.
    """
    candidates = gaussian_division_candidates(a, b)
    return min(candidates, key=lambda candidate: abs(a - candidate * b))

def generate_variants(g):
    """
    Genera las variantes de un candidato MCD multiplicándolo por las unidades:
    1, -1, i, -i.\n
    Asi evitamos hacer lo mismo por cada candidato encontrado y podemos trabajar con el que nos parezca más comodo.
    """
    units = [1, -1, 1j, -1j]
    return [g * u for u in units]

def gaussian_gcd(a, b, with_variants=False, verbose=False):
    """
    Calcula el MCD de enteros gaussianos usando el algoritmo de Euclides optimizado.
    
    En cada paso se elige el cociente q (entre los candidatos) que minimiza el residuo:
        r = a - (b * q).
    
    Parámetros:
    - a, b: enteros gaussianos.
    - with_variants: si es True, retorna una lista con las variantes del MCD.
    - verbose: si es True, imprime los pasos del algoritmo.
    
    Retorna:
    - Si with_variants es True: lista con las variantes del MCD.
    - En otro caso: el MCD canónico.
    """
    steps = []  # Guardar los pasos del algoritmo para un procedimiento más claro
    steps.append(f"Iniciando cálculo del MCD de {a} y {b}")
    while b != 0:
        q = gaussian_division(a, b)
        r = a - q * b
        steps.append(f"{a} = ({q}) * {b} + {r}")
        a, b = b, r
    
    steps.append("Proceso completo:")
    steps.append(f"MCD encontrado: {a}")
    
    if verbose:
        for step in steps:
            print(step)
    
    if with_variants:
        return generate_variants(a), steps  # Si se piden variantes, devuelve ambas cosas
    else:
        return a, steps  # Si no se piden variantes, solo el MCD y los pasos

def use_example():
    # Ejemplo de uso
    a = complex(11, 3)
    b = complex(1, 8)

    print("Cálculo detallado con variantes:")
    result_variants, steps1 = gaussian_gcd(a, b, with_variants=True, verbose=True)
    print(f"\nMCD({a}, {b}) variantes: {result_variants}")

    print("\nCálculo rápido (MCD canónico):")
    result_canonical, steps2 = gaussian_gcd(a, b, with_variants=False, verbose=True)
    print(f"\nMCD({a}, {b}) = {result_canonical}")

if __name__ == "__main__":
    use_example()