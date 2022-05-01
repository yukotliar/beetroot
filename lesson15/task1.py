# Створити клас, який описує поняття "онлайн магазин"

class Shop:
    def __init__(self, name, address, url, product, workers, delivery, payment):
        self.name = name
        self.address = address
        self.url = url
        self.product = product
        self.workers = workers
        self.status = True
        self.delivery = delivery
        self.payment = payment

    def close_shop(self):
        self.status = False

    def open_shop(self):
        self.status = True

    def sold(self):
        print('Продали товар')

    def buy_new(self):
        print('Закупили нових продуктів')

    def stop_sold(self):
        print('Заборона продажу')

    def add_worker(self, count):
        self.workers += count

    def remove_worker(self, count):
        self.workers -= count

    def print_information(self):
        print(self.name, self.address, self.product, self.workers, self.status)

    def show_info(self):
        print('Cайт: ' + self.url, 'адреса: ' + self.address)

    def make_order(self):
        print('Ваше замовлення буде доставлено: '+self.delivery, 'сплачено: '+self.payment)


book_shop = Shop('Світанок', 'Rivne', 'svitanok.com', 'book', 5, 'Nova Poshta', 'Card')
book_shop.show_info()
book_shop.make_order()
