# Розширити функціонал класу Shop добавивши у нього розділ знижок

class Discount:
    def __init__(self, name, amount, time):
        self.name = name
        self.amount = amount
        self.time = time

    def show(self):
        print(f'{self.name} з {self.amount}% до {self.time}')


class Shop:
    def __init__(self, name, address, product, workers, discount_list):
        self.name = name
        self.address = address
        self.product = product
        self.workers = workers
        self.status = True
        self.discounts = discount_list

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

    def all_discount(self):
        if self.status:
            for discount in self.discounts:
                discount.show()
        else:
            print(None)


book1 = Discount('Гаррі Поттер', 15, '08.05.2022')
book2 = Discount('Маленький принц', 9.75, '22.05.2022')
book3 = Discount('Трудова книжка', 50, '01.05.2022')

dis_list = [book1, book2, book3]

shop = Shop('Світанок', 'Rivne', 'book', 5, dis_list)
shop.all_discount()
