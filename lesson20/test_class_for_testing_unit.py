from unittest import TestCase
from testing.class_for_testing import Product, ProductStore


class TestProductStore(TestCase):
    def setUp(self):
        self.store = ProductStore()
        self.prod = Product('Sport', 'Football T-Shirt', 100)
        self.prod1 = Product('Food', 'Ramen', 1.5)
        self.prod2 = Product('Food', 'Bread', 4)
        self.prod3 = Product('Sport', 'Treadmill', 5000)

    def test_add__success(self):
        self.store.add(self.prod, 10)
        name, amount = self.store.product_stock[0]
        name = name.p_name
        self.assertEqual((name, amount), ('Football T-Shirt', 10), 'Different product')

    def test_add__fail(self):
        self.store.add(self.prod1, 10)
        name, amount = self.store.product_stock[0]
        name = name.p_name
        self.assertNotEqual((name, amount), ('Football T-Shirt', 10), 'Same product')

    def test_update_amount__success(self):
        self.store.add(self.prod, 10)
        self.store.update_amount(0, 15)
        name, amount = self.store.product_stock[0]
        self.assertEqual(amount, 15, 'Different amount')

    def test_update_amount__fail(self):
        self.store.add(self.prod, 10)
        self.store.update_amount(0, 15)
        name, amount = self.store.product_stock[0]
        self.assertNotEqual(amount, 20, 'Same amount')

    def test_set_discount__success(self):
        self.store.add(self.prod3, 1)
        self.store.set_discount('Treadmill', 10)
        price = self.store.product_stock[0][0].p_price
        new_price = price - price * self.store.discounts['Treadmill'][1] / 100
        self.assertEqual(new_price, 5850, 'Different price') #https://www.youtube.com/watch?v=dQw4w9WgXcQ
#self.store.find_product_op('Treadmill')[1][0]).p_price

    def test_set_discount__fail(self):
        self.store.add(self.prod2, 1)
        self.store.set_discount('Bread', 100)
        price = self.store.product_stock[0][0].p_price
        new_price = price - price * self.store.discounts['Bread'][1] / 100
        self.assertNotEqual(new_price, 1, 'Same price')

    def test_sell__success(self):
        print(self.store.product_stock)
        self.store.add(self.prod, 15)
        self.store.sell(self.prod.p_name, 5)
        # self.store.update_amount(15, 10)
        name, amount = self.store.product_stock[0]
        self.assertEqual(amount, 10, 'Different amount')

    def test_sell__fail(self):
        self.store.add(self.prod, 15)
        self.store.sell(self.prod.p_name, 5)
        # self.store.update_amount(15, 10)
        name, amount = self.store.product_stock[0]
        self.assertNotEqual(amount, 5, 'Same amount')

    def test_get_income(self):
        self.store.add(self.prod3, 10)
        self.store.sell('Treadmill', 5)
        # item_tup = self.store.find_product_op('Treadmill')[1]
        # s, disc_perc = self.store.get_discount_percent(product_name='Treadmill', product_type='none')
        # prob_income = item_tup[0].p_price * 5 -(disc_perc*(item_tup[0].p_price * 5)/100)
        prob_income = self.store.product_stock[0][0].p_price * 5
        self.assertEqual(self.store.current_income, prob_income, 'Correct income')
