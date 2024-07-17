from user import User
from cart import Cart
from wallet import Wallet 

class Customer(User):

    def __init__(self, name):
        super().__init__(name)
        self.cart = Cart(self)
        
        # Cuando se crea una instancia de cliente, tiene un carro que es de su propiedad.
    