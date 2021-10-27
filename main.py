from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
import mysql.connector
from kivymd.uix.button import MDFlatButton
import helpers
from helpers import navigation_helper

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="dog_app"
)

mycursor = db.cursor()

Window.size = (300, 500)


class StartScreen(Screen):
    pass


class NewProfileScreen(Screen):
    def registration(self):
        fullname = self.ids.fullName.text
        ph_number = self.ids.ph_number.text
        pw = self.ids.pw.text

        if self.acc_exists(ph_number):
            print("Account already exists!")

            self.ids.fullName.text = ""
            self.ids.ph_number.text = ""
            self.ids.pw.text = ""

            self.manager.current = 'accexists'
            self.manager.transition.direction = "left"
        else:
            mycursor.execute("INSERT INTO registration (fullname, phno, pw) VALUES (%s, %s, %s)",
                             (fullname, ph_number, pw))
            db.commit()

            self.ids.fullName.text = ""
            self.ids.ph_number.text = ""
            self.ids.pw.text = ""

            self.manager.current = 'profilecreated'
            self.manager.transition.direction = "left"

    def acc_exists(self, ph_number):
        flag = 0
        mycursor.execute("SELECT phno FROM registration")
        for i in mycursor:
            if ph_number == i[0]:
                flag = 1
        if flag == 0:
            return False
        else:
            return True


class ProfileCreatedScreen(Screen):
    pass


class AccExistScreen(Screen):
    pass


class LoginScreen(Screen):
    def login(self):
        phno = self.ids.phno.text
        pw = self.ids.pw.text

        flag = 2
        mycursor.execute("SELECT * FROM registration")
        for i in mycursor:
            if phno == i[1]:
                flag = 1
                if pw == i[2]:
                    flag = 0
                    self.ids.phno.text = ""
                    self.ids.pw.text = ""

                    self.manager.current = 'loggedin'
                    self.manager.transition.direction = 'left'
        if flag == 1:
            close_button = MDFlatButton(text="Close",
                                        on_release=self.close_dialog)

            self.ids.phno.text = ""
            self.ids.pw.text = ""

            self.dialog = MDDialog(title="Password incorrect",
                              text="Password incorrect!",
                              size_hint=(0.7, 1),
                              buttons=[close_button])
            self.dialog.open()
        elif flag == 2:
            close_button = MDFlatButton(text="Close",
                                        on_release=self.close_dialog)

            self.ids.phno.text = ""
            self.ids.pw.text = ""

            self.dialog = MDDialog(title="Not Found",
                              text="Account not found! Please register from home page",
                              size_hint=(0.7, 1),
                              buttons=[close_button])
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

class LoggedInScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(StartScreen(name='start'))
sm.add_widget(NewProfileScreen(name='newprofile'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(ProfileCreatedScreen(name='profilecreated'))
sm.add_widget(LoggedInScreen(name='loggedin'))


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        screen = Builder.load_string(navigation_helper)

        return screen


DemoApp().run()
