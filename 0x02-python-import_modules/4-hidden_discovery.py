#!/usr/bin/python3.8

if __name__ == '__main__':
    import hidden_4

    hidd_names = dir(hidden_4)

    for i in hidd_names:
        if not i.startswith('__'):
            print(i)
