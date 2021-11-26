from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.behaviors import button
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog

Window.size = (300, 500)

class MainApp(MDApp):
    

    def show_button(self):
        ok_button= MDFlatButton(text="OK",on_release=self.close_dialog)
        print("Going to adoption form")
        self.dialog = MDDialog(text="Your request has been sent",buttons=[ok_button])
        self.dialog.open()
    def close_dialog(self,obj):
        self.dialog.dismiss()

        
    def build(self):
        self.title = 'Adoption/Foster Listing'
        self.theme_cls.primary_palette = "Blue"
        

MainApp().run()