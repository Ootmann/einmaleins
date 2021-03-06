#!/usr/local/bin/python3

"""
MIT License

Copyright (c) 2018 - 2019 Sebastian

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

import colorsys
import decimal
import random
from datetime import datetime
from tkinter import *

from operations import *


# noinspection SpellCheckingInspection
class MainWidget:
    time = datetime.now()
    infoWidget = None
    stats_widget = None
    sign = ":"
    random_sign = True
    last_question = ""
    tries = 0
    max_tries = 3
    stats = {}
    signs = {
        "x": multiply.Multiply(),
        ":": divide.Divide(),
        "+": plus.Plus(),
        "-": minus.Minus(),
        "round": round.Round(),
        "series": series.Series(),
        "money_add": money_add.MoneyAdd(),
        "money_rest": money_rest.MoneyRest()
    }

    def __init__(self):
        self.root = Tk()
        self.root.title("Einmaleins")
        self.root.geometry('{}x{}'.format(600, 400))
        self.root.config(bg='#FFFFFF')
        self.root.resizable(width=False, height=False)

        self.ask_multiplication = BooleanVar(value=True)
        self.ask_division = BooleanVar(value=True)
        self.ask_plus = BooleanVar(value=True)
        self.ask_minus = BooleanVar(value=True)
        self.ask_round = BooleanVar(value=True)
        self.ask_series = BooleanVar(value=True)
        self.ask_money_add = BooleanVar(value=True)
        self.ask_money_rest = BooleanVar(value=True)

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.more_menu = Menu(self.menu)
        self.mode_menu = Menu(self.menu)
        self.menu.add_cascade(label="Mehr", menu=self.more_menu)
        self.menu.add_cascade(label="Aufgaben", menu=self.mode_menu)

        self.more_menu.add_command(label="Info", command=self.show_info)
        self.more_menu.add_command(label="Statistik", command=self.show_stats)
        self.more_menu.add_command(label="Überspringen", command=self.update)
        self.more_menu.add_command(label="Beenden", command=sys.exit)

        self.mode_menu.add_checkbutton(label="Malnehmen", onvalue=True, offvalue=False,
                                       variable=self.ask_multiplication)
        self.mode_menu.add_checkbutton(label="Teilen", onvalue=True, offvalue=False, variable=self.ask_division)
        self.mode_menu.add_checkbutton(label="Plus", onvalue=True, offvalue=False, variable=self.ask_plus)
        self.mode_menu.add_checkbutton(label="Minus", onvalue=True, offvalue=False, variable=self.ask_minus)
        self.mode_menu.add_checkbutton(label="Runden", onvalue=True, offvalue=False, variable=self.ask_round)
        self.mode_menu.add_checkbutton(label="Zahlenreihen", onvalue=True, offvalue=False, variable=self.ask_series)
        self.mode_menu.add_checkbutton(label="Geld addieren", onvalue=True, offvalue=False, variable=self.ask_money_add)
        self.mode_menu.add_checkbutton(label="Geld übrig", onvalue=True, offvalue=False, variable=self.ask_money_rest)

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
        self.entry_field.config(bg='#F0F0F0', font=("Sans", 16), borderwidth=1, relief="flat", width=10,
                                justify='center')
        self.entry_field.bind("<Return>", self.answer)

        self.submit_button = Button(submit_frame)
        self.submit_button.pack(side=RIGHT, padx=15, pady=15, anchor=W)
        self.submit_button.config(text='Antworten', bg='#FFFFFF', font=("Sans", 11), borderwidth=1,
                                  relief="flat", width=7, command=self.answer)

        self.answer_label = Label(self.root)
        self.answer_label.config(bg='#FFFFFF')
        self.answer_label.pack(pady=15)
        self.update()
        self.root.mainloop()

    def update(self):
        signs = []
        if self.ask_multiplication.get():
            signs.append("x")
        if self.ask_division.get():
            signs.append(":")
        if self.ask_plus.get():
            signs.append("+")
        if self.ask_minus.get():
            signs.append("-")
        if self.ask_round.get():
            signs.append("round")
        if self.ask_series.get():
            signs.append("series")
        if self.ask_money_add.get():
            signs.append("money_add")
        if self.ask_money_rest.get():
            signs.append("money_rest")
        if len(signs) == 0:
            self.ask_multiplication.set(True)
            self.ask_division.set(True)
            self.ask_plus.set(True)
            self.ask_minus.set(True)
            self.ask_round.set(True)
            self.ask_series.set(True)
            self.ask_money_add.set(True)
            self.ask_money_rest.set(True)
            self.update()

        self.sign = signs[random.randint(0, len(signs) - 1)]

        if self.sign not in self.signs.keys():
            raise Exception("Unknown operator" + self.sign)

        self.signs[self.sign].update()

        question_text = self.signs[self.sign].get_question()
        if question_text == self.last_question:
            self.update()

        rgb = colorsys.hsv_to_rgb(random.randint(0, 1000) / 1000, 70 / 100, 80 / 100)
        hex_color = '%02x%02x%02x' % (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

        self.last_question = question_text
        self.question_label.config(text=question_text)
        self.question_label.config(bg="#" + hex_color)
        self.time = datetime.now()
        self.tries = 0
        self.refresh()

    def refresh(self):
        correct, wrong = self.get_total_stats()
        self.score_label.config(text="Richtig: {} Falsch: {}".format(correct, wrong))
        self.entry_field.delete(0, 'end')
        self.entry_field.focus()

    # noinspection PyUnusedLocal
    def answer(self, event=None):
        answer = str(self.entry_field.get())
        answer = re.sub('[^0-9,.]', '', answer)
        answer = answer.replace(".", ",")
        answer = answer.strip()

        if answer == "":
            return

        now = datetime.now()
        answer_time_seconds = (now - self.time).seconds

        self.tries += 1

        solve = self.signs[self.sign].solve()
        solve_comparision = re.sub('[^0-9,.]', '', str(solve))
        solve_comparision = solve_comparision.replace(".", ",")
        solve_comparision = solve_comparision.strip()

        if answer == solve_comparision:
            self.answer_label.config(
                text="Toll! Die Lösung für '{}' ist {}.\n\nDas war richtig. Du hast {} Sekunden gebraucht.".format(
                    self.signs[self.sign].get_question(),
                    str(solve),
                    str(answer_time_seconds)))
            self.add_stat_correct()
            self.update()
        elif self.tries < self.max_tries:
            self.answer_label.config(
                text="Schade. Die Lösung für '{}' ist nicht {}.\n\nDu kannst es noch {} mal probieren.".format(
                    self.signs[self.sign].get_question(), answer, self.max_tries - self.tries))
            self.add_stat_wrong()
            self.refresh()
        else:
            self.answer_label.config(
                text="Schade. Die Lösung für '{}' ist {} und nicht {}.\n\nTipp: Du kannst schwere Aufgaben erst auf einem Blatt Papier lösen.".format(
                    self.signs[self.sign].get_question(), str(solve), answer))
            self.add_stat_wrong()
            self.update()

    def show_info(self):
        if self.infoWidget is None:
            self.infoWidget = Toplevel(self.root)
            self.infoWidget.wm_title("Info")
            self.infoWidget.geometry('{}x{}'.format(400, 400))
            self.infoWidget.protocol("WM_DELETE_WINDOW", self.delete_info)
            self.infoWidget.resizable(width=False, height=False)
            info_label = Label(self.infoWidget,
                               text="\nEin mal Eins Lernprogramm\nSebastian Schlegel 2018-2019\nFür meine Maja\n")
            info_label.pack()
            licence_field = Text(self.infoWidget)
            scroll = Scrollbar(self.infoWidget, command=licence_field.yview)
            scroll.pack(side=RIGHT, fill=Y)
            licence_field.configure(yscrollcommand=scroll.set)
            licence_field.pack(side=LEFT, fill=Y)
            licence_field.insert(END, __doc__)
        else:
            self.infoWidget.focus()

    def show_stats(self):
        if self.stats_widget is None:
            self.stats_widget = Toplevel(self.root)
            self.stats_widget.wm_title("Statistik")
            self.stats_widget.geometry('{}x{}'.format(300, 200))
            self.stats_widget.protocol("WM_DELETE_WINDOW", self.delete_stats_widget)
            self.stats_widget.resizable(width=False, height=False)

            Label(self.stats_widget, text="Aufgaben", borderwidth=1).grid(row=0, column=0)
            Label(self.stats_widget, text="Richtig", borderwidth=1).grid(row=0, column=1)
            Label(self.stats_widget, text="Falsch", borderwidth=1).grid(row=0, column=2)
            Label(self.stats_widget, text="Versuche", borderwidth=1).grid(row=0, column=3)

            r = 0
            for operation in self.signs:
                for c in range(4):
                    if c == 0:
                        text = self.signs[operation].description
                    else:
                        try:
                            text = self.stats[operation][c - 1]
                        except KeyError:
                            text = 0
                    Label(self.stats_widget, text=text, borderwidth=1).grid(row=r + 2, column=c)
                r += 1

        else:
            self.stats_widget.focus()

    def delete_info(self):
        if self.infoWidget is not None:
            self.infoWidget.destroy()
            self.infoWidget = None

    def delete_stats_widget(self):
        if self.stats_widget is not None:
            self.stats_widget.destroy()
            self.stats_widget = None

    def add_stat_correct(self):
        try:
            self.stats[self.sign]
        except KeyError:
            self.stats[self.sign] = [0, 0, 0]
        self.stats[self.sign][0] += 1
        self.stats[self.sign][2] += 1

    def add_stat_wrong(self):
        try:
            self.stats[self.sign]
        except KeyError:
            self.stats[self.sign] = [0, 0, 0]
        self.stats[self.sign][1] += 1
        self.stats[self.sign][2] += 1

    def get_total_stats(self):
        result = [0, 0]
        for stat in self.stats.values():
            result[0] += stat[0]
            result[1] += stat[1]
        return result


if __name__ == '__main__':
    decimal.getcontext().prec = 6
    w = MainWidget()
