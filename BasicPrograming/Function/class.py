class Animal(object):
    def __init__(self, name):
        self.name = name
        print(self.name)


animal = Animal("koki")


# property setter


class Car(object):
    def __init__(self, model=None):
        self.model = model


class AdvancedCar(Car):
    def __init__(self, model="SUV", enable_auto_run=False, password=""):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run
        self.password = password

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.password == "123":
            self.__enable_auto_run = is_enable


advanced_car = AdvancedCar("SUV")
print(advanced_car.enable_auto_run)


class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print("ok")
        else:
            raise Exception("No drive")


# __eq__


class Word(object):
    def __init__(self, text):
        self.text = text


w = Word("test")
w2 = Word("test")
print(w == w2)


class Word2(object):
    def __init__(self, text):
        self.text = text

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()


w = Word("test")
w2 = Word("test")
print(w == w2)
