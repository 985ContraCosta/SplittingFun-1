import kivy
from kivy.app import App
from kivy.uix.label import Label

class SplittingFun(App):

    def build(self):
        return Label(text = "Goodbye World!")
    
if __name__ == "__main__":
    SplittingFun().run()