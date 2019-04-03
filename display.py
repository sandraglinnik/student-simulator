from tkinter import *
from student import Student
from events import Events

class Display:
    def __init__(self):
        self.root = Tk()
        self.events_label = Label(self.root, text="Нажмите Enter, чтобы начать")
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
            self.events_label.after(100, self.update)

    def update(self):
        if self.student.get_alive() == "":
            self.events_label.after(100, self.update)
            if self.events.salary():
                self.student.get_money()
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
