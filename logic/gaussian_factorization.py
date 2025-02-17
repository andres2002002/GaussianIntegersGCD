import math
from sympy import factorint
# Puedes definir o importar is_gaussian_prime si lo requieres para otras funciones

def is_unit(z):
    """Determina si z es una unidad en Z[i]."""
    return (int(z.real)**2 + int(z.imag)**2) == 1

def divide_exact(z, w):
    """Divide z por w (se asume que w divide a z exactamente) y retorna el resultado."""
    c, d = int(w.real), int(w.imag)
    Nw = c*c + d*d
    z_conj_mult = z * complex(c, -d)
    q_real = round(z_conj_mult.real / Nw)
    q_imag = round(z_conj_mult.imag / Nw)
    return complex(q_real, q_imag)

def divides(z, w):
    """
    Verifica si w divide exactamente a z en Z[i].
    Se usa: q = (z * conjugado(w)) / N(w), y si q es gaussiano y z == w * q, entonces w divide a z.
    """
    if w == 0:
        return False
    q = divide_exact(z, w)
    return z == w * q

def sum_of_two_squares(p):
    """
    Para un primo entero p ≡ 1 mod 4, encuentra (a, b) enteros positivos tales que a^2+b^2 = p.
    Se busca de forma sencilla hasta int(sqrt(p)), es algo a lo bruto :(.
    """
    for a in range(1, int(math.sqrt(p)) + 1):
        b2 = p - a*a
        b = math.isqrt(b2)
        if b*b == b2: # si se da la condicion indica que p = a^2 + b^2
            return a, b
    return None

def are_associates(z1, z2):
    """
    Verifica si dos enteros gaussianos son asociados (difieren por una unidad).
    Retorna una unidad tal que:
        z2 * u == z1
    """
    unidades = [1, -1, 1j, -1j]
    for u in unidades:
        if z1 == z2 * u:
            return True, u
    return False, 1

def factor_gaussian(z):
    """
    Factoriza un entero gaussiano z en primos gaussianos.
    Retorna una lista de factores gaussianos tal que:
       z = (factor_1) * (factor_2) * ... * (factor_k)
    """
    if z == 0:
        raise ValueError("El 0 no tiene factorización en primos gaussianos.")
    
    original_z = z  # Guardamos el número original para la verificación final.
    factors = []
    
    # Primero extraemos los factores relacionados con el 2:
    # En Z[i] se tiene 2 = (1+i)^2
    while divides(z, 1 + 1j):
        factors.append(1 + 1j)
        z = divide_exact(z, 1 + 1j)
    
    # Ahora, mientras z no sea una unidad, intentamos extraer factores según la factorización entera de N(z)
    while not is_unit(z):
        a, b = int(z.real), int(z.imag)
        N = a*a + b*b
        # Factorizamos N en Z donde factorint nos devuelve las factorizaciones primas como keys y multiplicidades como values
        fact_int = factorint(N)
        factor_extraido = False
        
        # Recorremos los primos enteros (ordenados para procesar primero los más pequeños)
        for p in sorted(fact_int.keys()):
            if p == 2:
                # Ya se extrajeron los factores de 2 previamente.
                continue
            if p % 4 == 3:
                # p permanece primo en Z[i]. Se considera el candidato p (con parte imaginaria 0).
                candidate = complex(p, 0)
                if divides(z, candidate):
                    factors.append(candidate)
                    z = divide_exact(z, candidate)
                    factor_extraido = True
                    break
            elif p % 4 == 1:
                # p se descompone en dos factores conjugados: hallar una representación p = a^2 + b^2.
                rep = sum_of_two_squares(p)
                if rep is None:
                    continue  # Aunque esto no debería ocurrir para p ≡ 1 mod 4.
                a_rep, b_rep = rep
                candidate = complex(a_rep, b_rep)
                candidate_conj = complex(a_rep, -b_rep)
                if divides(z, candidate):
                    factors.append(candidate)
                    z = divide_exact(z, candidate)
                    factor_extraido = True
                    break
                elif divides(z, candidate_conj):
                    factors.append(candidate_conj)
                    z = divide_exact(z, candidate_conj)
                    factor_extraido = True
                    break
        if not factor_extraido:
            # Si no se extrajo ningún factor, z es primo.
            factors.append(z)
            break

    # Verificación final: se asegura que el producto de los factores sea exactamente original_z.
    prod = 1
    for f in factors:
        prod *= f
    if prod != original_z:
        # Si prod y original_z son asociados, se halla la unidad u tal que prod * u = original_z
        assoc, u = are_associates(original_z, prod)
        if assoc and u != 1:
            # se actualiza el valor del primer factor para que considere la unidad por lo que no se afecta la primalidad
            factors[0] *= u
    
    return factors

if __name__ == "__main__":
    test_numbers = [
        complex(5, 0),   # 5 se factoriza en (2+i) y (2-i) (o sus asociados)
        complex(7, 0),   # 7 es primo en Z[i] (ya que 7 ≡ 3 mod 4)
        complex(3, 2),   # 3+2i es primo (norma 13)
        complex(11, 0),  # 11 es primo en Z[i] (11 ≡ 3 mod 4)
        complex(1, 4),   # 1+4i: norma 17, se factoriza en dos primos conjugados
        complex(6, 9),  # no voy a hacer comentarios para cada cosito >:(
        complex(-3, 4),
        complex(-2319, -1694),  # Factorización con números grandes
        complex(16729, 0),
        complex(10, 91),
        complex(485062, 852697), # me dieron ganas de probarlo
        complex(785051162, 85269456947) # lo hace muy rapido :o que miedo
    ]
    
    for z in test_numbers:
        print(f"Factorización de {z}:")
        try:
            factors = factor_gaussian(z)
            if factors:
                factor_str = " * ".join(str(f) for f in factors)
                print(f"{z} = {factor_str}")
                
                # Verificación:
                result = 1
                for f in factors:
                    result *= f  # Multiplicación acumulada
                print(f"Verificación: {factor_str} = {result}")
                
                assoc, unit_corr = are_associates(result, z)
                if result == z:
                    print("Verificación exitosa!")
                elif assoc:
                    print(f"El resultado difiere del original por una unidad: {unit_corr}")
                    print(f"{z} = {unit_corr} * {factor_str}")
                else:
                    print(f"¡Error en la verificación! Se esperaba {z}, se obtuvo {result}")
            else:
                print(f"{z} es una unidad.")
        except ValueError as e:
            print(e)
        print("-" * 40)
