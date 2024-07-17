from customer import Customer
from item import Item
from seller import Seller
from ownable import Ownable
from cart import Cart

seller = Seller("tienda DIC")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("memoria", 13880, seller)
    Item("tarjeta madre", 28980, seller)
    Item("Unidad de fuente de alimentación", 8980, seller)
    Item("caja de la computadora", 8727, seller)
    Item("Disco duro de 3,5 pulgadas", 10980, seller)
    Item("SSD de 2,5 pulgadas", 13370, seller)
    Item("SSD M.2", 12980, seller)
    Item("enfriador de CPU", 13400, seller)
    Item("tablero grafico", 23800, seller)

print("🤖 Porfavor dime tu nombre")
customer = Customer(input())

print("🏧 Por favor ingresa el monto a cargar a tu billetera")
customer.wallet.deposit(int(input()))

print("🛍️ empieza a comprar")
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos")
    seller.show_items()

    print("️️⛏ Por favor ingrese el número de producto")
    number = int(input())

    print("⛏ Por favor ingrese la cantidad del producto")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 cantidad total: {customer.cart.total_amount()}")

    print("😭¿Quieres terminar de comprar? (yes/no)")
    end_shopping = input() == "yes"

print("💸 ¿Confirmar tu compra?(yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️{customer.name}propiedad de")
customer.show_items()
print(f"😱👛 {customer.name}saldo de billetera de: {customer.wallet.balance}")

print(f"📦 {seller.name}estado del inventario")
seller.show_items()
print(f"😻👛 {seller.name}saldo de billetera de: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 cantidad total: {customer.cart.total_amount()}")

print("🎉 fin")
