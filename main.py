from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from data import images, wordslist,letters
from kivymd.uix.button import MDFlatButton
import random
from functools import partial
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty,StringProperty,NumericProperty,ListProperty


class HomeScreen(Screen):
    pass


class MainApp(MDApp):
    status = 0
    word = StringProperty(random.choice(wordslist))
    guessedwords = ListProperty([])
    image = StringProperty(images[0])
    displayword = StringProperty()

    def on_start(self):
        letterslayout = self.root.ids['home'].ids['letters']
        for i in range(len(letters)):
            b = MDFlatButton(text=letters[i],font_size=17,md_bg_color=(1, 1, 0, 1),on_release=partial(self.checkletter, letters[i]))
            letterslayout.add_widget(b)

        self.handleword()

    def checkletter(self,*args):
        letter = args[0]
        if letter in self.word:
            self.guessedwords.append(letter)
            self.handleword()
        else:
            if self.status!= 6:
                self.status +=1
                self.image = images[self.status]
            else:
                self.showDialog('Sorry, You Lost',"Better luck next time")

        iswoned = True
        for i in range(len(self.word)):
            char = self.word[i]
            if char not in self.guessedwords:
                iswoned = False
                break
        if iswoned:
            self.showDialog('Hurray You Won',"Congrats")

    def showDialog(self,text,title):
        d = MDDialog(auto_dismiss=False,text=text,size_hint=(.5,.3),title=title,text_button_ok="Restart",on_dismiss=self.restart)
        d.open()

    def restart(self,*args):
        self.status = 0
        self.guessedwords = []
        self.word = random.choice(wordslist)
        self.image = images[0]
        self.handleword()

    def handleword(self):
        print(self.word)
        displayword = ''
        for i in range(len(self.word)):
            char  = self.word[i]
            if char in self.guessedwords:
                displayword += char + " "
            else:
                displayword += "_ "
        self.displayword = displayword

    def __init__(self,**kwargs):
        Window.size = (430,600)
        super().__init__(**kwargs)


MainApp().run()
