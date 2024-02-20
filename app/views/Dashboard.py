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
        
        #self.resizable(width=False, height=False) 
        
        self.state("zoomed")
        
        display_width= self.winfo_screenwidth()
        display_height =self.winfo_screenheight()
        
        minimalWidth=int(self.winfo_screenwidth()*0.95)
        minimalHeight=int(self.winfo_screenheight()*0.95)
        
        self.minsize(minimalWidth,minimalHeight)
        self.geometry(f'{minimalWidth}x{minimalHeight}+0+0')
        
         
              
        #security event
        self.bind('<Escape>', lambda event:self.quit())
    
        ctk.set_appearance_mode('light')
        
        self.columnconfigure((0,1),weight=1)
     
        self.rowconfigure((0,1,3),weight=1)
        self.rowconfigure(2,weight=6)
        
        self.create_widgets()
    
    
    def create_widgets(self):
        
        display_width= self.winfo_screenwidth()
        display_height =self.winfo_screenheight()
        
        
        self.create_navbar(display_width,display_height)
        self.create_title_bar(display_width)
        self.create_main_frame(display_width)
        self.create_footer_bar(display_width)
        
    def create_navbar(self,display_width,display_height):
        #header div
        self.headFrame = HeaderFrame(self,width=display_width,height=10,col=0,span=2,row=0,fg_color=COLORS['primary']['fg'],sticky='nsew')
        
        self.headFrame.columnconfigure(0,weight=8)
        self.headFrame.columnconfigure((1,2,3,4,5,6,7,8,9,10,11),weight=1)
        self.headFrame.rowconfigure(0,weight=1)    
        #importing the close icon image 
        self.logoImg = ctk.CTkImage(light_image=Image.open(IMAGE_LINKS['logoLepharma']) ,size=(200,50))
        
        self.logoFrame=ImageLabel(parent=self.headFrame,width=200,height=50,image=self.logoImg ,text='' ,corner_radius=0,span=1,col=0,row=0,sticky='ew')
        
        #Option Menu for the header               
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["Tableau de Bord", "Vendeur(se)"],col=4,span=1,row=0,sticky='e')
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["Ventes", "Vendeur(se)"],col=5,span=1,row=0,sticky='e')
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["Produits", "Vendeur(se)"],col=6,span=1,row=0,sticky='e')
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["Stocks", "Vendeur(se)"],col=7,span=1,row=0,sticky='e')
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["Rapports", "Vendeur(se)"],col=8,span=1,row=0,sticky='e')
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["Clients", "Vendeur(se)"],col=9,span=1,row=0,sticky='e')
           
        self.logoImg = ctk.CTkImage(light_image=Image.open(IMAGE_LINKS['userProfile']) ,size=(40,40))
        self.logoFrame=ImageLabel(parent=self.headFrame,width=50,height=50,image=self.logoImg ,text='' ,corner_radius=0,col=10,row=0,sticky='e')
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["","Utilisateurs","Notification","Parametre","Deconnexion"],col=11,span=1,row=0,sticky='w')
        
    def create_title_bar(self,display_width):
        self.frame = HeaderFrame(self,width=display_width,height=70,col=0,span=2,row=1,sticky='nsew',fg_color=COLORS['light']['fg'])
        
        #configure the column and rows
        self.frame.columnconfigure((0,1,2,3,4),weight=1)
        self.frame.rowconfigure(0,weight=1)
        
        #main title helps to know where we are     
        self.title = Text(self.frame,text="Clients  > Liste Des Clients",col=0,row=0,size=TITLE_FONT_SIZE,weight='bold',span=1,sticky='ws',color='title',padx=(50,0))
        
      
        self.addClient=Button(self.frame,text='Ajouter un client',color='blue-sky',col=4,row=0,span=1,func=lambda :print("hello"),sticky='es')
        
    
    def create_main_frame(self,display_width):
        self.headFrame = HeaderFrame(self,width=display_width,height=10,col=0,span=2,row=2,fg_color=COLORS['light']['fg'],sticky='ew')
        self.create_filter_frame()
        #self.create_list_frame()
        
    def create_filter_frame(self):
        #filter frame
        self.filterFrame = Frame(self.headFrame,width=350,height=590,col=0,span=1,row=1,sticky='w',padx=(50,0))
        self.filterFrame.grid_propagate(False)
        self.filterFrame.columnconfigure(0,weight=1)
        self.filterFrame.rowconfigure((0,1,2,3,4,5,6),weight=1)      
        
        self.filterTitle = Text(self.filterFrame,"Filtrer Par",0,1,0,15,'bold','ew')
        self.val = EntryFieldFrame(self.filterFrame,width=200,height=40,col=0,placeholder="Nom du client",span=1,row=1,sticky='we',padx=20)
    
    
    
    
    
        
    def create_list_frame(self):   
        #list frame
        self.frame = Frame(self.headFrame,width=1000,height=590,col=1,span=1,row=1,sticky='es',padx=(40,0))
     
    def create_footer_bar(self,display_width):
        self.headFrame = HeaderFrame(self,width=display_width,height=50,col=0,span=2,row=3,fg_color=COLORS['orange']['fg'],sticky='sew')
        
if __name__ == "__main__":
    Dashboard().mainloop()