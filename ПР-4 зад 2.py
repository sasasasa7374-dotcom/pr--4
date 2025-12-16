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
        return "пишу код"
    
    def rest(self):
        return "пью кофе"


class Designer(Worker):
    def work(self):
        return "рисую дизайн"
    
    def rest(self):
        return "рисую для себя"