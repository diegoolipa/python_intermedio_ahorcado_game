def run():
    my_list = [1, "hola", True, 4.5]
    my_dict = {"firstname": "Fcundo", "lastname": "Diego"}

    super_list = [
        {"firstname": "Fcundo", "lastname": "Diego"},
        {"firstname": "Dniale", "lastname": "Diego"},
        {"firstname": "Maria", "lastname": "Diego"},
        {"firstname": "Pedro", "lastname": "Diego"},
        {"firstname": "Ricanrdo", "lastname": "Diego"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5, 5, 6, 6, 7],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 1.34, 3.12]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i['firstname'], ".", i['lastname'])


if __name__ == '__main__':
    run()
