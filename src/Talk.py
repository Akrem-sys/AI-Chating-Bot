from gtts import gTTS
from os import remove,listdir
from playsound import playsound
class Talk:
    def __init__(self,text,count,language='en',slow=False):
        self.text=str(text)
        self.language=language
        self.slow=slow
        self.coun=count
    def read(self):
        out = gTTS(text=self.text,lang=self.language,slow=self.slow)
        out.save(f"audios/speak{self.coun}.mp3")
        playsound(f"audios/speak{self.coun}.mp3")
    def delete():
        path="audios/"
        dir=listdir(path)
        for i in dir:
            remove(path+i)