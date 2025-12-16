class Player:
    def __init__(self):
        self.__xp = 0
        
    def raise_score(self, amount):
        if amount < 0:
            print("Ошибка: нельзя добавить отрицательное число очков")
            return
        
        self.__xp += amount
        print(f"Добавлено {amount} очков. Теперь у вас {self.__xp} очков")
    
    def take_score(self, amount):
        if amount < 0:
            print("Ошибка: нельзя вычесть отрицательное число очков")
            return
            
        if amount > self.__xp:
            print(f"Ошибка: у вас только {self.__xp} очков, а хотите вычесть {amount}")
            return
        
        self.__xp -= amount
        print(f"Вычтено {amount} очков. Осталось {self.__xp} очков")
