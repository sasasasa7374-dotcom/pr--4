class Worker:
    def work(self):
        pass
    
    def rest(self):
        pass


class Programmer(Worker):
    def work(self):
        return "пишу код"

    def rest(self):
        return "делаю перерыв на кофе"


class Designer(Worker):
    def work(self):
        return "создаю Графический дизайн"

    def rest(self):
        return "создаю дизайн для удовольствия"