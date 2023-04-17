from src.controllers.main_controller import *
from src.views.menu_view  import menu
from time import sleep


def main() -> None:
    while True:
        menu()
        print('\n')
        option = input('Choose a option: ')
        if option == '1':
            register_product()
        elif option == '2':
            list_products()
        elif option == '3':
            buy_product()
        elif option == '4':
            show_cart()
        elif option == '5':
            close_order()
        elif option == '6':
            print('Come back anytime, bye!!')
            sleep(2)
            exit()
        else:
            print('INVALID OPTION !!!!!')


main()