import sys
from threading import Thread
from PyQt5 import QtCore
from PyQt5.QtCore import  Qt,QCoreApplication
from PyQt5.QtWidgets import QMainWindow,QApplication
from src.BotUI import *
from src.Network import Network
from src.Bot import Bot
from src.Talk import Talk
#--------------------------------------------------------------------------------------------------------#
#                                                   Contact me                                           #
#                                     https://www.facebook.com/akrem.waeir/                              #
#--------------------------------------------------------------------------------------------------------#
class Winner(QMainWindow):
    def __init__(self,bot):
        QMainWindow.__init__(self)
        self.ui = BotUI()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        def Clicked(Bot):
            input = self.ui.lineEdit.text()
            Bot.chat(input,self.ui)
            self.ui.lineEdit.setText("")
            Speach = Talk(Bot.say, Bot.count)
            Process = Thread(target=Speach.read())
            Process.start()

        def moveWindow(e):
            if e.buttons() == Qt.LeftButton:  
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.ui.frame.mouseMoveEvent = moveWindow
        self.ui.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.ui.textEdit.setText("Start talking with the bot")
        self.ui.pushButton.clicked.connect(lambda: Clicked(bot))



    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()


if __name__ == "__main__":
    Network.RunServer()
    Talk.delete()
    bot = Bot()
    bot.read()
    bot.stem()
    bot.modelsetup()
    bot.setup()
    app = QApplication(sys.argv)
    window = Winner(bot)
    sys.exit(app.exec_())