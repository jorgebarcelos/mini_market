from src.utils.utils_helper import currency_formatter


class Product:
    id_count: int = 1

    def __init__(self: object, name: str, price: float) -> None:
        self.__code: int = Product.id_count
        self.__name: str = name
        self.__price: float = price
        Product.id_count += 1


    @property
    def code(self: object) -> int:
        return self.__code
    
    @property
    def name(self: object) -> str:
        return self.__name
    
    @property
    def price(self: object) -> float:
        return self.__price
    
    def __str__(self) -> str:
        return f'Code: {self.code} \nName: {self.name} \nPrice: {currency_formatter(self.price)}'