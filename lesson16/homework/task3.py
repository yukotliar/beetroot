# Product Store
#
# Write a class Product that has three attributes:
#     type
#     name
#     price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
#
# Tips: Use aggregation/composition concepts while implementing the ProductStore class.
# You can also implement additional classes to operate on a certain type of product, etc.
#
# Also, the ProductStore class must have the following methods:
#     add(product, amount) - adds a specified quantity of a single product with a predefined price premium
#     for your store (30 percent)
#     set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input
#     identifiers (type or name).The discount must be specified in percentage
#     sell_product(product_name, amount) - removes a particular amount of products from the store
#     if available, in other case raises an error.It also increments income if the sell_product method succeeds
#     get_income() - returns amount of many earned by ProductStore instance
#     get_all_products() - returns information about all available products in the store
#     get_product_info(product_name) - returns a tuple with product name and amount of items in the store

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore(Product):
    def __init__(self):
        self.product_list = []
        self.income = 0

    def add(self, product,
            amount):  # adds a specified quantity of a single product with a predefined price premium for your store (30 percent)
        product.amount = amount
        product.price = round(product.price * 1.3, 2)
        self.product_list.append([product.type, product.name, product.amount, product.price])

    def set_discount(self, identifier, percent,
                     identifier_type='name'):  # adds a discount for all products specified by input
        #     identifiers (type or name).The discount must be specified in percentage
        fraction_percent = percent / 100
        if identifier_type == 'name':
            for i in self.product_list:
                if i[1] == identifier:
                    i[3] = round(i[3] - (i[3] * fraction_percent), 2)
        else:
            if identifier_type == 'type':
                for i in self.product_list:
                    if i[0] == identifier:
                        i[3] = round(i[3] - (i[3] * fraction_percent), 2)

    def sell_product(self, product_name, amount):  # removes a particular amount of products from the store
        # if available, in other case raises an error. It also increments income if the sell_product method succeeds
        for i in self.product_list:
            if i[1] != product_name:
                pass
            else:
                if i[2] < amount:
                    raise ValueError
                else:
                    i[2] -= amount
                    self.income += round(amount * i[3], 2)


    def get_income(self): # returns amount of many earned by ProductStore instance
        return self.income

    def get_all_products(self): # returns information about all available products in the store
        return self.product_list

    def get_product_info(self, product_name): # returns a tuple with product name and amount of items in the store
        list = []
        for i in self.product_list:
            if i[1] == product_name:
                list += i[1], i[2]
        return tuple(list)


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.set_discount('Ramen', 10)

s.set_discount('Sport', 10, identifier_type='type')

s.sell_product('Ramen', 10)

print(s.get_all_products())

print(s.get_income())

print(s.get_product_info('Ramen'))

assert s.get_product_info('Ramen') == ('Ramen', 290)
