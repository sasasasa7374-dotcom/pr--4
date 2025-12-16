from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def rest(self):
        pass


class Programmer(Worker):
    def work(self):
        return "Написание кода"

    def rest(self):
        return "делаю перерыв на кофе"


class Designer(Worker): 
    def work(self):
        return "создаем макеты"

    def rest(self):
        return "Рисуем для удовольствия"
