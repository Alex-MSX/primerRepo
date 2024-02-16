def sumar(*args):
    return sum(args)


def saludar(nombre):
    print(f'Hola {nombre}! Cómo estás?')


suma = sumar(5,6,8,2,1,4,5,6,3)
print(suma)


saludar('Alejandro')