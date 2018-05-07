#!/usr/local/bin/python3

"""
Copyright 2018 Sebastian Schlegel

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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

    def __init__(self):
        self.root = Tk()
        self.root.title("Einmaleins")
        self.root.geometry('{}x{}'.format(300, 200))
        self.root.resizable(width=False, height=False)

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.moreMenu = Menu(self.menu)
        self.modeMenu = Menu(self.menu)
        self.menu.add_cascade(label="Mehr", menu=self.moreMenu)
        self.menu.add_cascade(label="Aufgaben", menu=self.modeMenu)

        self.moreMenu.add_command(label="Info", command=self.show_info)
        self.moreMenu.add_command(label="Beenden", command=sys.exit)

        self.modeMenu.add_command(label="Malnehmen", command=self.set_multiply)
        self.modeMenu.add_command(label="Teilen", command=self.set_divide)
        self.modeMenu.add_command(label="Gemischte Aufgaben", command=self.set_random)

        Label(self.root).pack()

        self.scoreLabel = Label(self.root)
        self.scoreLabel.pack()

        Label(self.root).pack()

        self.questionLabel = Label(self.root)
        self.questionLabel.pack()

        self.entryField = Entry(self.root)
        self.entryField.pack()
        self.entryField.bind("<Return>", self.answer)

        Label(self.root).pack()
        self.answerLabel = Label(self.root)
        self.answerLabel.pack()
        self.update_menu()
        self.update()
        self.root.mainloop()

    def update(self):
        r1n = random.randint(1, 10)
        r2n = random.randint(1, 10)
        if self.r1 == r1n and self.r2 == r2n:
            self.update()
        else:
            if self.random_sign:
                self.sign = ("x", ":")[random.randint(0, 1)]
            if self.sign == "x":
                self.r1 = r1n
                self.r2 = r2n
            elif self.sign == ":":
                self.r1 = r1n * r2n
                self.r2 = r2n
            else:
                raise Exception("Unknown operator" + self.sign)

            self.questionLabel.config(text="Was ist {}{}{} ?".format(self.r1, self.sign, self.r2))
            self.scoreLabel.config(text="Richtig: {} Falsch: {}".format(self.correct, self.wrong))
            self.time = datetime.now()

    def answer(self, event):
        answer = str(self.entryField.get()).strip()
        if answer == "":
            return
        now = datetime.now()
        answer_time_seconds = (now - self.time).seconds
        if answer == str(self.solve()):
            self.answerLabel.config(
                text="Toll! {}{}{} ist {}. Das war richtig.\n\nDu hast {} Sekunden gebraucht.".format(str(self.r1),
                                                                                                      self.sign,
                                                                                                      str(self.r2),
                                                                                                      str(self.solve()),
                                                                                                      str(answer_time_seconds)))
            self.correct += 1
        else:
            self.answerLabel.config(
                text="Schade. {}{}{} ist {} und nicht {}.".format(str(self.r1), self.sign, str(self.r2), str(self.solve()), answer))
            self.wrong += 1

        self.entryField.delete(0, 'end')
        self.entryField.focus()
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

    def set_random(self):
        self.random_sign = True
        self.update_menu()
        self.update()

    def update_menu(self):
        if self.sign == "x":
            self.modeMenu.entryconfigure(1, label="✓ Malnehmen")
            self.modeMenu.entryconfigure(2, label="Teilen")
            self.modeMenu.entryconfigure(3, label="Gemischte Aufgaben")
        elif self.sign == ":":
            self.modeMenu.entryconfigure(1, label="Malnehmen")
            self.modeMenu.entryconfigure(2, label="✓ Teilen")
            self.modeMenu.entryconfigure(3, label="Gemischte Aufgaben")
        if self.random_sign:
            self.modeMenu.entryconfigure(1, label="Malnehmen")
            self.modeMenu.entryconfigure(2, label="Teilen")
            self.modeMenu.entryconfigure(3, label="✓ Gemischte Aufgaben")


if __name__ == '__main__':
    w = MainWidget()
