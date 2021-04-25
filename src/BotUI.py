from PyQt5 import QtCore, QtGui, QtWidgets
import src.Images_rc

class BotUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
        "background-color: rgb(80, 80, 80);\n"
        "\n"
        "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 10, 201, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Image/ForMe.png"))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 180, 361, 41))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
        "background-color: rgb(52, 52, 52);\n"
        "border-radius:1px;\n"
        "    font: 12pt \"Segoe Print\";\n"
        "    color: rgb(255, 255, 255);\n"
        "}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(60, 220, 361, 201))
        self.textEdit.setStyleSheet("QTextEdit{\n"
        "color: rgb(255, 255, 255);\n"
        "    font: 24pt \"Segoe Print\";\n"
        "border-radius:1px;\n"
        "}")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(340, 440, 75, 23))
        self.pushButton.setStyleSheet("QPushButton{\n"
        "background-color: rgb(52, 52, 52);\n"
        "border-radius:1px;\n"
        "font: 8pt \"Segoe Print\";\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(0, 0, 0);\n"
        "    color: rgb(255, 255, 255);\n"
        "}\n"
        "QPushButton:pressed{\n"
        "background-color: rgb(79, 79, 79);\n"
        "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 0, 21, 23))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
        "font: 12pt \"MS Shell Dlg 2\";\n"
        "background-color: rgb(0, 0, 0);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:1px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "background-color: rgb(255, 0, 0);\n"
        "}\n"
        "QPushButton:pressed{\n"
        "background-color: rgb(255, 49, 62);\n"
        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Segoe Print\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Chat"))
        self.pushButton_2.setText(_translate("MainWindow", "X"))

