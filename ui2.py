# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_folder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_folder.setGeometry(QtCore.QRect(10, 20, 171, 31))
        self.btn_folder.setObjectName("btn_folder")
        self.btn_doright = QtWidgets.QPushButton(self.centralwidget)
        self.btn_doright.setGeometry(QtCore.QRect(290, 370, 81, 31))
        self.btn_doright.setObjectName("btn_doright")
        self.btn_mirror = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mirror.setGeometry(QtCore.QRect(380, 370, 81, 31))
        self.btn_mirror.setObjectName("btn_mirror")
        self.btn_sharp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sharp.setGeometry(QtCore.QRect(470, 370, 81, 31))
        self.btn_sharp.setObjectName("btn_sharp")
        self.btn_B_W = QtWidgets.QPushButton(self.centralwidget)
        self.btn_B_W.setGeometry(QtCore.QRect(560, 370, 81, 31))
        self.btn_B_W.setObjectName("btn_B_W")
        self.btn_doleft = QtWidgets.QPushButton(self.centralwidget)
        self.btn_doleft.setGeometry(QtCore.QRect(200, 370, 81, 31))
        self.btn_doleft.setObjectName("btn_doleft")
        self.list_files = QtWidgets.QListWidget(self.centralwidget)
        self.list_files.setGeometry(QtCore.QRect(10, 60, 171, 371))
        self.list_files.setObjectName("list_files")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(210, 60, 450, 300))
        self.image.setObjectName("image")
        self.btn_blur = QtWidgets.QPushButton(self.centralwidget)
        self.btn_blur.setGeometry(QtCore.QRect(200, 402, 81, 31))
        self.btn_blur.setObjectName("btn_blur")
        self.btn_contrast = QtWidgets.QPushButton(self.centralwidget)
        self.btn_contrast.setGeometry(QtCore.QRect(290, 402, 81, 31))
        self.btn_contrast.setObjectName("btn_contrast")
        self.btn_green = QtWidgets.QPushButton(self.centralwidget)
        self.btn_green.setGeometry(QtCore.QRect(380, 402, 81, 31))
        self.btn_green.setObjectName("btn_green")
        self.btn_smooth = QtWidgets.QPushButton(self.centralwidget)
        self.btn_smooth.setGeometry(QtCore.QRect(470, 402, 81, 31))
        self.btn_smooth.setObjectName("btn_smooth")
        self.btn_sigma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sigma.setGeometry(QtCore.QRect(560, 402, 81, 31))
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(547, 20, 81, 31))
        self.btn_save.setObjectName("btn_save")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btn_sigma.setObjectName("btn_sigma")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_folder.setText(_translate("MainWindow", "Папка"))
        self.btn_doright.setText(_translate("MainWindow", "Праворуч"))
        self.btn_mirror.setText(_translate("MainWindow", "Дзеркало"))
        self.btn_sharp.setText(_translate("MainWindow", "Різкість"))
        self.btn_B_W.setText(_translate("MainWindow", "Ч/Б"))
        self.btn_doleft.setText(_translate("MainWindow", "Ліворуч"))
        self.image.setText(_translate("MainWindow", "Картинка"))
        self.btn_blur.setText(_translate("MainWindow", "Блюр"))
        self.btn_contrast.setText(_translate("MainWindow", "Контраст"))
        self.btn_green.setText(_translate("MainWindow", "Зелений"))
        self.btn_smooth.setText(_translate("MainWindow", "Гладкий"))
        self.btn_sigma.setText(_translate("MainWindow", "Контур"))
        self.btn_save.setText(_translate("MainWindow", "Збереження"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
