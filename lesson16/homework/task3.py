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


class ProductStore:
    product_list = []

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
                print(i)
                print(identifier)
                if i[1] == identifier:
                    i[3] = round(i[3] - (i[3] * fraction_percent), 2)
                else:
                    raise ValueError
        else:
            if identifier_type == 'type':
                for i in self.product_list:
                    if i[0] == identifier:
                        i[3] = round(i[3] - (i[3] * fraction_percent), 2)
                    else:
                        raise ValueError

    def identifiers(self, type):
        pass

    def sell_product(self, product_name, amount):
        pass

    def get_income():
        pass

    def get_all_products():
        pass

    def get_product_info(product_name):
        pass


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.set_discount('Ramen', 10, identifier_type='name')

print(s.product_list)

# s.sell(‘Ramen’, 10)
#
# assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
