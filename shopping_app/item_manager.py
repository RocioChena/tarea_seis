# Si incluyes este módulo, podrás manipular tus propias instancias de Item.

from item import Item
from tabulate import tabulate
from itertools import groupby

def items_list(self):   # Devuelve todas las instancias de Item que pertenecen al usuario。
    items = [item for item in Item.item_all() if item.owner == self]
    return items

def pick_items(self, number, quantity):   #  Devuelve el número y el número de instancias de Item que pertenecen a la cantidad especificada.
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]

def show_items(self):   # Muestre el estado de inventario de la instancia de artículo que posee en un formato de tabla con las columnas ["Número", "Nombre del producto", "Importe" y "Cantidad"].

    table_data = []
    for stock in _stock(self):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["número", "nombre comercial", "Cantidad de dinero", "cantidad"], tablefmt="grid"))    # tabulateモジュールを使ってテーブル形式で結果を出力

def _stock(self):   # Devuelve la disponibilidad de la instancia de Item que pertenece al usuario.
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(item_ls, key=lambda m: m.name):   # Item#name, que devuelve el mismo valor.
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append({"number": index, "label": {"name": item[0].name, "price": item[0].price}, "items": item})   # itemsの中には、分類されたItemインスタンスが格納されます。
    return stock
