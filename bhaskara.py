from math import sqrt

def bhaskara(a, b, c):
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