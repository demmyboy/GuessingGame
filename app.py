# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guessing.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    low_number = 1
    high_number = 10
    guess_left = 5 
    hidden_number = random.randint(low_number, high_number)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.setWindowIcon(QtGui.QIcon("demmy.png"))
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.round_label = QtWidgets.QLabel(self.centralwidget)
        self.round_label.setGeometry(QtCore.QRect(150, 50, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.round_label.setFont(font)
        self.round_label.setScaledContents(False)
        self.round_label.setAlignment(QtCore.Qt.AlignCenter)
        self.round_label.setWordWrap(False)
        self.round_label.setObjectName("round_label")
        self.win_count_label = QtWidgets.QLabel(self.centralwidget)
        self.win_count_label.setGeometry(QtCore.QRect(160, 110, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.win_count_label.setFont(font)
        self.win_count_label.setScaledContents(False)
        self.win_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.win_count_label.setWordWrap(False)
        self.win_count_label.setObjectName("win_count_label")
        self.highScoreCount_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.highScoreCount_label_4.setGeometry(QtCore.QRect(460, 120, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.highScoreCount_label_4.setFont(font)
        self.highScoreCount_label_4.setScaledContents(False)
        self.highScoreCount_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.highScoreCount_label_4.setWordWrap(False)
        self.highScoreCount_label_4.setObjectName("highScoreCount_label_4")
        self.guess_info = QtWidgets.QLabel(self.centralwidget)
        self.guess_info.setGeometry(QtCore.QRect(80, 190, 611, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.guess_info.setFont(font)
        self.guess_info.setScaledContents(False)
        self.guess_info.setAlignment(QtCore.Qt.AlignCenter)
        self.guess_info.setWordWrap(False)
        self.guess_info.setObjectName("guess_info")
        self.entry1 = QtWidgets.QLineEdit(self.centralwidget)
        self.entry1.setGeometry(QtCore.QRect(170, 290, 391, 41))
        self.entry1.setObjectName("entry1")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(170, 340, 101, 41))
        self.button1.setObjectName("button1")
        self.Hint_label = QtWidgets.QLabel(self.centralwidget)
        self.Hint_label.setGeometry(QtCore.QRect(240, 440, 400, 60))
        self.Hint_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Hint_label.setObjectName("Hint_label")
        self.highScore_label = QtWidgets.QLabel(self.centralwidget)
        self.highScore_label.setGeometry(QtCore.QRect(420, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.highScore_label.setFont(font)
        self.highScore_label.setScaledContents(False)
        self.highScore_label.setAlignment(QtCore.Qt.AlignCenter)
        self.highScore_label.setWordWrap(False)
        self.highScore_label.setObjectName("highScore_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button1.clicked.connect(self.guess_number)
        self.entry1.returnPressed.connect(self.guess_number)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Guessing"))
        self.round_label.setText(_translate("MainWindow", "Round"))
        self.win_count_label.setText(_translate("MainWindow", "1"))
        self.highScoreCount_label_4.setText(_translate("MainWindow", "1"))
        self.guess_info.setText(_translate("MainWindow", f"Guess a number between {self.low_number} and {self.high_number}. \n 10 Guess Numbers {self.guess_left}"))
        self.button1.setText(_translate("MainWindow", "Guess"))
        self.Hint_label.setText(_translate("MainWindow", " "))
        self.highScore_label.setText(_translate("MainWindow", "High Score"))

    def guess_number(self):
        guess = self.entry1.text()
        try:
            guess =int(guess)
            if guess == self.hidden_number:
                self.high_number = self.high_number*2
                new_round = int(self.win_count_label.text()) + 1
                self.win_count_label.setText(str(new_round))
                self.guess_left = 5
                self.hidden_number = random.randint(self.low_number, self.high_number)
                self.guess_info.setText(f"Guess a number between {self.low_number} and {self.high_number}. \n 10 Guess Numbers {self.guess_left}")
                self.entry1.setText("") 
                self.Hint_label.setText(f"Nice! {self.low_number} - {self.high_number}")
            elif self.guess_left > 1:
                if guess < self.hidden_number:
                    self.Hint_label.setText(f"{guess} is too low ....")
                else: 
                    self.Hint_label.setText(f"{guess} is too high ....")
                self.guess_left -= 1
                self.entry1.setText("")
                self.guess_info.setText(f"Guess a number between {self.low_number} and {self.high_number}. \n 10 Guess Numbers {self.guess_left}")
            else: 
                self.low_number = 1
                self.high_number = 10
                self.guess_left = 5 
                self.hidden_number = random.randint(self.ow_number, self.high_number)
                self.guess_info.setText(f"Guess a number between {self.low_number} and {self.high_number}. \n 10 Guess Numbers {self.guess_left}")
                self.entry1.setText("")
                self.hint.setText(f"You Lose! {self.hidden_number} \n lets make this easy for you again ")

                new_score = int(self.win_count_label.text())
                high_score = int(self.highScoreCount_label_4.text())
                self.win_count_label.setText("1")
                if new_score > high_score: 
                    self.highScoreCount_label_4.setText(str(new_score))
        except ValueError:
            self.Hint_label.setText("You need to guess a number not a word. Dummy!!")

        print(guess)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    style = """ 
        QWidget{
            background:#262D37;
        }
        QLabel{
            color:#fff;
        }
        QLabel#win_count_label, QLabel#highScoreCount_label_4{
            border: 1px solid #fff; 
            border-radius: 8px;
            padding: 2px
        }
        QlineEdit{
            padding:1px;
            color:#fff;
            border: 2px solid #fff;
            border-radius: 8px; 
        }
        QPushButton{
            color: #fff;
            outline:none;
            padding: 5px 10px;
            background: #0577a8; 
        }
        QPushButton:hover{
            color: #0892D0;  
        }
    
    """
    app.setStyleSheet(style)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
