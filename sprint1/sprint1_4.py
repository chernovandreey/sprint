from abc import ABC, abstractmethod


class Phone(ABC):
    def __init__(self, size, color, camera, weight, price):
        self.size = size
        self.color = color
        self.camera = camera
        self.weight = weight
        self.price = price

    @abstractmethod
    def unlock(self):
        pass

    @abstractmethod
    def message(self):
        pass

    @abstractmethod
    def phone_info(self):
        pass


class Iphone(Phone):
    def __init__(self, size, color, camera, weight, price):
        super().__init__(size, color, camera, weight, price)


class Android(Phone):
    def __init__(self, size, color, camera, weight, price):
        super().__init__(size, color, camera, weight, price)


class Iphone15(Iphone):
    def __init__(self, size, color, camera, weight, price, country, _serial_number):
        super().__init__(size, color, camera, weight, price)
        self.country = country
        self._serial_number = _serial_number

    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, new_num):
        if len(new_num) == 8:
            self._serial_number = new_num
        else:
            print("Номер не корректен")

    def unlock(self):
        print("Разблокирован")
        print("Разблокировано по фейс айди")

    def message(self):
        print("Отправляю сообщение с iPhone")

    def phone_info(self):
        print(
            f"Телефон iPhone 15 размером {self.size} дюймов, цвет {self.color}. "
            f"У него {self.camera} мегапикселей. Весит {self.weight} грамм и стоит {self.price} рублей. "
            f"Произведен в {self.country}. Серийный номер: {self.serial_number}")


class Iphone4(Iphone):
    def __init__(self, size, color, camera, weight, price):
        super().__init__(size, color, camera, weight, price)

    def unlock(self):
        print("Разблокирован")
        print("Разблокирован обычным способом")

    def message(self):
        print("Отправляю сообщение с iPhone 4")

    def phone_info(self):
        print(
            f"Телефон iPhone 4 размером {self.size} дюймов, цвет {self.color}. "
            f"У него {self.camera} мегапикселей. Весит {self.weight} грамм и стоит {self.price} рублей.")


p1 = Iphone15(10, "red", 21, 13, 1000, "UAE", "12345678")
p1.unlock()
p2 = Iphone4(10, "red", 10, 13, 1000)
p2.unlock()
p1.message()
p2.message()
p1.phone_info()
p2.phone_info()
p1.serial_number()
