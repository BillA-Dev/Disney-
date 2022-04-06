import requests as web

from bs4 import BeautifulSoup
import random

import sys
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QGridLayout, QWidget,
    QCheckBox, QSystemTrayIcon,
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp)
from PyQt5.QtCore import QSize


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 202)
        MainWindow.setMinimumSize(QtCore.QSize(797, 202))
        MainWindow.setMaximumSize(QtCore.QSize(797, 202))
        # frameless and transparent
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
                                 "\n"
                                 "background-color:#282A36;\n"
                                 "color:#282A36;\n"
                                 "border-radius: 20px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lg_image = QtWidgets.QLabel(self.frame)
        self.lg_image.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.lg_image.setText("")
        self.lg_image.setPixmap(QtGui.QPixmap("2a91e5e7a26c419aa9dd916ba32f5645White.png"))
        self.lg_image.setScaledContents(False)
        self.lg_image.setObjectName("lg_image")
        self.textBox = QtWidgets.QLineEdit(self.frame)
        self.textBox.setGeometry(QtCore.QRect(12, 90, 551, 31))
        self.textBox.setStyleSheet("background-color: #646985;\n"
                                   "border: 2px;\n"
                                   "border-color:#646985;\n"
                                   "border-radius: 13px;\n"
                                   "color: rgb(255, 255, 255)")
        self.textBox.setAlignment(QtCore.Qt.AlignCenter)
        self.textBox.setObjectName("textBox")
        self.textBox.setEnabled(False)
        self.generateBUtton = QtWidgets.QPushButton(self.frame)
        self.generateBUtton.setGeometry(QtCore.QRect(610, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.generateBUtton.setFont(font)
        self.generateBUtton.setStyleSheet("QPushButton{\n"
                                          "\n"
                                          "background-color: #16d1f8;\n"
                                          " border: 2px;\n"
                                          " border-radius: 13px;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover:!pressed {background-color: #8BE9FD; }"
                                          )
        self.generateBUtton.setObjectName("generateBUtton")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(730, 0, 48, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.close = QtWidgets.QPushButton(self.layoutWidget)
        self.close.setStyleSheet("QPushButton{border-radius:0px;border: 0px solid #345781;}")
        self.close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons8-macos-close-96.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.close.setIcon(icon1)
        self.close.setObjectName("close")
        self.horizontalLayout_2.addWidget(self.close)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # CONNECT BUTTON HERE
        self.generateBUtton.clicked.connect(self.mainFunc)
        self.close.clicked.connect(self.closeScreen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DinseyPlus"))
        self.generateBUtton.setText(_translate("MainWindow", "Generate"))

    def mainFunc(self):
        try:

            movies_and_shows = []
            with open("MoviesAndShows.txt", mode="r") as f:
                for i in f:
                    movies_and_shows.append(i)
            print("file found")
            chosen = movies_and_shows[random.randint(0, len(movies_and_shows) - 1)]
            print(f"Chosen = {chosen}")
            self.textBox.setText(chosen)



        except:

            response = web.get("https://www.androidauthority.com/disney-plus-movies-tv-shows-1040529/")
            html = BeautifulSoup(response.text, 'html.parser')  # Beutidul soup object, constructor!
            tagList = html.findAll("li")

            movies_and_shows = []
            index = 0
            with open("MoviesAndShows.txt", mode="w") as f:
                for i in tagList:
                    string = str(i)
                    movies_and_shows.append(string[string.index("<li>") + 4:string.index("</li>")])
                    f.write(f"{movies_and_shows[index]}\n")
                    index += 1

            print(movies_and_shows)
            chosen = movies_and_shows[random.randint(0, len(movies_and_shows) - 1)]
            print(f"Chosen = {chosen}")
            print("file created")
            self.textBox.setText(chosen)

    def closeScreen(self):
        print("ex clicked")
        self.close()

    def minimize(self):
        print("minClicked")
        self.showMinimized()
        self.hide()
        self.showNormal()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
