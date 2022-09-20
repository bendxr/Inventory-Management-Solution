"""
Inventory Management
"""

from exceptions import *

class Inventory:
  def __init__(self, items=[]):
    """
    :param items: list - list of items to create an inventory from.
    """
    self.inventory = {}
    if len(items) > 0:
      self.add_items(items)

  def add_items(self, items):
    """
    :param items: list - list of items to update the inventory with.
    """
    for i in items:
      self.inventory[i] = self.inventory.get(i, 0) + 1

  def decrement_items(self, items):
    """
    :param items: list - list of items to decrement from the inventory.
    """
    for i in items:
      if i in self.inventory.keys():
        if self.inventory[i] > 0:
          self.inventory[i] -= 1
      else:
        raise NonExistentItemException("{} does not belong to the inventory".format(i))

  def remove_item(self, item):
    """
    :param item: str - item to remove from the inventory.
    """
    if item in self.inventory:
        del self.inventory[item]
    else:
      raise NonExistentItemException("{} does not belong to the inventory".format(item))

  def list(self):
    """
    :return: the sorted tuples list (item, quantity) of the items
    """
    output_inventory = sorted([(k, v) for k, v in self.inventory.items() if self.inventory[k] > 0])
    return output_inventory

  def status(self):
    """
    :return: the string of the status of the inventory
      for each item, you will have a line like this: <item> : <quantity>\n
    """
    res = ""
    inv_list = self.list();
    if len(inv_list) > 0:
      for k, v in inv_list:
        res = res +"{} : {}\n".format(k, v)
    return res
    
  def clear(self):
    """
    clears all the inventory
    """
    self.inventory.clear()