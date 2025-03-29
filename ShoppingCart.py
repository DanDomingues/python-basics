from TerminalApp_Base import ConsoleApplication
from typing import Dict, List, Tuple

#improvements:
#rework tuple into list for value incrementing
#add inventory checking as decorator
#Write tests

class Product:
    def __init__(self, name: str, price: float, prod_id: str):
        self.name = name
        self.price = price
        self.prod_id = prod_id

    def __str__(self):
        return f'[{self.prod_id}] - {self.name} : {self.price}$'

def generate_products() -> Dict[str, Product]:
    return { p.prod_id: p for p in [
        Product('Apple (Fuji)', 1.99, '1001'),
        Product('Apple (Gala)', 2.49, '1002'),
        Product('Banana', .99, '1003'),
        Product('Strawberry', 4.99, '1004'),
        Product('Kiwi', 3.99, '1005'),
    ]}

def show_products(products: List[Product]) -> None:
    print('Displaying product catalog:')
    for prod in products:
        print(prod)

def show_cart(cart: Dict[str, Tuple[Product, int]], add_header: bool = True) -> None:
    if len(cart.keys()) == 0:
        print('Cart is empty.')
        return

    if add_header:
        print('Displaying cart items:')

    for (prod, amount) in cart.values():
        new_prod = Product(prod.name, prod.price * amount, prod.prod_id)
        print(f'{new_prod} (x{amount})')

def get_item_from_dict(dictionary: Dict, label: str = 'Please input product ID: '):
    p_id = ''
    while p_id not in dictionary.keys():
        p_id = input(f'{label} ')
    return dictionary[p_id]

def add_to_cart(
        catalog: Dict[str, Product],
        cart: Dict[str, Tuple[Product, int]]) -> None:

    product = get_item_from_dict(catalog)
    p_id = product.prod_id

    if p_id not in cart:
        cart[p_id] = (product, 1)
    else:
        prod, amount = cart[p_id]
        cart[p_id] = (prod, amount + 1)

    print(f'Added 1 {product.name} to cart')
    show_cart(cart)

def remove_from_cart(cart: Dict[str, Tuple[Product, int]]) -> None:
    if len(cart.keys()) == 0:
        print('Cart is empty.')
        return

    product = get_item_from_dict(cart)
    p_id = product.prod_id

    if p_id not in cart:
        print('Item ID not in cart.')
        return

    if cart[p_id][1] > 1:
        prod, amount = cart[p_id]
        cart[p_id] = (prod, amount - 1)
    else:
        cart.pop(p_id)

    print(f'Removed 1 {product.name} from cart')
    show_cart(cart)

def checkout(cart: Dict[str, Tuple[Product, int]]) -> None:
    if len(cart.keys()) == 0:
        print('Cart is empty.')
        return

    show_cart(cart, add_header=False)
    total: float = sum((tup[0].price * tup[1] for tup in cart.values()))
    print(f'Your total is: {total}$')

def init_app(
        catalog: Dict[str, Product],
        cart: Dict[str, Tuple[Product, int]]) -> ConsoleApplication:

    return ConsoleApplication(
        "John's Fruit Market",
        {
            'Main':[
                ['D', 'Display products', lambda: show_products([p for p in catalog.values()])],
                ['S', 'Show cart', lambda: show_cart(cart)],
                ['A', 'Add product', lambda: add_to_cart(catalog, cart)],
                ['R', 'Remove product', lambda: remove_from_cart(cart)],
                ['E', 'Checkout', lambda: checkout(cart)],
            ]})

def start_system():
    #local variables creation
    cart: Dict[str, Tuple[Product, int]] = dict()
    catalog: Dict[str, Product] = generate_products()
    app: ConsoleApplication = init_app(catalog, cart)
    state: str = 'Main'

    #Shows intro and starts loop
    app.show_intro()
    while True:
        app.show_inputs(state, suffix='Please enter a menu key')
        app.read_input_for(state, run_associated_callback=True)
        print('')

start_system()