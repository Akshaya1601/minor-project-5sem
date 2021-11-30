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
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
import pyperclip
import helpers
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton
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

Window.size = (400, 583)

class SplashScreen1(Screen):
    pass

class SplashScreen2(Screen):
    pass

class SplashScreen3(Screen):
    pass

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
    def show_error1(self):
        ok_button = MDFlatButton(text="OK", on_release=self.close_dialog)
        print("Error!")
        self.dialog = MDDialog(text="Please fill all fields!!", buttons=[ok_button])
        self.dialog.open()

    def show_error2(self):
        ok_button = MDFlatButton(text="OK", on_release=self.close_dialog)
        print("Error!")
        self.dialog = MDDialog(text="The answer to do you have a pet must be either YES or NO!", buttons=[ok_button])
        self.dialog.open()

    def show_error3(self):
        ok_button = MDFlatButton(text="OK", on_release=self.close_dialog)
        print("Error!")
        self.dialog = MDDialog(text="The answer to adopt or foster must be either ADOPT or FOSTER!", buttons=[ok_button])
        self.dialog.open()

    def show_error4(self):
        ok_button = MDFlatButton(text="OK", on_release=self.close_dialog)
        print("Error!")
        self.dialog = MDDialog(text="The answer to flat or independant must be either FLAT or INDEPENDANT!", buttons=[ok_button])
        self.dialog.open()

    def validate(self):
        fullname = self.ids.fullName.text
        ph_number = self.ids.ph_number.text
        haspet = self.ids.haspet.text.lower()
        adoptorfoster = self.ids.adoptorfoster.text.lower()
        flatorind = self.ids.flatorind.text.lower()

        valid_haspet = ['yes', 'no']
        valid_adoptorfoster = ['adopt', 'foster']
        valid_flatorind = ['flat', 'independant']
        flag = 0

        if fullname=="" or ph_number=="" or haspet=="" or adoptorfoster=="" or flatorind=="":
            flag = 1
        elif haspet not in valid_haspet:
            flag = 2
        elif adoptorfoster not in valid_adoptorfoster:
            flag = 3
        elif flatorind not in valid_flatorind:
            flag = 4

        if flag == 0:
            self.submitdetails()
        elif flag == 1:
            self.show_error1()
        elif flag == 2:
            self.show_error2()
        elif flag == 3:
            self.show_error3()
        elif flag == 4:
            self.show_error4()

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

        close_button = MDFlatButton(text="Close",
                                    on_release=self.close_dialog)
        self.dialog = MDDialog(title="Thank you!",
                               text="You can now view adoption listings!",
                               size_hint=(0.7, 1),
                               buttons=[close_button])
        self.dialog.open()
        self.manager.current = 'loggedin'
        self.manager.transition.direction = 'right'

    def close_dialog(self, obj):
        self.dialog.dismiss()

class DonationScreen(Screen):
    def copy_text(self, text):
        pyperclip.copy(text)

class ResourcesScreen(Screen):
    pass

class UserQueryScreen(Screen):
    def validate(self):
        flag = 0
        query = self.ids.query.text
        if query == "":
            flag = 1

        if flag == 0:
            self.sendquery()
        else:
            self.show_error()

    def sendquery(self):
        global current_account

        mycursor.execute("SELECT * FROM registration")

        for i in mycursor:
            if i[1] == current_account:
                fullname = i[0]

        querytext = self.ids.query.text

        mycursor.execute("INSERT INTO queries (fullname, phno, query) VALUES (%s, %s, %s)", (fullname, current_account, querytext))
        db.commit()
        self.ids.query.text = ""
        self.show_button()

    def show_button(self):
        ok_button = MDFlatButton(text="OK", on_release=self.close_dialog)
        print("Query submitted!")
        self.dialog = MDDialog(text="Your question has been sent", buttons=[ok_button])
        self.dialog.open()

    def show_error(self):
        ok_button = MDFlatButton(text="OK", on_release=self.close_dialog)
        print("Error!")
        self.dialog = MDDialog(text="Cannot submit empty query!", buttons=[ok_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


sm = ScreenManager()
sm.add_widget(SplashScreen1(name='splash1'))
sm.add_widget(SplashScreen2(name='splash2'))
sm.add_widget(SplashScreen3(name='splash3'))
sm.add_widget(StartScreen(name='start'))
sm.add_widget(NewProfileScreen(name='newprofile'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(ProfileCreatedScreen(name='profilecreated'))
sm.add_widget(LoggedInScreen(name='loggedin'))
sm.add_widget(AdoptNowScreen(name='adoptnow'))
sm.add_widget(AdoptionAppealScreen(name='appeal'))
sm.add_widget(AdopterFormScreen(name='adopterform'))
sm.add_widget(DonationScreen(name='donation'))
sm.add_widget(ResourcesScreen(name='resources'))
sm.add_widget(UserQueryScreen(name='queries'))

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        screen = Builder.load_string(navigation_helper)

        return screen


DemoApp().run()
