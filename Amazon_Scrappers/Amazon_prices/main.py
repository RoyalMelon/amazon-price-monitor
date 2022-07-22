from data import *
from utilities import Help as help
from time import sleep


def main():
    
    def run_program():
        for item in data:
            for index in range(len(item)):
                help.is_sale(item[index])
                
                
    one_day = 86400
    while True:
        run_program()
        sleep(one_day)
        


if __name__ == '__main__':
    main()
