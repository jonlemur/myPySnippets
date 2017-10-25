import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class myUI(GridLayout):
    def callback(instance):
        print('Hello Jon')
    
    def __init__(self, **kwargs):
        super(myUI, self).__init__(**kwargs)
        self
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.btnMyButton = Button(text='Press me')
        self.btnMyButton.bind(on_press=self.callback)
        self.add_widget(self.btnMyButton)


class MyApp(App):

    def build(self):
        return myUI()
    
    
if __name__ == '__main__':
    MyApp().run()
