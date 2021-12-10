class Person:
  def __init__(self, name, favorite_drink, wallet, tip_amount):
    self.name = name
    self.favorite_drink = favorite_drink
    self.wallet = wallet
    self.tip_amount = tip_amount

  def my_order(self):
    return Order(self, self.favorite_drink)



class Order:
  def __init__(self, person, type):
    self.person = person
    self.type = type

  def to_string(self):
    print(f'{self.person.name} orders: {self.type}')



class CoffeeBar:
  def __init__(self, name, barista):
    self.name = name
    self.orders = []
    self.barista = barista
    self.register = 0.00
    self.menu = {
      'Coffee': '3.99',
      'Tea': '2.95',
      'Milk': '1.85',
      'Cocoa': '3.59',
    }
    self.receipts = []
    self.tip_jar = 0.00

  def tip_calculator(self, order):
    price = float(self.menu[order.type])
    tip = price * order.person.tip_amount
    total = price + tip
    return (tip, total)

  def place_order(self, order):
    (tip, total) = self.tip_calculator(order)
    if order.person.wallet >= total:
      # Deduct from person's wallet
      order.person.wallet = round(order.person.wallet - total, 2)
      # Add money to register
      self.register = round(self.register + total, 2)
      self.orders.append(order)
    else:
      print(f'{order.person.name} has insufficient funds! Order not placed...')

  def process_orders(self):
    print(self.barista.greeting)
    for order in self.orders:
      order.to_string()
      self.receipts.append(order)
      (tip, total) = self.tip_calculator(order)
      self.tip_jar += tip
    # empty the orders list
    self.orders = []
    # The barista takes all the tips, then empty the tip jar
    self.barista.wallet = round(self.barista.wallet + self.tip_jar, 2)
    self.tip_jar = 0
    
  def cash_out(self):
    print(f'Money in register: ${format(self.register, ".2f")}')



class Barista(Person):
  def __init__(self, name, favorite_drink, wallet, tip_amount, greeting):
    super().__init__(name, favorite_drink, wallet, tip_amount)
    self.greeting = greeting




# 3 customers
amy = Person('Amy', 'Coffee', 5.47, 0.20)
bob = Person('Bob', 'Tea', 10.00, 0.18)
cat = Person('Cat', 'Milk', 7.89, 0.15)

# Barista
kevin = Barista('Kevin', 'green tea', 0.00, 0.15, 'Hey dude!')

# CoffeeBar
blue_ocean_coffee = CoffeeBar('Blue Ocean Coffee', kevin)

# Place 3 orders
blue_ocean_coffee.place_order(amy.my_order())
blue_ocean_coffee.place_order(bob.my_order())
blue_ocean_coffee.place_order(cat.my_order())
# Process all orders
blue_ocean_coffee.process_orders()

print(amy.wallet)
print(bob.wallet)
print(cat.wallet)

# Total revenue
blue_ocean_coffee.cash_out()

# Kevin made this much in tips:
print(blue_ocean_coffee.barista.wallet)

