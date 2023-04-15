from typing import List, Dict
from time import sleep
from src.views.menu_view  import menu
from src.models.model_product import Product
from src.utils.utils_helper import currency_formatter


product: List[Product] = []
cart: List[Dict[Product, int]] = []

menu = menu()


