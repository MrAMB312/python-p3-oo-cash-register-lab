#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0, items=None):
    self._discount = 0
    self._total = 0
    self._items = []
    self._transactions = []
    self.discount = discount
    self.total = total
    self.items = items

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, discount):
    if isinstance(discount, (int, float)) and 0 <= discount:
      self._discount = discount
    else:
      print("Discount cannot be a negative value.")

  @property
  def total(self):
    return self._total

  @total.setter
  def total(self, total):
    if isinstance(total, (int, float)):
      self._total = total
    else:
      print("Total must be a number.")

  @property
  def items(self):
    return self._items

  @items.setter
  def items(self, items):
    if isinstance(items, list):
      self._items = items
    else:
      print("Items is not a list.")

  def add_item(self, title, price, quantity=1):
    if isinstance(title, str) and isinstance(price, (int, float)) and isinstance(quantity, int):
      for _ in range (quantity):
        self._items.append(title)
      self.total += price * quantity
      self._transactions.append((title, price * quantity))
    else:
      print("Invalid title, price, or quantity.")

  def apply_discount(self, discount=0):
    if self.discount > 0:
      discounted_total = self.total * (1 - self.discount / 100)
      self.total = int(discounted_total)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if self._transactions:
      last_transaction = self._transactions.pop()
      _, amount = last_transaction
      self.total -= amount
    else:
      print("No transactions to void.")