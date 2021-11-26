from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
import mysql.connector
from kivymd.uix.button import MDFlatButton
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard
from helpers import navigation_helper
from kivy.factory import Factory
from kivy.uix.behaviors import button
from kivymd.uix.screen import MDScreen

__version__ = "0.0.1"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="dog_app"
)

mycursor = db.cursor()
current_account = "placeholder"

Window.size = (350, 583)


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
        global current_account
        phno = self.ids.phno.text
        pw = self.ids.pw.text

        flag = 2
        mycursor.execute("SELECT * FROM registration")
        for i in mycursor:
            if phno == i[1]:
                flag = 1
                if pw == i[2]:
                    flag = 0
                    current_account = phno

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
    def checkcurrent(self):
        global current_account

        mycursor.execute("SELECT * FROM adopterdetails")


        for i in mycursor:
            if current_account == i[1]:
                self.manager.current = 'adoptnow'
                self.manager.transition.direction = 'left'
            else:
                self.manager.current = 'adopterform'
                self.manager.transition.direction = 'left'

class AdoptNowScreen(Screen):
    def show_button(self):
        ok_button = MDFlatButton(text="OK", on_release=self.close_dialog)
        print("Going to adoption form")
        self.dialog = MDDialog(text="Your request has been sent", buttons=[ok_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

class AdoptionAppealScreen(Screen):
    def show_button(self):
        ok_button = MDFlatButton(text="OK", on_release=self.close_dialog)
        print("Going to adoption form")
        self.dialog = MDDialog(text="Your request has been sent", buttons=[ok_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

class AdopterFormScreen(Screen):
    def submitdetails(self):
        fullname = self.ids.fullName.text
        ph_number = self.ids.ph_number.text
        haspet = self.ids.haspet.text
        haspet = haspet.lower()
        adoptorfoster = self.ids.adoptorfoster.text
        adoptorfoster = adoptorfoster.lower()
        flatorind = self.ids.flatorind.text
        flatorind = flatorind.lower()

        mycursor.execute("INSERT INTO adopterdetails (fullname, phno, haspet, adoptorfoster, flatorind) VALUES (%s, %s, %s, %s, %s)",
                         (fullname, ph_number, haspet, adoptorfoster, flatorind))
        db.commit()

sm = ScreenManager()
sm.add_widget(StartScreen(name='start'))
sm.add_widget(NewProfileScreen(name='newprofile'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(ProfileCreatedScreen(name='profilecreated'))
sm.add_widget(LoggedInScreen(name='loggedin'))
sm.add_widget(AdoptNowScreen(name='adoptnow'))
sm.add_widget(AdoptionAppealScreen(name='appeal'))
sm.add_widget(AdopterFormScreen(name='adopterform'))

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        screen = Builder.load_string(navigation_helper)

        return screen


DemoApp().run()
