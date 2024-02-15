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


class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='#F1F4F8')
        
        
        self.resizable(width=False, height=False) 
        self.attributes('-topmost',True)
        
        display_width= self.winfo_screenwidth()
        display_height =self.winfo_screenheight()
        
        window_width = 600
        window_height = 400
        
        left = int(display_width / 2 - window_width/2)
        top = int(display_height / 2 - window_height/2)
        
        self.geometry(f'{display_width}x{display_height}+0+0')
        
        #mask off the title bar
        self.overrideredirect(0)        
        #security event
        self.bind('<Escape>', lambda event:self.quit())
    
        ctk.set_appearance_mode('light')
        
        self.columnconfigure((0,1),weight=1)
        self.rowconfigure((0,1,2),weight=1)
        
        self.frame = Frame(self,width=400,height=700,col=0,span=1,row=1,sticky='w')
        self.frame = Frame(self,width=400,height=700,col=1,span=1,row=1,sticky='w')
        
     

if __name__ == "__main__":
    Dashboard().mainloop()