# Context
In this Dojo, you will be managing an inventory system.

The inventory should be organized by the item name and it should keep track of the number of items available.

You will have to handle adding items to an inventory. Each time an item appears in a given list, increase the item's quantity by 1 in the inventory. Then, you will have to handle deleting items from an inventory.

Then you will have to implement a method which returns all the key-value pairs in an inventory as a list of tuples.

# Implementation Guidelines
## Implement the Class Inventory methods
### Constructor

Creates a new inventory, that may be initialized with a list of items.
```python
>>> inv = Inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
==> {"coal":1, "wood":2 "diamond":3}
```

### Add items from a list to an existing dictionary

Implement the `add_items()` method that adds a list of items to an inventory:
```python
>>> inv.add_items(["wood", "iron", "coal", "wood"])
{"coal":1, "wood":2 "diamond":3} ==> {"coal":2, "wood":4, "diamond":3, "iron":1}
```

### Decrement items from the inventory

Implement the `decrement_items(<items>)` method that takes a list of items. It should remove one from the available count in the inventory for each time an item appears on the list:

```python
>>> inv.decrement_items(["diamond", "coal", "iron", "iron"])
{"coal":3, "diamond":1, "iron":5} ==> {"coal":2, "diamond":0, "iron":3}
```

Item counts in the inventory should not fall below 0. If the number of times an item appears on the list exceeds the count available, the quantity listed for that item should remain at 0 and additional requests for removing counts should be ignored.

```python
>>> inv.decrement_items(["coal", "coal", "wood", "wood", "diamond"])
{"coal":0, "wood":0, "diamond":1}
```

It should raise `NonExistentItemException` when trying to decrement an item that does not belong at all to the inventory.

### Remove an item entirely from the inventory

Implement the `remove_item(<item>)` method that removes an item and its count entirely from an inventory:

```python
>>> inv.remove_item("coal")
{"coal":2, "wood":1, "diamond":2} ==> {"wood":1, "diamond":2}
```

If the item is not found in the inventory, the method should raise `NonExistentItemException`.


### Return the inventory list

Implement the `list()` method that takes an inventory and returns a list of (item, quantity) tuples. The list should only include the available items (with a quantity greater than zero):

```python
>>> inv.list()
{"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0} ==> [('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)]
```

### Print the inventory
Based on the previous list, build a status string of the inventory
```python
>>> inv.status()
{"wood":11, "diamond":2, "iron":7} ==> "wood : 11\ndiamond : 2\niron : 7\n"
```
### Clear the inventory
Just clear the whole inventory.
```python
>>> inv.clear()
{"wood":11, "diamond":2, "iron":7} ==> {}
```

## Exception
The Exception `NonExistentItemException` should inherit from `KeyError` Python built-in exception.