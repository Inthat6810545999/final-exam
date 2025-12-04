Inthat6810545999

Project Simple delivery service
Here's a sample README file for the project 
This project is a simple delivery service programme that allows users to order
 items and have them delivered to their doorstep.

To get started with the project, follow these steps:
first we need to assign the class 4 class for this project first 
we have person class second we have Customer 
class third we have driver class and fourth we have DeliveryOrder class
then we need to create a function that will handle the delivery process

class Person:
    def __init__(self, name):
        self.name = name assaign the name to person class
    def introduce(self):
        print(f"Hi, I'm {self.name}.") say hello 

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
    def place_order(self, item):
        self.item = item
        return self.item

class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name) assaign the name to driver class
        self.vehicle = vehicle
    
    def deliver(self, order, customer):
        self.order = order 
        print(f'{self.name} is delivering {self.order} to {customer} using {self.vehicle}.') we print the delivery message
    
    def deliverd(self, orders):
        self.orders = orders
        print(f'Order for {self.orders} → delivered') we print the delivered success message
class DeliveryOrder:
    def __init__(self, customer, item, status):
        self.customer = customer
        self.item = item
        self.status = status
    def assign_driver(self, driver):
        self.driver = driver assaign the driver to delivery order
    def summary(self): summary all of the order details
        print("Order Summary:")
        print(f'Item: {self.item}')
        print(f'Customer: {self.customer}')
        print(f"Status: {self.status}")
        print(f'Driver: {self.driver}')
        
step to run the project
#main part
if __name__ == '__main__':
    a = Person('Alice') 
    b = Person('Bob')
    c = Person('David')
    a.introduce() say hello 
    b.introduce() say hello 
    c.introduce() say hello 
    print()
    a1 = Customer(a.name, 'home') 
    first_order = a1.place_order("laptop") select the item to order
    a2 = Customer(b.name, 'home')
    second_order = a2.place_order('Headphones')
    a3 = Driver(c.name, 'motorcycle') assaign the vehicle to driver
    
    Deliver = DeliveryOrder(a.name, first_order, 'preparing') 
    courier = Deliver.assign_driver(c.name)
    Deliver.summary() summarize the order
    print()

    Deliver2 = DeliveryOrder(b.name, second_order, 'preparing')
    courier = Deliver2.assign_driver(c.name)
    Deliver2.summary()
    print()

    a3.deliver(first_order, a1.name)
    a3.deliver(second_order, a2.name)
    print()
    print('Final Status:')
    a3.deliverd(first_order) we print the delivered success message
    a3.deliverd(second_order) we print the delivered success message
    and the devllivery process is complete
![alt text](image.png)
