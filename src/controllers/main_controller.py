from typing import List, Dict
from time import sleep
from src.views.menu_view  import menu
from src.models.model_product import Product
from src.utils.utils_helper import currency_formatter


products: List[Product] = []
cart: List[Dict[Product, int]] = []


def register_product() -> None:
    print('Product Register')
    print('================')

    name: str = input('Insert product name: ')
    price: float = input('Input product price: ')
    product: Product = Product(name, price)
    products.append(product)
    print(f'The product: {product.name} was registered with success!!')
    sleep(2)
    menu()


def list_products() -> None:
    if len(products) > 0:
        print('Product list')
        print('============\n')
        for product in products:
            print(product)
            print('============')
            sleep(1)
    else:
        print('There is no registered product yet :( ')
    
    sleep(2)
    menu()


def pick_product_by_code(code: int) -> Product:
    product_code: Product = None

    for product in products:
        if product.code == code:
            product_code = product
    return product_code


def buy_product() -> None:
    if len(products) > 0:
        print('Inform the product code to buy: ')
        print('================================')
        print('====== Available Products ======')
        for product in products:
            print(product)
            print('================================')
            sleep(1)

        code: int = int(input())
        product: Product = pick_product_by_code(code)

        if product:
            if len(cart) > 0:
                is_in_cart: bool = False
                for item in cart:
                    quantity: int = item.get(product)
                    if quantity:
                        item[product] = quantity + 1
                        print(f'The current product {product.name} quantity  in your cart is {quantity + 1}')
                        is_in_cart = True
                        sleep(2)
                        menu()
                if  not is_in_cart:
                    current_product = {product: 1}
                    cart.append(current_product)
                    print(f'The product {product.name} was added in cart')
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                cart.append(item)
                print(f'The product {product.name} was added in cart')
                sleep(2)
                menu()
        else:
            print(f'The product code {code} was not found')
            sleep(2)
            menu()
    else:
        print('There is no product to sale')
    sleep(2)
    menu()


def show_cart() -> None:
    if len(cart) > 0:
        print('Cart products')

        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print('====================')
                sleep(1)

    else:
        print('There is no products in cart')
    sleep(2)
    menu()


def close_order() -> None:
    if len(cart) > 0:
        total_value: float = 0
    
        print('Cart products')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                total_value += float(data[0].price) * data[1]
                print('====================\n')
                sleep(1)
    
        print(f'Total cart is: {currency_formatter(total_value)}')
        print('Come back anytime!!')
        cart.clear()
        sleep(2)

    else:
        print('There is no products in the cart')
    sleep(2)
    menu()



# class Process:

#     def __init__(self, products: List[Product], cart: List[Dict[Product, int]]) -> None:
#         self.products = []
#         self.cart = []


#     def register_product(self) -> None:
#         print('Product Register')
#         print('================')

#         name: str = input('Insert product name: ')
#         price: float = input('Input product price: ')
#         product: Product = Product(name, price)
#         self.cart.append(product)
#         sleep(2)
#         menu()

    
#     def list_products(self) -> None:
#         if len(self.products) > 0:
#             print('Product list')
#             print('============\n')
#             for product in self.products:
#                 print(product)
#                 print('============')
#                 sleep(1)
#         else:
#             print('There is no product yet :( ')
        
#         sleep(2)


#     def pick_product_by_code(self, code: int) -> Product:
#         product_code: Product = None

#         for product in self.products:
#             if product.code == code:
#                 product_code = product
#         return product_code


#     def close_order(self) -> None:
#         if len(self.cart) > 0:
#             total_value: float = 0
        
#         print('Cart products')
#         for item in self.cart:
#             for data in item.items():
#                 print(data[0])
#                 print(f'Quantity: {data[1]}')
#                 total_value += data[0].price * data[1]
#                 print('====================\n')
        
#         print(f'Total cart is: {currency_formatter(total_value)}')
#         self.cart.clear()
#         sleep(2)