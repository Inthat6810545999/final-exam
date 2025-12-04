class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Hi, I'm {self.name}.")

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
    def place_order(self, item):
        self.item = item
        return self.item

class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle
    
    def deliver(self, order, customer):
        self.order = order
        print(f'{self.name} is delivering {self.order} to {customer} using {self.vehicle}.')
    
    def deliverd(self, orders):
        self.orders = orders
        print(f'Order for {self.orders} → delivered')
class DeliveryOrder:
    def __init__(self, customer, item, status):
        self.customer = customer
        self.item = item
        self.status = status
    def assign_driver(self, driver):
        self.driver = driver
    def summary(self):
        print("Order Summary:")
        print(f'Item: {self.item}')
        print(f'Customer: {self.customer}')
        print(f"Status: {self.status}")
        print(f'Driver: {self.driver}')
        

#main part
if __name__ == '__main__':
    a = Person('Alice')
    b = Person('Bob')
    c = Person('David')
    a.introduce()
    b.introduce()
    c.introduce()
    print()
    a1 = Customer(a.name, 'home')
    first_order = a1.place_order("laptop")
    a2 = Customer(b.name, 'home')
    second_order = a2.place_order('Headphones')
    a3 = Driver(c.name, 'motorcycle')
    
    Deliver = DeliveryOrder(a.name, first_order, 'preparing')
    courier = Deliver.assign_driver(c.name)
    Deliver.summary()
    print()

    Deliver2 = DeliveryOrder(b.name, second_order, 'preparing')
    courier = Deliver2.assign_driver(c.name)
    Deliver2.summary()
    print()

    a3.deliver(first_order, a1.name)
    a3.deliver(second_order, a2.name)
    print()
    print('Final Status:')
    a3.deliverd(first_order)
    a3.deliverd(second_order)




