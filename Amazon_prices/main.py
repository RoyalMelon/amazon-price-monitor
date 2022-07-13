from data import data
from utilities import Help as help
from datetime import datetime


def main():
    while True:
        time = datetime.now()
        time = time.strftime("%H:%M:%S")

        def run_program():
            for item in data:
                for index in range(len(item)):
                    help.is_sale(item[index])

        # loops throught the values 0-12 in steps of twos
        # So that program runs every two hours
        for hour in range(0, 14, 2):
            if time == f'{hour}:00:00':
                run_program()


if __name__ == '__main__':
    main()
