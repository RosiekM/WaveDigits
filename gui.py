import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.slider import Slider
from kivy.uix.filechooser import abspath
import threading
import taglib
import time
import threading
from kivy.uix.modalview import ModalView

Builder.load_file('gui.kv')

class tagEditor (GridLayout):


    def run(self):
        import FilesManager
        import test, gmm
        from sklearn.model_selection import KFold

        files, digits, types = FilesManager.importFiles("train")

        train, test = test.split(types["M"])

        mfcc = []
        for i in test:
            mfcc.append(FilesManager.joinMfcc(files, excluded=i))


        for k in range(len(train)):
            one = gmm.myGmm(mfcc[k])

            good = 0
            bad = 0
            for i in files:
                if files[i]['lektor'] in test[k]:
                    if gmm.compare(one, files[i]) == files[i]["znak"]:
                        good += 1
                    else:
                        bad += 1
            file = open("recognition_ratio", 'a')
            file.write("recognition ratio of: " + str(k) + " ")
            file.write(str(int(good / (good + bad) * 100)) + "%\n")
            file.close







class MyApp(App):
    def build(self):
        self.title = "WaveDigits"
        return tagEditor()

MyApp().run()