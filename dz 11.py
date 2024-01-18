class Product:
    def __init__(self, name, store, price):
        self.name = name
        self.store = store
        self.price = price

class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product(self, index):
        if index >= 0 and index < len(self.products):
            return self.products[index]
        else:
            return None

    def get_product_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def sort_name(self):
        self.products.sort(key=lambda x: x.name)

    def sort_store(self):
        self.products.sort(key=lambda x: x.store)

    def sort_price(self):
        self.products.sort(key=lambda x: x.price)

    def __add__(self, other):
        total_price = sum([product.price for product in self.products])
        total_price += sum([product.price for product in other.products])
        return total_price


product1 = Product("Телевизор", "Магазин 1", 10000)
product2 = Product("Холодильник", "Магазин 2", 12000)
product3 = Product("Смартфон", "Магазин 1", 15000)

warehouse = Warehouse()

warehouse.add_product(product1)
warehouse.add_product(product2)
warehouse.add_product(product3)

print(warehouse.get_product(0).name)

print(warehouse.get_product_name("Смартфон").store)

warehouse.sort_name()
for product in warehouse.products:
    print(product.name)

warehouse.sort_store()
for product in warehouse.products:
    print(product.store)

warehouse.sort_price()
for product in warehouse.products:
    print(product.price)

warehouse2 = Warehouse()
warehouse2.add_product(Product("Ноутбук","Магазин 3",20000))
print(warehouse + warehouse2)


class BeeEl:
    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def Fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False

    def Trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def Eat(self, meal, value):
        if meal == 'nectar':
            self.elephant = max(0, self.elephant - value)
            self.bee = min(100, self.bee + value)
        elif meal == "grass":
            self.elephant = min(100, self.elephant + value)
            self.bee = max(0, self.bee - value)

beel = BeeEl(50, 40)

print(beel.Fly())
print(beel.Trumpet())
beel.Eat("nectar", 30)
print(beel.bee)
print(beel.elephant)


сlass Bus:

    def __init__(self, max_seats, max_speed):
        self.speed = 0
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passenger_names = []
        self.has_free_seats = True
        self.seat_map = {}


    def boarding(self, passenger_names):
        if not self.has_free_seats:
            print("Автобус полностью заполнен")
            return

        for name in passenger_names:
            if len(self.passenger_names) >= self.max_seats:
                self.has_free_seats = False
                print(f"Автобус заполнен, не удалось посадить {name}")
                break

            self.passenger_names.append(name)
            self.seat_map[name] = len(self.passenger_names)

    def disembarking(self, passenger_names):
        for name in passenger_names:
            if name in self.passenger_names:
                self.passenger_names.remove(name)
                del self.seat_map[name]
            else:
                print(f"Пассажира с фамилией {name} нет в автобусе")

        self.has_free_seats = len(self.passenger_names) < self.max_seats

    def increase_speed(self, value):
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            print("Превышена максимальная скорость автобуса")

    def decrease_speed(self, value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            print("Скорость не может быть отрицательной")

    def __contains__(self, name):
        return name in self.passenger_names

    def __iadd__(self, name):
        self.boarding([name])
        return self

    def __isub__(self, name):
        self.disembarking([name])
        return self

bus = Bus(50, 80)
bus.boarding(["Ivanov", "Petrov", "Sidorov"])
print("Пассажиры в автобусе:", bus.passenger_names)

bus += "Smith"  # Сокращенная запись для посадки пассажира
print("Пассажиры в автобусе:", bus.passenger_names)

if "Ivanov" in bus:  # Проверка наличия пассажира
    print("Пассажир Ivanov есть в автобусе")

bus.disembarking(["Petrov", "Smith"])
print("Пассажиры в автобусе:", bus.passenger_names)

bus -= "Ivanov"  # Сокращенная запись для высадки пассажира
print("Пассажиры в автобусе:", bus.passenger_names)

bus.increase_speed(50)
print("Скорость автобуса:", bus.speed)

bus.decrease_speed(30)
print("Скорость автобуса:", bus.speed)