# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Cube:
    def __init__(self, volume: float, material: str):
        """
        Создание и подготовка к работе объекта "Куб"
        :param volume: Объем куба
        :param material: материал куба
        Примеры:
        >>> cube = Cube(50, "wood")  # инициализация экземпляра класса
        """
        if not isinstance(volume, (int, float)):
            raise TypeError
        if volume <= 0:
            raise ValueError
        self.volume = volume

        if not isinstance(material, str):
            raise TypeError
        self.material = material
    def change_material(self, material):
        """
        Изменение материала куба
        :param material: новый материал
        :return: новый материал куба
         Примеры:
        >>> cube1 = Cube(500, "wood")
        >>> cube1.change_material('steel')
        """
        if not isinstance(material, str):
            raise TypeError
        ...
    def change_volume(self, volume):
        """
        Изменение объема куба
        :param volume: новый объем
        :return: новый объем куба
         Примеры:
         >>> cube1 = Cube(500, "wood")
         >>> cube1.change_volume(100)
         """
        if not isinstance(volume, (int, float)):
            raise TypeError
        if volume < 0:
            raise ValueError("Объем должен быть положительным")
        ...
class Gate:
    def __init__(self, size: float, open_condition: bool):
        """
        Создание и подготовка к работе объекта "Ворота"
        :param size: Размер ворот
        :param open_condition: Ворота открыты
        Примеры:
        >>> gate1 = Gate(100, True)
        """
        if not isinstance(size, (int, float)):
            raise TypeError
        if size <= 0:
            raise ValueError
        self.size = size

        if not isinstance(open_condition, bool):
            raise TypeError
        self.open_condition = open_condition
    def is_open_gate(self):
        """
    Проверяет, открыты ли ворота
    :return: Открыты ли ворота
        Прмеры:
        >>> gate1 = Gate(125, False)
        >>> gate1.is_open_gate()
        """
    ...
    def is_bigger_than_250(self):
        """
    Проверяет, больше ли ворота размера 250
    :return: Больше ли размер ворот 250
        Прмеры:
        >>> gate1 = Gate(271, False)
        >>> gate1.is_bigger_than_250()
        """
    ...
class Backpack:
    def __init__(self, capacity: float, occupied_space: float):
        """
        Создание и подготовка к работе объекта "Рюкзак"
        :param capacity: Вместимость рюкзака
        :param occupied_space: занятое место в рюкзаке
        Примеры:
        >>> backpack = Backpack(100, 30)  # инициализация экземпляра класса
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError
        if capacity <= 0:
            raise ValueError
        self.capacity = capacity
        if not isinstance(occupied_space, (int, float)):
            raise TypeError
        if occupied_space < 0 or occupied_space > capacity:
            raise ValueError
        self.occupied_space = occupied_space
    def free_space(self):
        """
        Вычисляет свободное место в рюкзаке
        :return: Объем свободного места
        Прмеры:
        >>> backpack1 = Backpack(100, 70)
        >>> backpack1.free_space()
        """
        ...
    def is_backpack_full(self):
        """
        Проверяет, полон ли рюкзак
        :return: Полон ли рюкзак
        Примеры:
        >>> backpack1 = Backpack(100, 100)
        >>> backpack1.is_backpack_full()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
