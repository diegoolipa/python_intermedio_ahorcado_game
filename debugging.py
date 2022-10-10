def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input("Ingrese un nuemro: "))
        assert int(num) > 0, 'assert:::::Ingrese un numero positivo'
        if num < 0:
            raise ValueError(" ::::Ingrese un numero positivo")  # Agregando un raise
        print(divisors(num))
        print('Termino mi programa')
    except ValueError as ve:  # capturar el error de tipo valueError
        print(ve)
        print('Debees ingresar un número')
        return False


if __name__ == '__main__':
    run()
