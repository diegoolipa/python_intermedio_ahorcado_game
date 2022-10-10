def run():
    my_list = [1, 2, 3, 4, 5, 6]
    filter_ = list(filter(lambda x: x % 2 != 0, my_list))
    print(filter_)


if __name__ == '__main__':
    run()
