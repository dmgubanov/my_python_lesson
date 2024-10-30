# Класс Product, представляющий товар
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

# Класс Customer, представляющий клиента
class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"Customer(name={self.name}, orders={len(self.orders)})"

    def __repr__(self):
        return self.__str__()

# Класс Order, представляющий заказ
class Order:
    total_orders = 0
    total_amount = 0

    def __init__(self, products):
        self.products = products
        Order.total_orders += 1
        Order.total_amount += self.calculate_total()

    def calculate_total(self):
        return sum(product.price for product in self.products)

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders

    @classmethod
    def get_total_amount(cls):
        return cls.total_amount

    def __str__(self):
        return f"Order(products={[str(product) for product in self.products]}, total={self.calculate_total()})"

    def __repr__(self):
        return self.__str__()

# Класс Discount для применения скидок
class Discount:
    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def apply_discount(price, discount_percent):
        return price * (1 - discount_percent / 100)

    def __str__(self):
        return f"Discount(description={self.description}, discount_percent={self.discount_percent})"

    def __repr__(self):
        return self.__str__()

# Пример использования системы интернет-магазина
# Создаем продукты
product1 = Product("Laptop", 1200)
product2 = Product("Smartphone", 800)
product3 = Product("Headphones", 150)
product4 = Product("Tablet", 400)

# Создаем клиентов
customer1 = Customer("Elena")
customer2 = Customer("Mihail")
customer3 = Customer("Vladimir")

# Создаем заказы
order1 = Order([product1, product3])
order2 = Order([product2, product4])
order3 = Order([product1, product2])

# Добавляем заказы к клиентам
customer1.add_order(order1)
customer2.add_order(order2)
customer3.add_order(order3)

# Применяем скидки
season_discount = Discount("Seasonal Discount", 10)
promo_discount = Discount("Promo Code Discount", 15)

# Применение скидки для клиентов
order1_total_with_season_discount = Discount.apply_discount(order1.calculate_total(), season_discount.discount_percent)
order2_total_with_promo_discount = Discount.apply_discount(order2.calculate_total(), promo_discount.discount_percent)

# Вывод информации о клиентах, заказах и продуктах
print(customer1)
for order in customer1.orders:
    print(order)
    print(f"Total with seasonal discount: {order1_total_with_season_discount}")

print(customer2)
for order in customer2.orders:
    print(order)
    print(f"Total with promo discount: {order2_total_with_promo_discount}")

print(customer3)
for order in customer3.orders:
    print(order)
    print(f"Total without discount: {order.calculate_total()}")

# Общая информация о всех заказах
print("Total orders:", Order.get_total_orders())
print("Total amount of all orders:", Order.get_total_amount())
