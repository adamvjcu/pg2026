def add(a, b):
    c = a + b
    return c

def mul(a, b, c):
    return a * b * c

def div(a, b):
    if b == 0:
        return "Chyba: Dělení nulou není možné!"
    return a / b

def jedelitelnebezzbytku(a ,b):
    if a % b == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    x1 = add(1, 2)
    print(x1)  # Výsledek: 3
    
    x2 = mul(1, 2, 3)
    print(x2)  # Výsledek: 6
    
    x3 = div(10, 2)
    print(x3)  # Výsledek: 5.0
    
    x4 = div(10, 0)
    print(x4)  # Výsledek: Chyba: Dělení nulou není možné!

    x5 = jedelitelnebezzbytku(10, 2)
    print(x5)  # Výsledek: True