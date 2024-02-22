from tkinter.constants import NORMAL
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
    def __init__(self,parent, text, col,span,row,size,weight,sticky,color='text',padx=0,pady=0):
        super().__init__(
            master=parent,
            font=(FONT,size,weight),
            text=text,             
            text_color=COLORS['text-color'][color],           
        )
        self.grid(column=col,columnspan=span,row=row,sticky=sticky,padx=padx,pady=pady)


class EntryField(ctk.CTkEntry):
    def __init__(self, parent, width,placeholder_text,size:int,col:int,row:int,sticky:str,span:int=1,fg_color='#ECEDF2',border_width=0,corner_radius=STYLING['button-corner-radius'],height=30,border_color='#fff',padx=0,pady=0):
        super().__init__(
            master=parent,
            width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,  
            fg_color=fg_color,            
            text_color='#4B5563',
            placeholder_text_color = '#7B7B7B', 
            placeholder_text=placeholder_text,
            font=(FONT,size),
            border_color=border_color
           )
        self.grid(column=col,columnspan=span,row=row,sticky=sticky,padx=padx,pady=pady)


class IconButton(ctk.CTkButton):
    def __init__(self,parent,image, func,text:str,col:int,row:int,sticky:str,width=40, height=40,padx:int=0,pady:int=0,span=1,color='blue-sky'):
        super().__init__(
            master=parent,
            command=func,
            text=text,
            width=width,
            height=height,
            corner_radius=STYLING['button-corner-radius'],
            fg_color=COLORS[color]['fg'],
            hover_color=COLORS[color]['hover'],
            text_color=COLORS[color]['text'],
            font=(FONT,BUTTON_FONT_SIZE),
            image=image
        )
        self.grid(column=col,columnspan=span,row=row,sticky=sticky,padx=padx,pady=pady)


class EntryFieldFrame(ctk.CTkFrame):
    def __init__(self,parent, width,col,placeholder,span,row,sticky,icon,buttonSticky,fg_color="#FFF",padx=0,pady=0,border_color='#fff',border_width=0,height=40):
        super().__init__(master=parent,
                         width=width, 
                         height=height,
                         corner_radius=15,
                         border_width=border_width,                           
                         fg_color=fg_color, 
                         border_color=border_color,
                         
                         )
        self.rowconfigure(0,weight=3)
        self.columnconfigure((0,1),weight=1)
        self.grid_propagate(False)

        
        #entry field
        self.entry = EntryField(parent=self,width=180,placeholder_text=placeholder,size=15,col=0,span=1,row=0,sticky='ew',fg_color='#fff',border_width=0,border_color="#B6BDCA",corner_radius=12,height=30,padx=(10,0))
        
        #button with icon here
        
        self.button=IconButton(parent=self,image=icon,text='',func=lambda :print('button clicked'),col=1,row=0,sticky=buttonSticky,color='white',width=10,height=10,padx=(0,10))
         
        self.grid(column=col,columnspan=span,row=row,sticky=sticky,padx=padx,pady=pady)
 
        
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
    def __init__(self,parent, width,height,col,span,row,sticky,fg_color="#FFF",padx=0,pady=0):
        super().__init__(master=parent,
                         width=width, 
                         height=height,
                         corner_radius=15,
                         border_width=0,                           
                         fg_color=fg_color, 
                         border_color=None,
                         )
        
        self.grid(column=col,columnspan=span,row=row,sticky=sticky,padx=padx,pady=pady)


class HeaderFrame(ctk.CTkFrame):
    def __init__(self,parent, width,height,col,span,row,sticky,fg_color="#FFF" ,padx=0,pady=0):
        super().__init__(master=parent,width=width,height=height,                        
                         border_width=0,                           
                         fg_color=fg_color, 
                         border_color=None,
                         corner_radius=0
                         )
        
        self.grid(column=col,columnspan=span,row=row,sticky=sticky,padx=padx,pady=pady)
                
                 
class ImageLabel(ctk.CTkLabel):
    def __init__(self, parent , width:int, height:int, corner_radius:int ,text, image:str, col:int,row:int,sticky:str ,span :int=1, compound: str = "center"):
        super().__init__(master=parent, width=width, height=height, text=text,corner_radius=corner_radius,image=image, compound=compound)
        self.grid(column=col,columnspan=span,row=row,sticky=sticky)


class RadioButton(ctk.CTkRadioButton):
    def __init__(self, 
                 parent, func,
                 width: int = 100,
                 height: int = 30,
                 border_width_unchecked=5, 
                 border_width_checked=5,         
                 fg_color: str | Tuple[str, str] | None = None, 
                 border_color:str="#B6BDCA",
                 text_color: str | Tuple[str, str] | None = None,
                 text: str = "nom de radio button",
                 size:int=13,                 
                 textvariable: None = None, 
                 variable:None = None, 
                 value:str = "put a value", 
                 state: str = "normal", #disabled #for changing the state of the button
                 hover: bool = True,
                 col=0,
                 span=1,
                 row=0,
                 sticky="w",
                 padx=0,
                 pady=0
                  ):
        super().__init__(master=parent,
                         width=width,
                         height=height,
                         border_width_unchecked=border_width_unchecked,
                         border_width_checked=border_width_checked,
                         fg_color=fg_color,
                         border_color=border_color,
                         text_color=text_color,
                         text=text,
                         textvariable=textvariable,
                         variable=variable,
                         value=value,
                         state=state,
                         hover=hover,
                         command=func,
                         font=(FONT,size))
        
        self.grid(column=col,columnspan=span,row=row,sticky=sticky,padx=padx,pady=pady)