import math


def is_prime_integer(n):
    """
    Verifica si un entero n es primo.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_gaussian_prime(z):
    """
    Determina si el entero gaussiano z es primo en Z[i].

    Un entero gaussiano a+bi se considera primo si:
    - No es una unidad (es decir, su norma a^2+b^2 no es 1).
    - Si a y b son ambos distintos de 0, z es primo si y solo si
        su norma (a^2+b^2) es un número primo en Z.
    - Si uno de a o b es 0 (es decir, z es puramente real o imaginario),
        z es primo si y solo si |a| (o |b|) es primo en Z y además es congruente a 3 mod 4.
    """
    # Extraer partes real e imaginaria (aseguramos que sean enteras)
    a = int(z.real)
    b = int(z.imag)
    
    # El cero no es primo
    if a == 0 and b == 0:
        return False
    
    # Verificar unidades: 1, -1, i, -i tienen norma 1
    if a*a + b*b == 1:
        return False

    # Si ambas partes son no nulas, usamos la norma
    if a != 0 and b != 0:
        norm = a*a + b*b
        return is_prime_integer(norm)
    else:
        # Caso en que z es puramente real o puramente imaginario
        p = abs(a) if a != 0 else abs(b)
        return is_prime_integer(p) and (p % 4 == 3)


if __name__ == "__main__":
    # Ejemplos de uso
    test_numbers = [
        complex(3, 0),   # 3 es primo en Z[i] porque 3 mod 4 == 3.
        complex(2, 0),   # 2 no es primo en Z[i] (2 = (1+i)(1-i)).
        complex(1, 1),   # 1+i es primo porque norm = 2 (primo en Z).
        complex(2, 1),   # 2+i es primo (norm = 5, primo en Z).
        complex(3, 2),   # 3+2i es primo (norm = 13).
        complex(4, 1),   # 4+1i es primo (norm = 17).
        complex(5, 0),   # 5 no es primo en Z[i] (5 mod 4 == 1, se descompone).
        complex(0, 7),   # 7i es primo porque 7 mod 4 == 3.
        complex(0, 5),   # 5i no es primo porque 5 mod 4 == 1.
        complex(0, -3),  # -3i es primo, ya que | -3 | = 3 y 3 mod 4 == 3.
    ]

    for z in test_numbers:
        result = "primo" if is_gaussian_prime(z) else "no primo"
        print(f"{z} es {result}")