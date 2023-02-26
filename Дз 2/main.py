class AK:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def information(self):
        print(f"this is ak- {self.model}, it was created in {self.year}")
class AR:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def information(self):
        print(f"this is ar- {self.model}, it was created in {self.year}")
class ArUpgraded(AR):
    def __init__(self, model, year):
        self.model=model
        self.year=year
    def shoot(self):
        print("ra-ta-ta")
ak47=AK("47",1970)
ar15=ArUpgraded("15",1980)
for guns in (ak47,ar15): #здесь сразу и полиморфизм и наследование (Полиморфизм - при одинаковых названиях метода information() можно вызвать оба метода по общей переменной,
                        # Наследование - метод ArUpgraded обладает родительским методом information(), а также новым методом потомка - shoot())
    guns.information()
ar15.shoot()