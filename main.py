from inventory import Inventory
from exceptions import *

inv = Inventory()
print(inv.status())
inv.add_items(["wood", "wood", "carrot", "leek"])
print(inv.status())
inv.add_items(["wool", "carrot", "leek", "leek", "stone", "stone", "stone", "wood"])
print(inv.status())
inv.decrement_items(["wool", "wool", "wood", "stone", "stone"])
print(inv.status())
inv.remove_item("leek")
print(inv.status())
