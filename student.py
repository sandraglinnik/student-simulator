class Student:
    def __init__(self):
        self.activity = ""
        self.money = 0
        self.performance = 5
        self.energy = 100
        self.fullness = 100
        self.recreation = 100
        self.hygiene = 100
        self.alive = ""

    def eat(self):
        if self.money <= 120:
            self.money = 0
            self.alive = "Вы на мели"
        else:
            self.money -= 120
            self.fullness = min(100, self.fullness + 40)
            self.activity = ""

    def sleep(self):
        self.energy = min(100, self.energy + 50)
        self.activity = ""

    def study(self):
        self.performance = min(10, self.performance + 0.5)
        self.activity = ""

    def shower(self):
        self.hygiene = 100
        self.activity = ""

    def play_games(self):
        self.recreation = min(100, self.recreation + 50)
        self.activity = ""

    def get_money(self):
        self.money += 12000

    def get_activity(self):
        return self.activity

    def get_statement(self):
        return [int(self.money), int(self.performance), int(self.energy), int(self.fullness), int(self.recreation), int(self.hygiene)]

    def set_activity(self, action):
        self.activity = action

    def update(self):
        if self.activity != "Ботает":
            if self.performance <= 2 + 1/200:
                self.performance = 2
                self.alive = "Вас отчислили"
            else:
                self.performance -= 1/200
        if self.activity != "Спит":
            if self.energy <= 0.4:
                self.energy = 0
                self.alive = "Вы умерли от переутомления"
            else:
                self.energy -= 0.4
        if self.activity != "Ест":
            if self.fullness <= 0.4:
                self.fullness = 0
                self.alive = "Вы умерли от голода"
            else:
                self.fullness -= 0.4
        if self.activity != "Играет":
            if self.recreation <= 0.2:
                self.recreation = 0
                self.alive = "Вы покончили жизнь самоубийством вследствии депрессии"
            else:
                self.recreation -= 0.2

        if self.activity != "Принимает душ":
            if self.hygiene <= 0.2:
                self.hygiene = 0
                self.alive = "Вас выгнали из общаги из-за неприятного запаха"
            else:
                self.hygiene -= 0.2

    def get_alive(self):
        return self.alive
