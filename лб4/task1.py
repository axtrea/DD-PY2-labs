import doctest

class Door:
    def __init__(self, material: str, condition: str):
        """
        Создание объекта "Дверь"
        :param material: материал двери
        :param condition: открытое или закрытое состояние двери
        Примеры:
        >>> door = Door('wood', 'closed')
        """
        if not isinstance(material, str):
            raise TypeError
        self.material = material
        if not isinstance(condition, str):
            raise TypeError
        self.condition = condition

    def open_door(self) -> str:
        """
        Меняет состояние двери на открытое, если дверь закрыта.
        :return: Открытое состояние двери
        Пример:
        >>> door = Door('wood', 'closed')
        >>> door.open_door()
        """
        ...

    def close_door(self) -> str:
        """
        Меняет состояние двери на закрытое, если дверь открыта.
        :return: Закрытое состояние
        Пример:
        >>> door = Door('wood', 'opened')
        >>> door.close_door()
        """
        ...

    def __str__(self) -> str:
        return f"Состояние {self.condition}. Материал {self.material}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(condition={self.condition!r}, material = {self.material!r})"


class VaultDoor(Door):
    def __init__(self, material: str, condition: str, password: str):
        """
        Создание объекта "Дверь от хранилища"
        :param material: материал двери
        :param condition: состояние двери
        :param password: пароль от двери
        Пример:
        >>> vaultdoor = VaultDoor('steel', 'closed', '175237')
        """
        super().__init__(material, condition)
        if not isinstance(password, str):
            raise TypeError
        self.password = password

    def open_door(self, password: str) -> str:
        """
        Открывает дверь, если закрыта. На вход принимает пароль, если пароль совпадает со значением соответствующего аргумента объекта, то меняет состояние двери на открытое.
        :param password: для окрытия двери требуется ввести пароль
        :return: меняет состояние двери на открытое
        Пример:
        >>> vaultdoor = VaultDoor('steel', 'closed', '175237')
        >>> vaultdoor.open_door('175237')
        """
        ...

    def __str__(self) -> str:
        return f"Состояние {self.condition}. Материал {self.material}. Пароль {self.password}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(condition={self.condition!r}, material = {self.material!r}, password = {self.password})"


if __name__ == "__main__":
    doctest.testmod()
    pass

