class Worker(self):
    def work(self):
        pass
    def rest(self):
        pass
        
class Programmer(Worker):
    def work(self):
        return "Написание кода"

    def rest(self):
        return "делаю перерыв на кофе"

class Designer(Worker): 
    def work(self):
        return "создаем Графический дизайн"

    def rest(self):
        return "создаем дизайн для удовольствия"
