navigation_helper = """
ScreenManager:
    StartScreen:
    NewProfileScreen:
    ProfileCreatedScreen:
    AccExistScreen:
    LoginScreen:
    LoggedInScreen:
    AdoptNowScreen:
    AdoptionAppealScreen:
    AdopterFormScreen:
    DonationScreen:
    ResourcesScreen:
    UserQueryScreen:

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
                        title: "Bangalore Animal Welfare"
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
        pos_hint: {'center_y': 0.73}
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
        pos_hint: {'center_y': 0.73}
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
        pos_hint: {'center_x': 0.33, 'center_y': 0.4}
        
    MDRoundFlatButton:
        text: 'Back'
        on_press: 
            root.manager.current= 'start'
            root.manager.transition.direction = 'right'
        pos_hint: {'center_x': 0.67, 'center_y': 0.4}
        theme_text_color: "ContrastParentBackground"
        
<LoggedInScreen>:
    name: 'loggedin'
    
    ScrollView:
        size_hint_y: None
        size_hint_x: 1
        size: root.size
        
        GridLayout:
            cols: 1
            size_hint_y: None
            height: 1735
            padding: "15dp"
            spacing: '8dp'
            
            MDLabel:
                text: "   "
                size_hint: 0.5, 0.06
            MDLabel:
                text: "Oops! No more page to load"
                size_hint: 0.5, 0.08
            
            MDCard:
                orientation: 'vertical'
                padding: '7dp'
                size_hint_x: .72
                pos_hint: {'center_x': 0.5, 'top': 0.6}
                elevation: 9
                radius: [10, 10, 10, 10]
                on_press: 
                    root.checkcurrent()
                FitImage:
                    id: 'adopt_img'
                    source: "dog1.jpg"
                    pos_hint: {'top': 1}
                    allow_stretch: True
                    keep_ratio: False
                MDLabel:
                    text: 'Adopt Now'
                    size_hint_y: .2
                    pos_hint: {'center_x': 0.5}
                        
            MDCard:
                orientation: 'vertical'
                padding: '7dp'
                size_hint_x: .72
                pos_hint: {'center_x': 0.5, 'top': 1}
                elevation: 9
                radius: [10, 10, 10, 10]
                on_press: 
                    root.manager.current= 'appeal'
                    root.manager.transition.direction = 'left'
                FitImage:
                    id: 'appeal_img'
                    source: "img.png"
                    pos_hint: {'top': 1}
                    allow_stretch: True
                    keep_ratio: False
                MDLabel:
                    text: 'Post an Adoption Appeal'
                    size_hint_y: .2
                    pos_hint: {'center_x': 0.5}
            
            MDCard:
                orientation: 'vertical'
                padding: '7dp'
                size_hint_x: .72
                pos_hint: {'center_x': 0.5, 'top': 1}
                elevation: 9
                radius: [10, 10, 10, 10]
                on_press: 
                    root.manager.current= 'donation'
                    root.manager.transition.direction = 'left'
                FitImage:
                    id: 'donate_img'
                    source: "donate.jpg"
                    pos_hint: {'top': 1}
                    allow_stretch: True
                    keep_ratio: False
                MDLabel:
                    text: 'Donate to a good cause'
                    size_hint_y: .2
                    pos_hint: {'center_x': 0.5}
            
            MDCard:
                orientation: 'vertical'
                padding: '7dp'
                size_hint_x: .72
                pos_hint: {'center_x': 0.5, 'top': 1}
                elevation: 9
                radius: [10, 10, 10, 10]
                on_press: 
                    root.manager.current= 'resources'
                    root.manager.transition.direction = 'left'
                FitImage:
                    id: 'donate_img'
                    source: "helpline.jpg"
                    pos_hint: {'top': 1}
                    allow_stretch: True
                    keep_ratio: False
                MDLabel:
                    text: 'Resources & Helplines'
                    size_hint_y: .2
                    pos_hint: {'center_x': 0.5}
            
            MDCard:
                orientation: 'vertical'
                padding: '7dp'
                size_hint_x: .72
                pos_hint: {'center_x': 0.5, 'top': 1}
                elevation: 9
                radius: [10, 10, 10, 10]
                on_press: 
                    root.manager.current= 'queries'
                    root.manager.transition.direction = 'left'
                FitImage:
                    id: 'query_img'
                    source: "query.jpg"
                    pos_hint: {'top': 1}
                    allow_stretch: True
                    keep_ratio: False
                MDLabel:
                    text: 'Ask us your Questions'
                    size_hint_y: .2
                    pos_hint: {'center_x': 0.5}
                               
            MDFillRoundFlatIconButton:
                text: 'Log Out'
                icon: 'account-cancel'
                on_press: 
                    root.manager.current= 'start'
                    root.manager.transition.direction = 'right'
                pos_hint: {'center_x': 0.5, 'top': 1}

    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Home"
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
                    text: '  Home'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        spacing: '8dp'
                        padding: '8dp'
                    
                        MDRectangleFlatIconButton:
                            text: 'Log Out'
                            on_press: 
                                root.manager.current= 'start'
                                root.manager.transition.direction = 'right'
                            icon: 'account-cancel-outline'
                            theme_text_color: 'Hint'

<AdoptNowScreen>:
    name: 'adoptnow'
    
    MDBoxLayout:
        orientation:"vertical"            
        MDBoxLayout:
            orientation: 'vertical'
        
            MDLabel:
                text: 'Something'
                size_hint: 0.1, 0.15
        
            ScrollView:
                MDGridLayout:
                    cols:2
                    padding:dp(2)
                    spacing:dp(10)
                    adaptive_height:True
                    ElementCard:
                        image:'dog1.jpg'
                        MDLabel:
                            text:"Name:milky Age:5months"
                            font_size: dp(10)
                            size_hint: 0.8, 0.8
                            pos_hint: {"center_x": 0.23,"center_y": 0.3}


                        MDFillRoundFlatButton:
                            text:"adopt/foster"
                            font_size: dp(10)
                            pos_hint: {"center_x": 0.5,"center_y": 0.08}
                            on_release:root.show_button()                        
                        
                        
                    ElementCard:
                        image:'dog1.jpg'
                        MDLabel:
                            text:"Name:Cookie  Age:5months"
                            font_size: dp(10)
                            size_hint: 0.8, 0.8
                            pos_hint: {"center_x": 0.23,"center_y": 0.3}
                            


                        MDRaisedButton:
                            text:"adopt/foster"
                            font_size: dp(10)
                            pos_hint: {"center_x": 0.5,"center_y": 0.08}
                            on_release:root.show_button()
                            

                        
                    ElementCard:
                        image:'dog1.jpg'
                        MDLabel:
                            text:"Name:boky  Age:5months"
                            font_size: dp(10)
                            size_hint: 0.8, 0.8
                            pos_hint: {"center_x": 0.23,"center_y": 0.3}
                            


                        MDRaisedButton:
                            text:"adopt/foster"
                            font_size: dp(10)
                            pos_hint: {"center_x": 0.5,"center_y": 0.08}
                            on_release:
                                root.show_button()
                                
                                root.manager.transition.direction = 'right'
                        
                    ElementCard:
                        image:'dog1.jpg'
                        MDLabel:
                            text:"Name:Tan  Age:5months"
                            font_size: dp(10)
                            size_hint: 0.8, 0.8
                            pos_hint: {"center_x": 0.23,"center_y": 0.3}


                        MDRaisedButton:
                            text:"adopt/foster"
                            font_size: dp(10)
                            pos_hint: {"center_x": 0.5,"center_y": 0.08}
                            on_release:root.show_button()
                        
                    ElementCard:
                        image:'dog1.jpg'
                        MDLabel:
                            text:"Name:Bhutan  Age:14months"
                            font_size: dp(10)
                            size_hint: 0.8, 0.8
                            pos_hint: {"center_x": 0.23,"center_y": 0.3}


                        MDRaisedButton:
                            text:"adopt/foster"
                            font_size: dp(10)
                            pos_hint: {"center_x": 0.5,"center_y": 0.08}
                            on_release:root.show_button()
                        
                    ElementCard:
                        image:'dog1.jpg'
                        MDLabel:
                            text:"Name:Askya    Age:1 year"
                            font_size: dp(10)
                            size_hint: 0.8, 0.8
                            pos_hint: {"center_x": 0.23,"center_y": 0.3}


                        MDRaisedButton:
                            text:"adopt/foster"
                            font_size: dp(10)
                            pos_hint: {"center_x": 0.5,"center_y": 0.08}
                            on_release:root.show_button()
                        
        # bottom navigation appbar
        MDBoxLayout:
            size_hint_y:None
            md_bg_color:.9,.9,.9,1
            height:dp(60)
            padding:[0,0,0,15]
            MDBoxLayout:
                orientation:'vertical'
                MDIconButton:
                    pos_hint:{'center_x':.5,'center_y':.5}
                    icon:'home'
                    on_release:
                        root.manager.current= 'loggedin'
                        root.manager.transition.direction = 'right'
                    theme_text_color:'Custom'
                    text_color:app.theme_cls.primary_color
                    
                MDLabel:
                    text:'Home'
                    valign:"center"
                    theme_text_color:'Custom'
                    text_color:app.theme_cls.primary_color
                    halign:"center"
        
    
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Adopt Now"
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
                    text: '  Adopt Now'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        spacing: '8dp'
                        padding: '8dp'
                    
                        MDRectangleFlatIconButton:
                            text: 'Log Out'
                            on_press: 
                                root.manager.current= 'start'
                                root.manager.transition.direction = 'right'
                            icon: 'account-cancel-outline'
                            theme_text_color: 'Hint'
                        
<AdoptionAppealScreen>:
    name: 'appeal'
                  
    MDRelativeLayout:
        size_hint: None, None
        size: root.size
        
        MDFillRoundFlatButton:
            text: 'Back to Home'
            on_press: 
                root.manager.current= 'loggedin'
                root.manager.transition.direction = 'right'
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                        
        # bottom navigation appbar
        MDBoxLayout:
            size_hint_y:None
            md_bg_color:.9,.9,.9,1
            height:dp(60)
            padding:[0,0,0,15]
            MDBoxLayout:
                orientation:'vertical'
                MDIconButton:
                    pos_hint:{'center_x':.5,'center_y':.5}
                    icon:'home'
                    on_release:
                        root.manager.current= 'loggedin'
                        root.manager.transition.direction = 'right'
                    theme_text_color:'Custom'
                    text_color:app.theme_cls.primary_color
                    
                MDLabel:
                    text:'Home'
                    valign:"center"
                    theme_text_color:'Custom'
                    text_color:app.theme_cls.primary_color
                    halign:"center"
        
          
        
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Post Adoption Appeal"
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
                    text: '  Post an Adoption Appeal'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        spacing: '8dp'
                        padding: '8dp'
                    
                        MDRectangleFlatIconButton:
                            text: 'Log Out'
                            on_press: 
                                root.manager.current= 'start'
                                root.manager.transition.direction = 'right'
                            icon: 'account-cancel-outline'
                            theme_text_color: 'Hint'

<AdopterFormScreen>:
    name: 'adopterform'
        
    MDTextField:
        id: fullName
        hint_text: "Enter your full name"
        pos_hint: {'center_x': 0.5, 'center_y': 0.75}
        size_hint_x: None
        width: 200
    
    MDTextField:
        id: ph_number
        hint_text: "Enter your mobile number"
        helper_text: ""
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        size_hint_x: None
        width: 200
        
    MDTextField:
        id: haspet
        hint_text: "Do you already have a pet?"
        helper_text: "Yes/No"
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
        size_hint_x: None
        width: 200
    
    MDTextField:
        id: adoptorfoster
        hint_text: "Will you adopt or foster?"
        helper_text: "Adopt/Foster"
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        size_hint_x: None
        width: 200
    
    MDTextField:
        id: flatorind
        hint_text: "Do you live in a flat or independant??"
        helper_text: "Flat/Independant"
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        size_hint_x: None
        width: 200

    MDRoundFlatButton:
        text: 'Register'
        on_press:
            root.submitdetails()
            root.manager.current= 'loggedin'
            root.manager.transition.direction = 'right'
        pos_hint: {'center_x': 0.33, 'center_y': 0.25}
        
    MDRoundFlatButton:
        text: 'Back'
        on_press: 
            root.manager.current= 'loggedin'
            root.manager.transition.direction = 'right'
        pos_hint: {'center_x': 0.67, 'center_y': 0.25}
        theme_text_color: "ContrastParentBackground"
    
    
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Post Adoption Appeal"
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
                    text: '  Home'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        spacing: '8dp'
                        padding: '8dp'
                    
                        MDRectangleFlatIconButton:
                            text: 'Log Out'
                            on_press: 
                                root.manager.current= 'start'
                                root.manager.transition.direction = 'right'
                            icon: 'account-cancel-outline'
                            theme_text_color: 'Hint'                   

<DonationScreen>:
    name: 'donation'
    
    MDRelativeLayout:
        size_hint: None, None
        size: root.size
        
        MDFillRoundFlatButton:
            text: 'Back to Home'
            on_press: 
                root.manager.current= 'loggedin'
                root.manager.transition.direction = 'right'
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                        
        # bottom navigation appbar
        MDBoxLayout:
            size_hint_y:None
            md_bg_color:.9,.9,.9,1
            height:dp(60)
            padding:[0,0,0,15]
            MDBoxLayout:
                orientation:'vertical'
                MDIconButton:
                    pos_hint:{'center_x':.5,'center_y':.5}
                    icon:'home'
                    on_release:
                        root.manager.current= 'loggedin'
                        root.manager.transition.direction = 'right'
                    theme_text_color:'Custom'
                    text_color:app.theme_cls.primary_color
                    
                MDLabel:
                    text:'Home'
                    valign:"center"
                    theme_text_color:'Custom'
                    text_color:app.theme_cls.primary_color
                    halign:"center"
        
          
        
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Donate"
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
                    text: '  Donate'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        spacing: '8dp'
                        padding: '8dp'
                    
                        MDRectangleFlatIconButton:
                            text: 'Log Out'
                            on_press: 
                                root.manager.current= 'start'
                                root.manager.transition.direction = 'right'
                            icon: 'account-cancel-outline'
                            theme_text_color: 'Hint'
                            
<ResourcesScreen>:
    name: 'resources'
    
    MDRelativeLayout:
        size_hint: None, None
        size: root.size
        
        MDFillRoundFlatButton:
            text: 'Back to Home'
            on_press: 
                root.manager.current= 'loggedin'
                root.manager.transition.direction = 'right'
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                        
        # bottom navigation appbar
        MDBoxLayout:
            size_hint_y:None
            md_bg_color:.9,.9,.9,1
            height:dp(60)
            padding:[0,0,0,15]
            MDBoxLayout:
                orientation:'vertical'
                MDIconButton:
                    pos_hint:{'center_x':.5,'center_y':.5}
                    icon:'home'
                    on_release:
                        root.manager.current= 'loggedin'
                        root.manager.transition.direction = 'right'
                    theme_text_color:'Custom'
                    text_color:app.theme_cls.primary_color
                    
                MDLabel:
                    text:'Home'
                    valign:"center"
                    theme_text_color:'Custom'
                    text_color:app.theme_cls.primary_color
                    halign:"center"
        
          
        
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Resources & Helplines"
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
                    text: '  Resources & Helplines'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        spacing: '8dp'
                        padding: '8dp'
                    
                        MDRectangleFlatIconButton:
                            text: 'Log Out'
                            on_press: 
                                root.manager.current= 'start'
                                root.manager.transition.direction = 'right'
                            icon: 'account-cancel-outline'
                            theme_text_color: 'Hint'

<UserQueryScreen>:
    name: 'queries'
    
    MDRelativeLayout:
        size_hint: None, None
        size: root.size
        
        MDFillRoundFlatButton:
            text: 'Back to Home'
            on_press: 
                root.manager.current= 'loggedin'
                root.manager.transition.direction = 'right'
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                        
        # bottom navigation appbar
        MDBoxLayout:
            size_hint_y:None
            md_bg_color:.9,.9,.9,1
            height:dp(60)
            padding:[0,0,0,15]
            MDBoxLayout:
                orientation:'vertical'
                MDIconButton:
                    pos_hint:{'center_x':.5,'center_y':.5}
                    icon:'home'
                    on_release:
                        root.manager.current= 'loggedin'
                        root.manager.transition.direction = 'right'
                    theme_text_color:'Custom'
                    text_color:app.theme_cls.primary_color
                    
                MDLabel:
                    text:'Home'
                    valign:"center"
                    theme_text_color:'Custom'
                    text_color:app.theme_cls.primary_color
                    halign:"center"
        
          
        
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Ask us a Question"
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
                    text: '  Ask us a question'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        spacing: '8dp'
                        padding: '8dp'
                    
                        MDRectangleFlatIconButton:
                            text: 'Log Out'
                            on_press: 
                                root.manager.current= 'start'
                                root.manager.transition.direction = 'right'
                            icon: 'account-cancel-outline'
                            theme_text_color: 'Hint'

<ElementCard@MDCard>:
    image:''
    
    orientation:'vertical'
    
    size_hint_x:.5
    elevation:15
    size_hint_y:None
    md_bg_color:app.theme_cls.primary_color
    height:dp(220)
    padding:dp(25)
    spacing:dp(15)
    radius:[25]
    MDBoxLayout:
        height:dp(120)
        size_hint_y:None
        Image:
            source:root.image

"""
