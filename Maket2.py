import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

import action
import dictionaries
from Form2 import Ui_Form as Ui_Form2
from untitled import Ui_Form


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.trigger_condition)
        self.ui.pushButton_4.clicked.connect(self.examination)
        self.ui.pushButton_3.clicked.connect(self.stoped)
        self.ui.pushButton.clicked.connect(self.open_second_window)
        self.ui.lineEdit.returnPressed.connect(self.examination)
        self.comboBox = self.ui.comboBox
        self.comboBox.addItem("Глаголы А1")
        self.comboBox.addItem("Погода")
        self.comboBox.addItem("Вещи в доме")
        self.comboBox.addItem("new_word")
        self.selected_dict = None
        self.correct = None
        self.question = None
        self.r = None
        self.random_list = None
        self.key = None
        self.comboBox.currentIndexChanged.connect(self.on_combo_box_changed)
        self.combo_dict = {
            "Глаголы А1": dictionaries.verb_A1,
            "Погода": dictionaries.weather_vocabulary,
            "Вещи в доме": dictionaries.house_vocabulary,
            "new_word": dictionaries.new_word
        }
        self.selected_item = self.ui.comboBox.currentText()
        self.selected_dict = self.combo_dict.get(self.selected_item)

    def open_second_window(self):
        second_window = SecondWindow(self)
        second_window.exec_()

    def on_combo_box_changed(self, index):
        selected_item = self.ui.comboBox.currentText()
        self.selected_dict = self.combo_dict.get(selected_item)

    def stoped(self):
        self.ui.label.clear()
        self.ui.lineEdit.clear()


    def trigger_condition(self):
        if self.ui.radioButton.isChecked():
            self.random_list, self.key = action.find_min_rating(self.selected_dict)
            data_test = action.for_test(self.random_list[0], self.random_list[1], self.random_list[2],
                                        self.random_list[3])
            self.correct, self.question, self.r, language = action.ru_no.quest(data_test)

            self.ui.label.setText(f"Как перевести \' {self.question} \' \n на {language} язык")
            if self.correct == '' or self.question == '' or self.correct == "":
                self.r = + 1
                self.random_list[3] = int(self.r)
                self.selected_dict[self.key] = self.random_list
                print(self.random_list)
                self.trigger_condition()
            if self.correct == 'Словарь пройде!!':
                self.ui.label.setText('Словарь пройде!!')
                self.selected_dict = action.clear_dict(self.selected_dict)
                print(f" СМОТРИ СЮДА  {self.selected_dict}")

        elif self.ui.radioButton_2.isChecked():
            self.random_list, self.key = action.find_min_rating(self.selected_dict)
            data_test = action.for_test(self.random_list[0], self.random_list[1], self.random_list[2],
                                        self.random_list[3])
            self.correct, self.question, self.r, language = action.ru_en.quest(data_test)
            self.ui.label.setText(f"Как перевести  \' {self.question}\' \n на {language} язык")
            if self.correct == '' or self.question == '' or self.correct == "":
                self.r =+ 1
                self.random_list[3] = int(self.r)
                self.selected_dict[self.key] = self.random_list
                print(self.random_list)
                self.trigger_condition()
            if self.correct == 'Словарь пройде!!':
                self.ui.label.setText(f' {self.question}')
                timer = QTimer()
                timer.singleShot(2300, self.trigger_condition)
                self.stoped()

    def examination(self):
        if not self.question:
            return
        else:
            answer = self.ui.lineEdit.text()
            self.ui.lineEdit.clear()
            # grade = action.testing_r(answer, self.correct, self.r)
            # tf = action.testing_bool(answer, self.correct, self.r)
            if answer != self.correct:
                if self.random_list[3] == 0:
                    self.ui.label.setText(f"ОШИБКА\nПравильный ответ: {self.correct}")
                else:
                    self.r -= 1
                    self.ui.label.setText(f"ОШИБКА\nПравильный ответ: {self.correct}")

            elif answer == self.correct:
                self.ui.label.setText("Правильно!")
                self.r += 1

            print(self.r)
            self.random_list[3] = int(self.r)
            self.selected_dict[self.key] = self.random_list
            # print("self.selected_dict:",

            timer = QTimer()
            timer.singleShot(2300, self.trigger_condition)


class SecondWindow(QDialog):
    def __init__(self,  main_ui):
        super().__init__()
        self.ui = Ui_Form2()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem("Глаголы А1")
        self.ui.comboBox.addItem("Погода")
        self.ui.comboBox.addItem("Вещи в доме")
        self.ui.comboBox.addItem("new_word")
        self.ui.pushButton.clicked.connect(self.add_word)
        self.combo_dict = {
            "Глаголы А1": dictionaries.verb_A1,
            "Погода": dictionaries.weather_vocabulary,
            "Вещи в доме": dictionaries.house_vocabulary,
            "new_word": dictionaries.new_word
        }

    def add_word(self):
        rus = self.ui.lineEdit.text()
        eng = self.ui.lineEdit_2.text()
        nor = self.ui.lineEdit_3.text()
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        selected_item = self.ui.comboBox.currentText()
        selected_dict = self.combo_dict[selected_item]
        new_list = [rus, eng, nor, 0]
        selected_dict[selected_item] = new_list
        print(selected_dict)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())

