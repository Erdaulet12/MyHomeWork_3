"""task_1.py"""


class MainClass:
    """Класс, который содержит приватное текстовое поле и методы для его присваивания и вывода."""

    def __init__(self, text):
        """Инициализирует объект класса с заданным текстом."""
        self.__text = text

    def set_text(self, text=None):
        """Присваивает значение полю, если передан аргумент, или запрашивает его у пользователя, если нет."""
        if text is None:
            self.__text = input("Введите текст: ")
        else:
            self.__text = text

    def get_text(self):
        """Выводит значение поля."""
        print(self.__text)


class SubClass(MainClass):
    """Класс-потомок, который содержит числовое поле и наследует текстовое поле и методы от суперкласса."""

    def __init__(self, text, number):
        """Инициализирует объект класса-потомка с заданным текстом и числом."""
        super().__init__(text)
        self.number = number

    def get_number(self):
        """Выводит значение числового поля."""
        print(self.number)


if __name__ == "__main__":
    obj1 = MainClass("Привет")
    obj1.get_text()
    obj1.set_text("Пока")
    obj1.get_text()

    obj2 = SubClass("Hello", 42)
    obj2.get_text()
    obj2.get_number()
