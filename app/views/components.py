from typing import Tuple
import customtkinter as ctk
from components import *
from ui_settings import *
from PIL import Image

class Button(ctk.CTkButton):
    def __init__(self,parent, func,text:str,col:int,row:int,sticky:str,padx:int=0,pady:int=0,span=1,color='blue-sky'):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            width=70,
            height=40,
            corner_radius=STYLING['button-corner-radius'],
            fg_color=COLORS[color]['fg'],
            hover_color=COLORS[color]['hover'],
            text_color=COLORS[color]['text'],
            font=(FONT,BUTTON_FONT_SIZE) 
        )
        self.grid(column=col,columnspan=span,row=row,sticky=sticky,padx=padx,pady=pady)


class Text(ctk.CTkLabel):
    def __init__(self,parent, text, col,span,row,size,weight,sticky,color='text'):
        super().__init__(
            master=parent,
            font=(FONT,size,weight),
            text=text,             
            text_color=COLORS['text-color'][color],           
        )
        self.grid(column=col,columnspan=span,row=row,sticky=sticky)



class EntryField(ctk.CTkEntry):
    def __init__(self, parent, width,placeholder_text,size,col,span,row,sticky):
        super().__init__(
            master=parent,
            width=width,
            height=30,
            corner_radius=STYLING['button-corner-radius'],
            border_width=0,  
            fg_color='#ECEDF2',            
            text_color='#4B5563',
            placeholder_text_color = '#7B7B7B', 
            placeholder_text=placeholder_text,
            font=(FONT,size),
           )
        self.grid(column=col,columnspan=span,row=row,sticky=sticky)


class OptionMenu(ctk.CTkOptionMenu):
    def __init__(self, parent,width,height,button_hover_color ,values, col, span,row,sticky):
        super().__init__(master=parent,width=width,height=height,corner_radius=5,
                         bg_color="transparent",fg_color='#fff', 
                         button_color='#fff',button_hover_color=button_hover_color, 
                         text_color='#00A0FF',dropdown_fg_color='#fff',
                         dropdown_hover_color='#eee',dropdown_text_color='#303030',
                         font=(FONT,15),dropdown_font=(FONT,13), 
                         values=values,dynamic_resizing=True)
        self.grid(column=col,columnspan=span,row=row,sticky=sticky)       

class OptionMenuHeader(ctk.CTkOptionMenu):
    def __init__(self, parent,width,height,button_hover_color ,values, col, span,row,sticky):
        super().__init__(master=parent,width=width,height=height,corner_radius=5,
                         bg_color="transparent",fg_color=COLORS['primary']['fg'], 
                         button_color=COLORS['primary']['fg'],button_hover_color=button_hover_color, 
                         text_color='#fff',dropdown_fg_color='#fff',
                         dropdown_hover_color='#eee',dropdown_text_color='#303030',
                         font=('poppins',15,'normal'),dropdown_font=(FONT,13), 
                         values=values,dynamic_resizing=True)
        self.grid(column=col,columnspan=span,row=row,sticky=sticky) 
    
    
class Frame(ctk.CTkFrame):
    def __init__(self,parent, width,height,col,span,row,sticky,fg_color="#FFF"):
        super().__init__(master=parent,
                         width=width, 
                         height=height,
                         corner_radius=15,
                         border_width=0,                           
                         fg_color=fg_color, 
                         border_color=None,
                         )
        
        self.grid(column=col,columnspan=span,row=row,sticky=sticky)


class HeaderFrame(ctk.CTkFrame):
    def __init__(self,parent, width,height,col,span,row,sticky,fg_color="#FFF"):
        super().__init__(master=parent,width=width,height=height,                        
                         border_width=0,                           
                         fg_color=fg_color, 
                         border_color=None,
                         corner_radius=0
                         )
        
        self.grid(column=col,columnspan=span,row=row,sticky=sticky)
                
    
class ImageLabel(ctk.CTkLabel):
    def __init__(self, parent , width:int, height:int, corner_radius:int ,text, image:str, col:int,row:int,sticky:str ,span :int=1, compound: str = "center"):
        super().__init__(master=parent, width=width, height=height, text=text,corner_radius=corner_radius,image=image, compound=compound)
        self.grid(column=col,columnspan=span,row=row,sticky=sticky)
