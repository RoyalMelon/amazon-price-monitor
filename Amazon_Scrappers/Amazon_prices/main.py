from data import *
from utilities import Help as help
from time import sleep


def main():
    while True:

        def run_program():
            for item in data:
                for index in range(len(item)):
                    help.is_sale(item[index])

        run_program()
        one_day = 86400
        sleep(one_day)
        


if __name__ == '__main__':
    main()
