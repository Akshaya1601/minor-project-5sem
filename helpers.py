navigation_helper = """
ScreenManager:
    StartScreen:
    NewProfileScreen:
    ProfileCreatedScreen:
    AccExistScreen:
    LoginScreen:

<StartScreen>:
    name: 'start'

    MDFillRoundFlatIconButton:
        text: 'New Profile'
        icon: 'account-plus'
        on_press: 
            root.manager.current= 'newprofile'
            root.manager.transition.direction = 'left'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDFillRoundFlatIconButton:
        text: 'Log In'
        icon: 'account-arrow-right'
        on_press: 
            root.manager.current= 'login'
            root.manager.transition.direction = 'left'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}

    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Dog App"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                Image:
                    source: 'vector60-3771-01.jpg'

                MDLabel:
                    text: '  Welcome to our App'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: '  Akash B'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                MDLabel:
                    text: '  Akshaya N'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                MDLabel:
                    text: '  Pranjal P'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                MDLabel:
                    text: '  Prarthana G'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        spacing: '8dp'
                        padding: '8dp'
                    
                        MDRectangleFlatIconButton:
                            text: 'Register'
                            on_press: 
                                root.manager.current= 'newprofile'
                                root.manager.transition.direction = 'left'
                            icon: 'account-plus'

                        MDRectangleFlatIconButton:
                            text: 'Log in'
                            on_press: 
                                root.manager.current= 'login'
                                root.manager.transition.direction = 'left'
                            icon: 'account-arrow-right'
                            theme_text_color: 'Hint'

<NewProfileScreen>:
    name: 'newprofile'

    MDLabel:
        text: 'Register New Account'
        halign: 'center'
        pos_hint: {'center_y': 0.8}
        font_style: 'H5'
        
    MDTextField:
        id: fullName
        hint_text: "Enter your full name"
        helper_text: "or click here to log-in"
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 200
    
    MDTextField:
        id: ph_number
        hint_text: "Enter your mobile number"
        helper_text: ""
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 200
        
    MDTextField:
        id: pw
        hint_text: "Enter password"
        helper_text: ""
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 200

    MDRoundFlatButton:
        text: 'Register'
        on_press:
            root.registration()
        pos_hint: {'center_x': 0.33, 'center_y': 0.3}
        
    MDRoundFlatButton:
        text: 'Back'
        on_press: 
            root.manager.current= 'start'
            root.manager.transition.direction = 'right'
        pos_hint: {'center_x': 0.67, 'center_y': 0.3}
        theme_text_color: "ContrastParentBackground"

<ProfileCreatedScreen>:
    name: 'profilecreated'
    
    MDLabel:
        text: 'Profile successfully registered!'
        halign: 'center'
        pos_hint: {'center_y': 0.6}
    
    MDLabel:
        text: 'Log in from home'
        halign: 'center'
        pos_hint: {'center_y': 0.5}
    
    MDRectangleFlatButton:
        text: 'Home'
        on_press: 
            root.manager.current= 'start'
            root.manager.transition.direction = 'right'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}

<AccExistScreen>:
    name: 'accexists'
    
    MDLabel:
        text: 'Account already registered!!'
        halign: 'center'
        pos_hint: {'center_y': 0.6}
    
    MDLabel:
        text: 'Log in from home'
        halign: 'center'
        pos_hint: {'center_y': 0.5}
    
    MDRectangleFlatButton:
        text: 'Home'
        on_press: 
            root.manager.current= 'start'
            root.manager.transition.direction = 'right'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}


<LoginScreen>:
    name: 'login'

    MDLabel:
        text: 'Log In'
        halign: 'center'
        pos_hint: {'center_y': 0.8}
        font_style: 'H5'
        
    MDTextField:
        id: phno
        hint_text: "Enter phone number"
        helper_text: "Use registered mobile number"
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 200
    
    MDTextField:
        id: pw
        hint_text: "Enter password"
        helper_text: ""
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 200

    MDRoundFlatButton:
        text: 'Log In'
        on_press:
            root.login()
            root.manager.current= 'profilecreated'
            root.manager.transition.direction = 'left'
        pos_hint: {'center_x': 0.33, 'center_y': 0.3}
        
    MDRoundFlatButton:
        text: 'Back'
        on_press: 
            root.manager.current= 'start'
            root.manager.transition.direction = 'right'
        pos_hint: {'center_x': 0.67, 'center_y': 0.3}
        theme_text_color: "ContrastParentBackground"
"""