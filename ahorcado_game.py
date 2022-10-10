import random

palabra_inicial = []
my_palabra_armada = []
vidas_del_juego = [3]
count_error = [0]


def persona_haorcado(a):
    data_error = [
        {"1": """
        
        
         
         
        ___________
        """,
         "2": """
        ______
        |
        |
        |
        |
        |__________
        """,
         "3": """
        _______
        |     |
        |     o 
        |    /|\*
        |   _/\_
        |__________
        """},
    ]
    for i in data_error:
        print(i[a])


def palabra_random():
    my_list = ['perro', 'arbol', 'lol', 'diego']
    r = random.randint(0, len(my_list) - 1)
    palabra = my_list[r]
    palabra_inicial.append(palabra)


def valida(a, b):
    return a == b


def repetir_bucle():
    if vidas_del_juego[0] == 0:
        print('-------PERDISTE - TERMINASTE TUS VIDAS--------')
        return False
    if palabra_inicial[0] == ''.join(my_palabra_armada):
        print('-----------------GANASTE!!--------------------')
        return False
    return True


def vidas_juego(vidas):
    vdj = list(map(lambda x: x - 1, vidas_del_juego))
    cr = list(map(lambda x: x + 1, count_error))
    vidas_del_juego[0] = vdj[0]
    count_error[0] = cr[0]
    persona_haorcado(str(count_error[0]))


def construye_array(array_palabra):
    for p in list(array_palabra):
        my_palabra_armada.append('__')
    print(my_palabra_armada)


def logica(vidas, palabra, input_palabra):
    error = []
    array_palabra = list(palabra)
    i = 0
    for p in array_palabra:
        i += 1
        if valida(p, input_palabra):
            if my_palabra_armada[i - 1] == "__":
                my_palabra_armada[i - 1] = p
            error.append('s')
        else:
            if my_palabra_armada[i - 1] == "__":
                my_palabra_armada[i - 1] = "__"
            error.append('n')

    if 's' in error:
        print('-----------------------------------------------------')
        print('corecto!!!!', 'Vidas disponibles: ', vidas_del_juego[0])
        persona_haorcado(str(count_error[0]))
    else:
        print('-----------------------------------------------------')
        print('INCORECTO!!!', 'Vidas disponibles: ', vidas_del_juego[0])
        vidas_juego(vidas)

    print(my_palabra_armada)


def run():
    print('-----------------------------------------------------')
    print('-----------BIENVENIDOS AL JUEGO - AHORACADOS---------')
    print('-----------------------------------------------------')
    palabra_random()
    construye_array(list(palabra_inicial[0]))
    while repetir_bucle():
        e = input('Introdusca la Palabra: ')
        logica(vidas_del_juego[0], palabra_inicial[0], e)


if __name__ == '__main__':
    run()
