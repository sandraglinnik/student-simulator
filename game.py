from tkinter import *


class Student:
    def __init__(self):
        self.activity = ""
        self.money = 0
        self.perfomance = 5
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
            if self.fullness <= 40:
                self.fullness += 60
            else:
                self.fullness = 100
            self.activity = ""

    def sleep(self):
        if self.energy <= 50:
            self.energy += 50
        else:
            self.energy = 100
        self.activity = ""

    def study(self):
        if self.perfomance <= 9:
            self.perfomance += 0.5
        self.activity = ""

    def shower(self):
        self.hygiene = 100
        self.activity = ""

    def play_games(self):
        if self.recreation <= 50:
            self.recreation += 50
        else:
            self.recreation = 100
        self.activity = ""

    def get_money(self):
        self.money += 12000

    def get_activity(self):
        return self.activity

    def get_statement(self):
        return [int(self.money), int(self.perfomance), int(self.energy), int(self.fullness), int(self.recreation), int(self.hygiene)]

    def set_activity(self, action):
        self.activity = action

    def update(self):
        if self.activity != "Ботает":
            if self.perfomance <= 1/20:
                self.perfomance = 0
                self.alive = "Вас отчислили"
            else:
                self.perfomance -= 1/20
        if self.activity != "Спит":
            if self.energy <= 4:
                self.energy = 0
                self.alive = "Вы умерли от переутомления"
            else:
                self.energy -= 4
        if self.activity != "Ест":
            if self.fullness <= 4:
                self.fullness = 0
                self.alive = "Вы умерли от голода"
            else:
                self.fullness -= 4
        if self.activity != "Играет":
            if self.recreation <= 2:
                self.recreation = 0
                self.alive = "Вы покончили жизнь самоубийством вследствии депрессии"
            else:
                self.recreation -= 2

        if self.activity != "Принимает душ":
            if self.hygiene <= 2:
                self.hygiene = 0
                self.alive = "Вас выгнали из общаги из-за неприятного запаха"
            else:
                self.hygiene -= 2

    def get_alive(self):
        return self.alive


class Events:
    def __init__(self):
        self.hours = 0
        self.special_event = ""
        self.started = False

    def update(self):
        self.hours += 1

    def get_day(self):
        return int(self.hours/24)

    def get_hours(self):
        return self.hours


class Display:
    def __init__(self):
        self.root = Tk()
        self.events_label = Label(self.root, text="День: 0")
        self.statement_label = Label(self.root, text = "Деньги: 12000    Успеваемость: 5        Бодрость: 100    Сытость: 100    Досуг: 100    Гигиена: 100" + '\n'*2)
        self.student_pic = PhotoImage(file = "student1.png")
        self.student_label = Label(self.root, image = self.student_pic)
        self.study_btn = Button(text = "Ботать", command = self.study)
        self.sleep_btn = Button(text = "Спать", command = self.sleep)
        self.eat_btn = Button(text = "Есть", command = self.eat)
        self.play_games_btn = Button(text = "Играть", command = self.play_games)
        self.shower_btn = Button(text = "Принять душ", command = self.shower)
        self.empty_label = Label(text='\n')
        self.student = Student()
        self.events = Events()
        self.started = False

    def create(self):
        self.root.title("DIHT student simulator")
        self.root.geometry("800x800")
        self.events_label.pack()
        self.statement_label.pack()
        self.study_btn.pack()
        self.sleep_btn.pack()
        self.eat_btn.pack()
        self.play_games_btn.pack()
        self.shower_btn.pack()
        self.empty_label.pack()
        self.student_label.pack()

    def start(self, event):
        if not self.started:
            self.started = True
            self.events_label.after(1000, self.update)

    def update(self):
        if self.student.get_alive() == "":
            if self.events.get_hours() % (30*24) == 0:
                self.student.get_money()
            self.events_label.after(1000, self.update)
            self.events.update()
            self.student.update()
            self.events_label.config(text = "День: {}    {}".format(self.events.get_day(), self.student.get_activity()))
            self.statement_label.config(text = "Деньги: {}    Успеваемость: {}        Бодрость: {}    Сытость: {}    Досуг: {}    Гигиена: {}".format(*self.student.get_statement()) + '\n'*2)
        else:
            self.events_label.config(text = "День: " + str(self.events.get_day()) + "    " + self.student.get_alive())

    def study(self):
        if self.student.get_activity() == "":
            self.study_btn.after(2000, self.student.study)
            self.student.set_activity("Ботает")

    def sleep(self):
        if self.student.get_activity() == "":
            self.sleep_btn.after(4000, self.student.sleep)
            self.student.set_activity("Спит")

    def eat(self):
        if self.student.get_activity() == "":
            self.eat_btn.after(1000, self.student.eat)
            self.student.set_activity("Ест")

    def play_games(self):
        if self.student.get_activity() == "":
            self.play_games_btn.after(2000, self.student.play_games)
            self.student.set_activity("Играет")

    def shower(self):
        if self.student.get_activity() == "":
            self.shower_btn.after(1000, self.student.shower)
            self.student.set_activity("Принимает душ")

    def play(self):
        self.create()
        self.root.bind('<Return>', self.start)
        self.root.mainloop()
        
        
d = Display()
d.play()
