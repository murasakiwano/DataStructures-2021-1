def pontuar(cartas):
    if len(cartas) <= 3:
        m1 = max(cartas)
        cartas.remove(m1)
        return m1 + max(cartas)
    s1 = descartar(cartas[1:])
    s2 = descartar(cartas[:-1])

def descartar(cartas):
    return pontuar(cartas)