# app/views/authentication_view.py

import customtkinter as ctk
from components import *
from ui_settings import *
from PIL import Image

# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

class AuthenticationView(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='#eee')
        
        self.geometry('600x400')
        self.resizable(width=False, height=False)  
        
        self.title('Login To Lepharma')
        ctk.set_appearance_mode('light')
        
        self.loginImage = ctk.CTkImage(light_image=Image.open('D:\\Work\\Projet GEKATON\\Projet LEPHARMA\\codage\\Lepharma Software\\app\\images\\login.png') ,size=(273,400))
        
        

        self.frameImage = ctk.CTkFrame(self,width=273,height=400)
        self.frameImage.place(x=0,y=0)
        
       
        
        self.logiImgB = ctk.CTkLabel(
            self.frameImage,          
            text='',
            width=273,
            height=400,
            image=self.loginImage )
        
        self.logiImgB.pack(fill='both' ,expand=True)
        
        
        
        self.frameForm = ctk.CTkFrame(self,  fg_color='#fff',width=327, height=400)
        self.frameForm.place(x=273,y=0 )
        self.frameForm.grid_propagate(False)
        
        
        self.frameForm.columnconfigure(0,weight=1)
        self.frameForm.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
        
        self.loginTitle = ctk.CTkLabel(master=self.frameForm,text='Connexion',font=(FONT,LOGIN_TITLE_FONT_SIZE,'normal' ))
        self.loginTitle.grid(column=0,row=0,sticky="nsew")
        
        self.username_label = ctk.CTkLabel(master=self.frameForm,text='Nom d’utilisateur',font=(FONT,BUTTON_FONT_SIZE,'normal' ))
        self.username_label.grid(column=0,row=3,sticky="nsew")
        
        
        
        
        self.usernameEntry = customtkinter.CTkEntry(
            self.frameForm,
            placeholder_text="Inserez votre nom d'utilisateur",
            corner_radius=STYLING['button-corner-radius'],width=268,height=30,
            fg_color='#F5F6FA').grid(column=0 ,row=4)
        
        
        
        
        
        #button for login
        
        self.loginButton = ctk.CTkButton(
            self.frameForm,          
            text='Se Connecter',
            width=50,
            height=20,
            corner_radius=STYLING['button-corner-radius'],
            fg_color=COLORS['blue-sky']['fg'],
            hover_color=COLORS['blue-sky']['hover'],
            text_color=COLORS['blue-sky']['text'],
            font=(FONT,BUTTON_FONT_SIZE,'bold' ),
        )
        self.loginButton.grid(column=0 ,row=8,ipadx=40 ,ipady=5)
        
        
        
        
        
        
        
        
        
        
        
        
    def greet(self):
        print("hey how are you ?")    
        
        # Button(self,parent=self,func=self.greet,text='Login',col=0,row=1)
        
        
        
 


    # def authenticate_user(self):
    #     username = self.username_entry.get()
    #     password = self.password_entry.get()command=self.authenticate_user

    #     result = AuthenticationController.authenticate_user(username, password)
    #     if result["success"]:
           # self.destroy()   Close the login window
            #ProductView().mainloop()   Open the main application window
        # else:
        #     print(f"Error: {result['message']}")

if __name__ == "__main__":
    AuthenticationView().mainloop()


 