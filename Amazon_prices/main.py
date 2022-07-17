from data import data
from utilities import Help as help

from time import sleep


def main():
    while True:

        def run_program():
            for item in data:
                for index in range(len(item)):
                    help.is_sale(item[index])

        # Program runs every two hours
        run_program()
        sleep(7200)


if __name__ == '__main__':
    main()
