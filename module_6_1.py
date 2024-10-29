class Animal:
    alive = True       # Определил атрибуты царства
    fed = False
    def __init__(self, name): # Создал параметры объекта
        self.name = name


class Plant:
    edible = False               # Определил атрибуты
    def __init__(self, name):           # Создал параметры объекта
        self.edible = name


class Mammal(Animal):
    def eat(self, food):       # Пункт приема объектов другого класса из другого царства
        if food.edible is True:                         # Условие природы при котором класс выживает
            print(f"{self.name} съел {food.name}")
            Animal.fed = True
        if food.edible is False:
            print(f"{self.name} не стал есть {food.name}")  # Условие природы при котором класс погибает(((
            Animal.alive = False


class Predator(Animal):
    def eat(self, food):    # Пункт приема объектов другого класса из другого царства
        if food.edible is True:
            print(f"{self.name} съел {food.name}")      # Условие природы при котором класс выживает
            Animal.fed = True
        if food.edible is False:
            print(f"{self.name} не стал есть {food.name}")      # Условие природы при котором класс погибает(((
            Animal.alive = False

class Flower(Plant):
    def __init__(self, name):   # Один из видов класса
        self.name = name
        self.edible = False

class Fruit(Plant):
    def __init__(self, name):    # Другой один из видов класса
        self.name = name
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)