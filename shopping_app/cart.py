

from ownable import Ownable

class Cart(Ownable):
    from item_manager import show_items
    def __init__(self, owner):
        super().__init__()
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        total = self.total_amount()
        if self.owner.wallet.balance < total:
            print ("Saldo insuficiente")
            return 
        
        for item in self.items:
            self.owner.wallet.balance -= item.price
            item.owner.wallet.balance += item.price
            item.owner = self.owner
        
        self.items = []
        print("Compra completada. El carrito está vacío.")

        
        
        
        
        
        
        
        
        # Eliminar pase al codificar el método check_out.

       # Requisitos

    #: el monto de la compra de todos los artículos en el carrito (Cart#items) se transfiere de la billetera del propietario del carrito a la billetera del propietario del artículo.
    # #: la propiedad de todos los artículos del carrito (Cart#items) se transfiere al propietario del carrito. 
    # # - El contenido del carrito (Cart#items) está vacío.
       # Consejo
    # - Cartera del propietario del carrito ==> self.owner.wallet 
    # # - Cartera del propietario del artículo ==> item.owner.wallet
    # # - El dinero se transferirá ==> Esa cantidad de la cartera de (?) Retirar y depositar la cantidad en (?) billetera 
    # # - La propiedad del artículo se transfiere al propietario del carrito ==> Reescribir el propietario (item.owner =?)

