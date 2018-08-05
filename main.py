#!/usr/local/bin/python3

"""
MIT License

Copyright (c) 2018 Sebastian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import random
from datetime import datetime
from tkinter import *


class MainWidget:
    r1 = 0
    r2 = 0
    correct = 0
    wrong = 0
    time = datetime.now()
    infoWidget = None
    sign = ":"
    random_sign = True
    last_question = ""

    def __init__(self):
        self.root = Tk()
        self.root.title("Einmaleins")
        self.root.geometry('{}x{}'.format(400, 400))
        self.root.config(bg='#FFFFFF')
        self.root.resizable(width=False, height=False)

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.more_menu = Menu(self.menu)
        self.mode_menu = Menu(self.menu)
        self.menu.add_cascade(label="Mehr", menu=self.more_menu)
        self.menu.add_cascade(label="Aufgaben", menu=self.mode_menu)

        self.more_menu.add_command(label="Info", command=self.show_info)
        self.more_menu.add_command(label="Beenden", command=sys.exit)

        self.mode_menu.add_command(label="Malnehmen", command=self.set_multiply)
        self.mode_menu.add_command(label="Teilen", command=self.set_divide)
        self.mode_menu.add_command(label="Plus", command=self.set_plus)
        self.mode_menu.add_command(label="Mnis", command=self.set_minus)
        self.mode_menu.add_command(label="Gemischte Aufgaben", command=self.set_random)

        self.score_label = Label(self.root)
        self.score_label.config(bg='#FFFFFF')
        self.score_label.pack(pady=15)

        self.question_label = Label(self.root)
        self.question_label.config(bg='#E95420', fg='#FFFFFF', font=("Sans", 16), height=3)
        self.question_label.pack(pady=15, fill=X)

        submit_frame = Frame(self.root)
        submit_frame.config(bg='#FFFFFF')
        submit_frame.pack(padx=30, pady=15)

        self.entry_field = Entry(submit_frame)
        self.entry_field.pack(side=LEFT, padx=15, pady=15, anchor=E)
        self.entry_field.config(bg='#FFFFFF', font=("Sans", 16), borderwidth=1, relief="flat", width=10, justify='center')
        self.entry_field.bind("<Return>", self.answer)

        self.submit_button = Button(submit_frame)
        self.submit_button.pack(side=RIGHT, padx=15, pady=15, anchor=W)
        self.submit_button.config(text='Antworten', bg='#FFFFFF', font=("Sans", 11), borderwidth=1,
                                  relief="flat", width=7, command=self.answer)

        self.answer_label = Label(self.root)
        self.answer_label.config(bg='#FFFFFF')
        self.answer_label.pack(pady=15)
        self.update_menu()
        self.update()
        self.root.mainloop()

    def update(self):
        if self.random_sign:
            self.sign = ("x", ":", "+", "-")[random.randint(0, 3)]
        if self.sign == "x" or self.sign == ":":
            r1n = random.randint(1, 10)
            r2n = random.randint(1, 10)
        elif self.sign == "+" or self.sign == "-":
            r1n = random.randint(0, 100)
            r2n = random.randint(0, 100)
        else:
            raise Exception("Unknown operator" + self.sign)

        if self.sign == "x":
            self.r1 = r1n
            self.r2 = r2n
        elif self.sign == ":":
            self.r1 = r1n * r2n
            self.r2 = r2n
        elif self.sign == "+":
            r12 = [max(r1n, r2n) - min(r1n, r2n), min(r1n, r2n)]
            random.shuffle(r12)
            self.r1 = r12[0]
            self.r2 = r12[1]
        elif self.sign == "-":
            self.r1 = max(r1n, r2n)
            self.r2 = min(r1n, r2n)
        else:
            raise Exception("Unknown operator" + self.sign)

        question_text = "Was ist {}{}{} ?".format(self.r1, self.sign, self.r2)
        if question_text == self.last_question:
            self.update()

        self.last_question = question_text
        self.question_label.config(text=question_text)
        self.score_label.config(text="Richtig: {} Falsch: {}".format(self.correct, self.wrong))
        self.time = datetime.now()

    def answer(self, event=None):
        answer = str(self.entry_field.get()).strip()
        if answer == "":
            return
        now = datetime.now()
        answer_time_seconds = (now - self.time).seconds
        if answer == str(self.solve()):
            self.answer_label.config(
                text="Toll! {}{}{} ist {}. Das war richtig.\n\nDu hast {} Sekunden gebraucht.".format(str(self.r1),
                                                                                                      self.sign,
                                                                                                      str(self.r2),
                                                                                                      str(self.solve()),
                                                                                                      str(answer_time_seconds)))
            self.correct += 1
        else:
            self.answer_label.config(
                text="Schade. {}{}{} ist {} und nicht {}.".format(str(self.r1), self.sign, str(self.r2), str(self.solve()), answer))
            self.wrong += 1

        self.entry_field.delete(0, 'end')
        self.entry_field.focus()
        self.update()

    def show_info(self):
        if self.infoWidget is None:
            self.infoWidget = Toplevel(self.root)
            self.infoWidget.wm_title("Info")
            self.infoWidget.geometry('{}x{}'.format(400, 400))
            self.infoWidget.protocol("WM_DELETE_WINDOW", self.delete_info)
            self.infoWidget.resizable(width=False, height=False)
            info_label = Label(self.infoWidget, text="\nEin mal Eins Lernprogramm\nSebastian Schlegel 2018\nFür meine Maja\n")
            info_label.pack()
            licence_field = Text(self.infoWidget)
            scroll = Scrollbar(self.infoWidget, command=licence_field.yview)
            scroll.pack(side=RIGHT, fill=Y)
            licence_field.configure(yscrollcommand=scroll.set)
            licence_field.pack(side=LEFT, fill=Y)
            licence_field.insert(END, __doc__)
        else:
            self.infoWidget.focus()

    def delete_info(self):
        if self.infoWidget is not None:
            self.infoWidget.destroy()
            self.infoWidget = None

    def solve(self):
        if self.sign == "x":
            return self.r1 * self.r2
        elif self.sign == ":":
            return int(self.r1 / self.r2)
        elif self.sign == "+":
            return self.r1 + self.r2
        elif self.sign == "-":
            return self.r1 - self.r2
        else:
            raise Exception("Unknown operator" + self.sign)

    def set_multiply(self):
        self.sign = "x"
        self.random_sign = False
        self.update_menu()
        self.update()

    def set_divide(self):
        self.sign = ":"
        self.random_sign = False
        self.update_menu()
        self.update()

    def set_plus(self):
        self.sign = "+"
        self.random_sign = False
        self.update_menu()
        self.update()

    def set_minus(self):
        self.sign = "-"
        self.random_sign = False
        self.update_menu()
        self.update()

    def set_random(self):
        self.random_sign = True
        self.update_menu()
        self.update()

    def update_menu(self):
        if self.sign == "x":
            self.mode_menu.entryconfigure(1, label="✓ Malnehmen")
            self.mode_menu.entryconfigure(2, label="Teilen")
            self.mode_menu.entryconfigure(3, label="Plus")
            self.mode_menu.entryconfigure(4, label="Minus")
            self.mode_menu.entryconfigure(5, label="Gemischte Aufgaben")
        elif self.sign == ":":
            self.mode_menu.entryconfigure(1, label="Malnehmen")
            self.mode_menu.entryconfigure(2, label="✓ Teilen")
            self.mode_menu.entryconfigure(3, label="Plus")
            self.mode_menu.entryconfigure(4, label="Minus")
            self.mode_menu.entryconfigure(5, label="Gemischte Aufgaben")
        elif self.sign == "+":
            self.mode_menu.entryconfigure(1, label="Malnehmen")
            self.mode_menu.entryconfigure(2, label="Teilen")
            self.mode_menu.entryconfigure(3, label="✓ Plus")
            self.mode_menu.entryconfigure(4, label="Minus")
            self.mode_menu.entryconfigure(5, label="Gemischte Aufgaben")
        elif self.sign == "-":
            self.mode_menu.entryconfigure(1, label="Malnehmen")
            self.mode_menu.entryconfigure(2, label="Teilen")
            self.mode_menu.entryconfigure(3, label="Plus")
            self.mode_menu.entryconfigure(4, label="✓ Minus")
            self.mode_menu.entryconfigure(5, label="Gemischte Aufgaben")
        if self.random_sign:
            self.mode_menu.entryconfigure(1, label="Malnehmen")
            self.mode_menu.entryconfigure(2, label="Teilen")
            self.mode_menu.entryconfigure(3, label="Plus")
            self.mode_menu.entryconfigure(4, label="Minus")
            self.mode_menu.entryconfigure(5, label="✓ Gemischte Aufgaben")


if __name__ == '__main__':
    w = MainWidget()
