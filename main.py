import sys
from os import system
from threading import Thread
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
    def __init__(self,bot,Net):
        QMainWindow.__init__(self)
        self.ui = BotUI()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.show()
        self.Net=Net
        def Clicked(Bot):
            try:
                input = self.ui.lineEdit.text()
                Bot.chat(input,self.ui)
                self.ui.lineEdit.setText("")
                Speach = Talk(Bot.say, Bot.count)
                Process = Thread(target=Speach.read())
                Process.start()
                self.Net.Connect(f"PlayAudio audios/speak{Speach.coun}.wav")
            except Exception as e:
                print(e)

        def moveWindow(e):
            if e.buttons() == Qt.LeftButton:  
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()
        #Change this when turning this to exe
        def Finish():
            system('taskkill /f /im java.exe')
            QCoreApplication.instance().quit()
        self.ui.frame.mouseMoveEvent = moveWindow
        self.ui.pushButton_2.clicked.connect(Finish)
        self.ui.textEdit.setText("Start talking with the bot")
        self.ui.pushButton.clicked.connect(lambda: Clicked(bot))



    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()


if __name__ == "__main__":
    Net= Network()
    Network.RunServer()
    Talk.delete()
    bot = Bot()
    bot.read()
    bot.stem()
    bot.modelsetup()
    bot.setup()
    app = QApplication(sys.argv)
    window = Winner(bot,Net)
    sys.exit(app.exec_())