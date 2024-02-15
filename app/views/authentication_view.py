# app/views/authentication_view.py
from tkinter.constants import NORMAL
from typing import Tuple
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
        super().__init__(fg_color='#fff')
        
        
        self.resizable(width=False, height=False) 
        self.attributes('-topmost',True)
        
        display_width= self.winfo_screenwidth()
        display_height =self.winfo_screenheight()
        
        window_width = 600
        window_height = 400
        
        left = int(display_width / 2 - window_width/2)
        top = int(display_height / 2 - window_height/2)
        
        self.geometry(f'{window_width}x{window_height}+{left}+{top}')
        
        #mask off the title bar
        self.overrideredirect(1)        
        #security event
        self.bind('<Escape>', lambda event:self.quit())
    
        ctk.set_appearance_mode('light')
        
        #importing the login image 
        self.loginImage = ctk.CTkImage(light_image=Image.open('D:\\Work\\Projet GEKATON\\Projet LEPHARMA\\codage\\Lepharma Software\\app\\images\\login.png') ,size=(273,400))
        
        #importing the close icon image 
        self.closeIcon = ctk.CTkImage(light_image=Image.open('D:\\Work\\Projet GEKATON\\Projet LEPHARMA\\codage\\Lepharma Software\\app\\images\\closeIcon.png') ,size=(15,15))
        
        self.frameImage = ctk.CTkFrame(self,width=273,height=400)
        self.frameImage.place(x=0,y=0)
        
        self.logiImgB = ctk.CTkLabel(
            self.frameImage,          
            text='',
            width=273,
            height=400,
            image=self.loginImage )
        
        self.logiImgB.pack(fill='both' ,expand=True)
        
        # frame form
        self.frameForm = ctk.CTkFrame(self,fg_color='#fff',width=287, height=400)
        self.frameForm.place(x=293,y=0)
        self.frameForm.grid_propagate(False)
        
        self.frameForm.columnconfigure(0,weight=1)
        self.frameForm.rowconfigure(0,weight=3)
        self.frameForm.rowconfigure((1,2,3,4,5,6,7,8,9,10),weight=1)
                
        #------------------------- Layout --------------------------
        
        self.closeIconLabel = ctk.CTkLabel(
            self.frameForm,          
            text='',
            width=50,
            height=50,
            image=self.closeIcon )
        self.closeIconLabel.place(x=250,y=0)      
        
        #connexion title
        self.logTitle = Text(self.frameForm,text="Connexion",col=0,span=1,row=0,size=LOGIN_TITLE_FONT_SIZE,weight='normal',sticky='s',color='text-color')
        
        #option role
        self.optionLabel = Text(self.frameForm,text="Selectionnez le role",col=0,span=1,row=1,size=13,weight='normal',sticky='se',color='text-color')
        self.optionMenu2 = OptionMenu(self.frameForm,70,30,'#ECEDF2',values=["Pharmacien", "Vendeur(se)"],col=0,span=1,row=2,sticky='ne')
        
        #username label and entry
        self.usernameLabel = Text(self.frameForm,text="Nom d'utilisateur",col=0,span=1,row=3,size=13,weight='normal',sticky='ws',color='text-color')
        self.usernameEntry=EntryField(self.frameForm,150,'Inserez votre nom d\'utilisateur ',12,0,1,4,'new')
              
        #username label and entry
        self.passwordLabel = Text(self.frameForm,text="Mot de Passe",col=0,span=1,row=5,size=13,weight='normal',sticky='ws',color='text-color')
        self.passwordEntry=EntryField(self.frameForm,150,'Inserez votre mot de passe ',12,0,1,6,'new')
       
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
              
            font=ctk.CTkFont(family='Poppins',size=15, weight="bold", )
        )
        self.loginButton.grid(column=0 ,row=8,ipadx=10 ,ipady=5 , sticky='ew')
        
        
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