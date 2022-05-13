
class Product:
    def __init__(self, p_type, p_name, p_price):
        self.p_type = p_type
        self.p_name = p_name
        self.p_price = p_price


class ProductStore:
    def __init__(self):
        self.product_stock = []
        self.discounts = {}
        self.current_income = 0

    def add(self, in_product, in_amount):
        success, product, index = self.find_product_op(in_product.p_name)
        if success:
            print(f'Product is already in stock! Adding {in_amount} more of {product[0].p_name}')
            self.update_amount(index, product[1] + in_amount)
        else:
            print(
                f'x{in_amount} of {in_product.p_name}, Category: {in_product.p_type}, With {in_product.p_price} price per piece (+30% interest) successfully added!')
            temp_product = Product(in_product.p_type, in_product.p_name, round((in_product.p_price * 1.3), 2))
            self.product_stock.append((temp_product, in_amount))

    def update_amount(self, index, new_amount):
        self.product_stock[index] = (self.product_stock[index][0], new_amount)
        print(f'Item: {self.product_stock[index][0].p_name} now x{self.product_stock[index][1]} in stock!')

    def delete_product_op(self, index):
        temp_product = self.product_stock.pop(index)
        print(
            f'Item: {temp_product[0].p_name}, Category: {temp_product[0].p_type} is out of stock! Removing it from database...')

    def set_discount(self, product_identifier, percent, identifier_type='name'):
        local_success = False
        try:
            if identifier_type == 'name' or identifier_type == 'type':
                self.discounts[product_identifier] = (identifier_type, percent)
                local_success = True
        except:
            local_success = False
            print('Product discount must be added by product name or type!')
        if local_success:
            print(f'{percent} discount for "{product_identifier}" has been added!')
        return local_success

    def get_discount_percent(self, product_name='none', product_type='none'):  # quietly
        local_success = False
        out_discount = 0
        if product_name == 'none' and product_type == 'none':
            local_success = False
        else:
            local_discount_by_name = 0
            local_discount_by_type = 0
            if product_name in self.discounts:
                local_discount_by_name = self.discounts[product_name][1]
                local_success = True
            if product_type in self.discounts:
                local_discount_by_type = self.discounts[product_type][1]
                local_success = True
            if local_success:
                out_discount = max(1, min(local_discount_by_name + local_discount_by_type,
                                          99))  # going big with additive discounts clamped 1-99%
        return local_success, out_discount

    def sell(self, p_name, amount):
        success, product, index = self.find_product_op(p_name)
        if success:
            local_discount = 0
            success, local_discount = self.get_discount_percent(product[0].p_name, product[0].p_type)
            local_amount = product[1]
            local_sell_amount = (amount, local_amount)[local_amount - amount < 0]
            print(f'{product[0].p_name} x{local_sell_amount} sold!')

            if local_amount == local_sell_amount:
                self.delete_product_op(index)
            else:
                self.update_amount(index, local_amount - amount)
            self.current_income = self.current_income + (local_sell_amount * product[0].p_price - (
                        (local_discount * (local_sell_amount * (product[0].p_price))) / 100))
        else:
            print('Product not found!')

    def get_product_info(self, p_name):
        success, product, index = self.find_product_op(p_name)
        if success:
            print(
                f'Item: {product[0].p_name}, Category: {product[0].p_type}, Price per piece: {product[0].p_price}. Avaliable {product[1]} pcs.')

    def get_all_products(self):
        print('----------STOCK--------')
        for item, amount in self.product_stock:
            self.get_product_info(item.p_name)
        print('-----------------------')

    def get_income(self):
        print(f'Current income: {self.current_income}')

    def find_product_op(self, p_name):
        local_found = False
        local_index = 0
        item = None
        amount = 0
        for item, amount in self.product_stock:
            if p_name == item.p_name:
                local_found = True
                local_index = self.product_stock.index((item, amount))
                break
        return local_found, (item, amount), local_index


Store = ProductStore()

Prod = Product('Sport', 'Football T-Shirt', 100)
Prod1 = Product('Food', 'Ramen', 1.5)
Prod2 = Product('Food', 'Bread', 4)
Prod3 = Product('Sport', 'Treadmill', 5000)

