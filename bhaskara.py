from math import sqrt

def bhaskara(a, b, c):
    """Método para resolver equações de segundo grau encontrando suas raízes, se utilizando da fórmula de Bhaskara

    Args:
        a (integer): Primeiro coeficiente da fórmula
        b (integer): Segundo coeficiente da fórmula
        c (integer): Terceiro coeficiente da fórmula

    Returns:
        dict: Dicionário contendo as duas raízes como resultado do cálculo, caso o delta seja negativo ele retornará seus valores como 'Indefinido' (x1 : x2)
    """
    
    x1 = 0
    x2 = 0
    delta = pow(b, 2) - 4 * a * c
    
    try:
        x1 = (-b + sqrt(delta)) / 2*a
        x2 = (-b - sqrt(delta)) / 2*a
    except ValueError:
        return {
            "x1": 'Indefinido',
            "x2": 'Indefinido'
        }
    else:
        return {
            "x1": x1,
            "x2": x2
        }