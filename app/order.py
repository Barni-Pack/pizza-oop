from ctypes import ArgumentError
from app.pizza_classes import Pizza


class Order:
    def __init__(self) -> None:
        '''Inits order with list of products'''
        self.products_list: list[Pizza] = []
        
    def add_product(self, product: Pizza) -> None:
        '''Adds product to order'''
        self.products_list.append(product)
      
    def remove_product(self, product: Pizza) -> None:
        '''Removes product from order'''
        try:
            self.products_list.remove(product)
        except ValueError:
            print(f'Product "{product.name}" not in products_list')
        
    def get_total_price(self):
        '''Returns total price of order'''
        total_price = 0
        for product in self.products_list:
            total_price += product.price
        return total_price
            
    # def product_in_stock(self, func):
    #     def wrapper(**kw):
    #         if kw['product'] in self.products_list:
    #             func()
    #         else:
    #             raise Exception('Product is out of stock')
        
    
    def commit(self):
        '''Prints total price and clears order'''
        print(self.get_total_price())
        self.products_list = []
    

if __name__ == "__main__":
    from pizza_classes import Pepperoni
    p1 = Pepperoni()
    o1 = Order()
    o1.add_product(p1)
    o1.add_product(p1)
    print(o1.get_total_price())