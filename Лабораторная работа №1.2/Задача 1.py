# TODO Написать 3 класса с документацией и аннотацией типов
class Final_mark:
    def __init__(self, attendance: int, points: float):
        """
        Создание и подготовка к работе объекта "Итоговая отметка"
        :param attendance: Посещаемость
        :param points: Баллы
        """
        if not isinstance(attendance, int):
            raise TypeError("Посещаемость должна быть типа int")
        if attendance <= 7:
            raise ValueError("Посещаемость должна быть не меньше 8")
        self.attendance = attendance
        if not isinstance(points, float):
            raise TypeError("Баллы должны быть типа float")
        if points <= 0:
            raise ValueError("Баллы должны быть положительным числом")
        self.points = points
    def are_there_enough_points(self, needed_points: float) -> bool:
        """
        Функция, которая проверяет, достаточно ли баллов для формирования итоговой отметки
        :param needed_points: Необходимое количество баллов
        :return: Достаточно ли баллов для формирования итоговой отметки
        """
        if not isinstance(needed_points, float):
            raise TypeError("Необходимое количество баллов должно быть типа float")
        if needed_points < 0:
            raise ValueError("Необходимое количество баллов должно положительным числом")
        ...
    def add_points(self, added_points: float) -> None:
        """
        Функция, добавляющая баллы
        :param added_points: Дополнительные баллы
        """
        if not isinstance(added_points, float):
            raise TypeError("Дополнительные баллы должны быть типа float")
        if added_points < 0:
            raise ValueError("Дполнительные баллы должны положительным числом")
        ...

class TV_show:
    def __init__(self, releases: int, topic: str):
        """
        Создание и подготовка к работе объекта "ТВ-шоу"
        :param releases: Количество выпусков
        :param topic: Тематика
        """
        if not isinstance(releases, int):
            raise TypeError("Количество выпусков должно быть типа int")
        if releases <= 0:
            raise ValueError("Количество выпусков должно быть больше 0")
        self.releases = releases
        if not isinstance(topic, str):
            raise TypeError("Тематика должна быть типа str")
        self.topic = topic
    def check_releases(self, needed_releases: float) -> bool:
        """
        Функция, которая проверяет, больше ли количество выпусков, чем требуемое
        :param needed_releases: Необходимое количество выпусков
        :return: Больше ли количество выпусков, чем требуемое
        """
        if not isinstance(needed_releases, int):
            raise TypeError("Необходимое количество выпусков должно быть типа int")
        if needed_releases <= 0:
            raise ValueError("Необходимое количество выпусков должно быть больше 0")
        ...
    def check_topic(self, list1: list) -> bool:
        """
        Функция, проверяющая, принадлежит ли тематика списку
        :param list1: Список тем
        :return: Принадлежит ли тематика списку
        """
        if not isinstance(list1, list):
            raise TypeError("Список тем должен быть типа list")
        ...

class Workout:
    def __init__(self, number_of_approaches: int, repetitions: int):
        """
        Создание и подготовка к работе объекта "Тренировка"
        :param number_of_approaches: Количество подходов
        :param repetitions: Количество повторений
        """
        if not isinstance(number_of_approaches, int):
            raise TypeError("Количество подходов должно быть типа int")
        if number_of_approaches < 1:
            raise ValueError("Количество подходов должно быть больше или равно 1")
        self.number_of_approaches = number_of_approaches
        if not isinstance(repetitions, int):
            raise TypeError("Количество повторений должно быть типа int")
        if repetitions <= 0:
            raise ValueError("Количество повторений должно быть положительным числом")
        self.repetitions = repetitions

    def more_approaches_or_not(self, needed_number_of_approaches: int) -> bool:
        """
        Функция, которая проверяет, больше ли количество подходов, чем требуемое
        :param needed_number_of_approaches: Необходимое количество подходов
        :return: Больше ли количество подходов, чем требуемое
        """
        if not isinstance(needed_number_of_approaches, int):
            raise TypeError("Необходимое количество подходов должно быть типа int")
        if needed_number_of_approaches <= 0:
            raise ValueError("Необходимое количество подходов должно быть положительным числом")
        ...

    def add_repetitions(self, added_repetitions: int) -> None:
        """
        Функция, увеличивающая количество повторений
        :param added_repetitions: Добавляемые повторения
        """
        if not isinstance(added_repetitions, int):
            raise TypeError("Добавляемые повторения должны быть типа int")
        if added_repetitions <= 0:
            raise ValueError("Добавляемые повторения должны быть положительным числом")
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
