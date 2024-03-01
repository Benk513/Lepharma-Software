# app/views/authentication_view.py
from tkinter.constants import NORMAL
from typing import Tuple
import customtkinter as ctk
from components import *
from ui_settings import *
from PIL import Image
from product_view import *
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
     
        self.rowconfigure((0,1,3),weight=1,uniform='a')
        self.rowconfigure(2,weight=6,uniform='a')
        
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
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["Ventes","Point de Vente","Factures", "Historique de Vente"],col=5,span=1,row=0,sticky='e')
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["Produits", "Ajouter un Produit","Produits Perimés"],col=6,span=1,row=0,sticky='e')
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["Stocks","Ajouter un Stock" ,"Inventaire"],col=7,span=1,row=0,sticky='e')
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["Rapports", "Vendeur(se)"],col=8,span=1,row=0,sticky='e')
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["Clients","Ajouter","Debiteurs"],col=9,span=1,row=0,sticky='e')
           
        self.logoImg = ctk.CTkImage(light_image=Image.open(IMAGE_LINKS['userProfile']) ,size=(40,40))
        self.logoFrame=ImageLabel(parent=self.headFrame,width=50,height=50,image=self.logoImg ,text='' ,corner_radius=0,col=10,row=0,sticky='e')
        OptionMenuHeader(self.headFrame,40,30,COLORS['primary']['hover'],values=["","Utilisateurs","Notification","Parametre","Deconnexion"],col=11,span=1,row=0,sticky='w')
        
    def create_title_bar(self,display_width):
        self.frame = HeaderFrame(self,width=display_width,height=70,col=0,span=2,row=1,sticky='nsew',fg_color=COLORS['white']['fg'])
        
        #configure the column and rows
        self.frame.columnconfigure(0,weight=4)
        self.frame.columnconfigure((1,2),weight=2)
        self.frame.columnconfigure((3,4),weight=1)
        self.frame.rowconfigure(0,weight=1)
        
        #main title helps to know where we are     
        self.navigationTitle("Ventes","Statistiques")
        #self.addbuttonswidgets()
        
    def navigationTitle(self,main,sub):
        # main ="Clients"
        # sub="Liste des clients"
        text = main+"  >  "+sub
        self.title = Text(self.frame,text=text,col=0,row=0,size=TITLE_FONT_SIZE,weight='bold',span=3,sticky='ws',color='title',padx=(50,0))    
    def addbuttonswidgets(self): 
        self.addClient=Button(self.frame,text='Ajouter un client',color='blue-sky',col=4,row=0,span=1,func=lambda :print("hello"),sticky='es',padx=(10,100),pady=(20,0))
        self.exportClientsXls=Button(self.frame,text='Exporter en .xlsx ',color='gray',col=3,row=0,span=1,func=lambda :print("hello"),sticky='es',padx=10,pady=(20,0))
        
         #importing the close icon image 
        self.searchIcon = ctk.CTkImage(light_image=Image.open(IMAGE_LINKS['searchIcon']) ,size=(25,25))
        self.rechercherClient = EntryFieldFrame(self.frame,width=150,height=40,col=2,placeholder="Nom du client",span=1,row=0,sticky='swe',padx=20,buttonSticky='e',icon=self.searchIcon,border_width=2,border_color=COLORS['entryFieldColor'],pady=(20,0))
        
    
    def create_main_frame(self,display_width):
        self.headFrame = HeaderFrame(self,width=display_width,height=10,col=0,span=2,row=2,fg_color=COLORS['light']['fg'],sticky='ew',pady=(20,0))
        # self.create_list_frame()
        # self.create_filter_frame()
        #self.create_add_client_frame()
        #self.create_list_clients()
        self.productview=ProductView().create_add_product_frame(self.headFrame)    
    


    def create_footer_bar(self,display_width):
        self.headFrame = HeaderFrame(self,width=display_width,height=50,col=0,span=2,row=3,fg_color=COLORS['white']['fg'],sticky='sew')
        
if __name__ == "__main__":
    Dashboard().mainloop()