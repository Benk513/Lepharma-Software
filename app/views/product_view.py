# app/views/product_view.py
from tkinter.constants import NORMAL
from typing import Tuple
import customtkinter as ctk
from components import *
from ui_settings import *
from PIL import Image

def create_add_product_frame(self):   
        #list frame
        self.frame = Frame(self.headFrame,width=1400,height=590,col=1,span=2,row=1,sticky='ew',padx=(40,40))
        self.frame.columnconfigure((0,1),weight=1,uniform='a')
        self.frame.columnconfigure((2,3),weight=1)
        self.frame.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1,uniform='a')
        self.frame.rowconfigure((7,8),weight=2)
        self.frame.grid_propagate(False)
        
        # #importing the close icon image 
        # self.searchIcon = ctk.CTkImage(light_image=Image.open(IMAGE_LINKS['searchIcon']) ,size=(25,25))
        # self.val = EntryFieldFrame(self.frame,width=100,height=50,col=0,placeholder="Nom du client",span=1,row=1,sticky='we',padx=20,buttonSticky='e',icon=self.searchIcon,border_width=2,border_color=COLORS['entryFieldColor'])
        
        #codebar
        self.codebarProduitLabel = Text(self.frame,text="Code Produit",col=0,span=1,row=1,size=15,weight='normal',sticky='ws',color='text',padx=(50,0))
        self.codebarProduitEntry=EntryField(self.frame,placeholder_text="inserer le code a bar",height=50,size=13,width=150,col=0,row=2,sticky="new",padx=50,border_width=2,border_color=COLORS['entryFieldColor'],fg_color='#fff')
        
        #designation
        self.designationL = Text(self.frame,text="Designation",col=0,span=1,row=3,size=15,weight='normal',sticky='ws',color='text',padx=50)
        self.designationE=EntryField(self.frame,placeholder_text="Inserez le nom du produit" ,height=50,size=13,width=150,col=0,row=4,sticky="new",padx=50,border_width=2,border_color=COLORS['entryFieldColor'],fg_color='#fff')
        

        #forme
        self.formeL = Text(self.frame,text="Forme",col=0,span=1,row=5,size=15,weight='normal',sticky='ws',color='text',padx=50)
        self.formeE=EntryField(self.frame,placeholder_text="inj ,sp,cès" ,height=50,size=13,width=150,col=0,row=6,sticky="new",padx=50,border_width=2,border_color=COLORS['entryFieldColor'],fg_color='#fff')
        
        #date d'expiration 
        self.formeL = Text(self.frame,text="Date d'Expiration",col=0,span=1,row=5,size=15,weight='normal',sticky='ws',color='text',padx=50)
        self.formeE=EntryField(self.frame,placeholder_text="Jour/Mois/Annee" ,height=50,size=13,width=150,col=0,row=6,sticky="new",padx=50,border_width=2,border_color=COLORS['entryFieldColor'],fg_color='#fff')

        
        #prixAchat
        self.prixAchatL = Text(self.frame,text="Prix d'Achat",col=1,span=1,row=1,size=15,weight='normal',sticky='ws',color='text',padx=20)
        self.prixAchatE=EntryField(self.frame,placeholder_text="Inserer le prix d'achat'" ,height=50,size=13,width=150,col=1,row=2,sticky="new",padx=(20,50),border_width=2,border_color=COLORS['entryFieldColor'],fg_color='#fff')
        
        #prixVente
        self.prixVenteL = Text(self.frame,text="Prix de Vente",col=1,span=1,row=3,size=15,weight='normal',sticky='ws',color='text',padx=20)
        self.prixVenteE=EntryField(self.frame,placeholder_text="Inserez le prix de vente'" ,height=50,size=13,width=150,col=1,row=4,sticky="new",padx=20,border_width=2,border_color=COLORS['entryFieldColor'],fg_color='#fff')
        
        
        #Quantité
        self.creditClient = ctk.StringVar(value="0")
        self.nomclientLabel = Text(self.frame,text="Quantité",col=1,span=1,row=5,size=15,weight='normal',sticky='ws',color='text',padx=20)
        self.nomclientEntry=EntryField(self.frame,placeholder_text="Inserez la quantité de stock" ,height=50,size=13,width=150,col=1,row=6,sticky="new",padx=20,border_width=2,border_color=COLORS['entryFieldColor'],fg_color='#fff',state=ctk.NORMAL,textvariable=self.creditClient)
        
        #en gros ici si le entryfield state est egale a disabled -> changer le style du box 
        
        
        #stock minimal
        self.creditClient = ctk.StringVar(value="0")
        self.nomclientLabel = Text(self.frame,text="Stock Minimal",col=2,span=1,row=1,size=15,weight='normal',sticky='ws',color='text',padx=20)
        self.nomclientEntry=EntryField(self.frame,placeholder_text="Inserez la quantité de stock minimale" ,height=50,size=13,width=150,col=2,row=2,sticky="new",padx=20,border_width=2,border_color=COLORS['entryFieldColor'],fg_color='#fff',state=ctk.NORMAL,textvariable=self.creditClient)
        

    
        #age du client
        self.nomclientLabel = Text(self.frame,text="Age du client",col=2,span=1,row=3,size=15,weight='normal',sticky='ws',color='text',padx=20)
         
        self.value=ctk.StringVar(value="adulte")
        self.rAdulte = RadioButton(parent=self.frame,func=lambda:print(self.value.get()),value="adulte",text="Adulte",col=2,row=4,variable=self.value,sticky="w",padx=(10,0))
        self.rAge = RadioButton(parent=self.frame,func=lambda:print(self.value.get()),value="age",text="Agé",col=2,row=4,variable=self.value,sticky="e",padx=(10,0))
     
     
        #type de client
        self.nomclientLabel = Text(self.frame,text="Type de client",col=2,span=1,row=5,size=15,weight='normal',sticky='ws',color='text',padx=20)
         
        self.value=ctk.StringVar(value="male")
        
        self.rAdulte = RadioButton(parent=self.frame,func=lambda:print(self.value.get()),value="fidel",text="Standard",col=2,row=6,variable=self.value,sticky="w",padx=(10,0))
        self.rAge = RadioButton(parent=self.frame,func=lambda:print(self.value.get()),value="fidele",text="Fidele",col=2,row=6,variable=self.value,sticky="e",padx=(10,0))
        
        
        self.ajouterButton = Button(self.frame ,func=lambda:print("button clicked"),col=3,row=8,sticky="wn",padx=(0,0),text="Ajouter")
        
        self.annulerButton = Button(self.frame ,func=lambda:print("button clicked"),col=3,row=8,sticky="en",padx=(0,20),text="Annuler",color='gray')
        
        


























































# from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame, CTkScrollbar, CTkTextbox

# from ..controllers.product_controller import ProductController
# class ProductView(CTk):
#     def __init__(self):
#         super().__init__(title="Product Management")

#         self.product_list_frame = CTkFrame(self, borderwidth=1, relief="solid")
#         self.product_list_frame.pack(side="left", fill="both", expand=True)

#         self.product_list_label = CTkLabel(self.product_list_frame, text="Product List")
#         self.product_list_label.pack(pady=10)

#         self.product_listbox = CTkTextbox(self.product_list_frame, selectmode="single", height=10)
#         self.product_listbox.pack(side="left", fill="both", expand=True)

#         self.product_scrollbar = CTkScrollbar(self.product_list_frame, command=self.product_listbox.yview)
#         self.product_scrollbar.pack(side="right", fill="y")

#         self.product_listbox.config(yscrollcommand=self.product_scrollbar.set)

#         self.load_products()

#         self.product_details_frame = CTkFrame(self, borderwidth=1, relief="solid")
#         self.product_details_frame.pack(side="right", fill="both", expand=True, padx=10)

#         self.product_details_label = CTkLabel(self.product_details_frame, text="Product Details")
#         self.product_details_label.pack(pady=10)

#         self.name_label = CTkLabel(self.product_details_frame, text="Name:")
#         self.name_label.pack()

#         self.name_entry = CTkEntry(self.product_details_frame)
#         self.name_entry.pack()

#         self.dosage_label = CTkLabel(self.product_details_frame, text="Dosage:")
#         self.dosage_label.pack()

#         self.dosage_entry = CTkEntry(self.product_details_frame)
#         self.dosage_entry.pack()

#         self.manufacturer_label = CTkLabel(self.product_details_frame, text="Manufacturer:")
#         self.manufacturer_label.pack()

#         self.manufacturer_entry = CTkEntry(self.product_details_frame)
#         self.manufacturer_entry.pack()

#         self.expiration_label = CTkLabel(self.product_details_frame, text="Expiration Date (YYYY-MM-DD):")
#         self.expiration_label.pack()

#         self.expiration_entry = CTkEntry(self.product_details_frame)
#         self.expiration_entry.pack()

#         self.quantity_label = CTkLabel(self.product_details_frame, text="Quantity in Stock:")
#         self.quantity_label.pack()

#         self.quantity_entry = CTkEntry(self.product_details_frame)
#         self.quantity_entry.pack()

#         self.price_label = CTkLabel(self.product_details_frame, text="Price:")
#         self.price_label.pack()

#         self.price_entry = CTkEntry(self.product_details_frame)
#         self.price_entry.pack()

#         self.add_button = CTkButton(self.product_details_frame, text="Add Product", command=self.add_product)
#         self.add_button.pack(pady=10)

#         self.update_button = CTkButton(self.product_details_frame, text="Update Product", command=self.update_product)
#         self.update_button.pack()

#         self.product_listbox.bind("<ButtonRelease-1>", self.load_selected_product)

#     def load_products(self):
#         result = ProductController.get_all_products()
#         if result["success"]:
#             products = result["products"]
#             for product in products:
#                 self.product_listbox.insert("end", f"{product['name']} ({product['manufacturer']})")

#     def load_selected_product(self, event):
#         selected_index = self.product_listbox.curselection()
#         if selected_index:
#             selected_product = self.product_listbox.get(selected_index)
#             product_name, _ = selected_product.split(" (")
#             result = ProductController.get_product_by_id(product_name)
#             if result["success"]:
#                 product = result["product"]
#                 self.name_entry.delete(0, "end")
#                 self.name_entry.insert(0, product["name"])

#                 self.dosage_entry.delete(0, "end")
#                 self.dosage_entry.insert(0, product["dosage"])

#                 self.manufacturer_entry.delete(0, "end")
#                 self.manufacturer_entry.insert(0, product["manufacturer"])

#                 self.expiration_entry.delete(0, "end")
#                 self.expiration_entry.insert(0, product["expiration_date"])

#                 self.quantity_entry.delete(0, "end")
#                 self.quantity_entry.insert(0, str(product["quantity_in_stock"]))

#                 self.price_entry.delete(0, "end")
#                 self.price_entry.insert(0, str(product["price"]))

#     def add_product(self):
#         name = self.name_entry.get()
#         dosage = self.dosage_entry.get()
#         manufacturer = self.manufacturer_entry.get()
#         expiration_date = self.expiration_entry.get()
#         quantity_in_stock = self.quantity_entry.get()
#         price = self.price_entry.get()

#         result = ProductController.add_product(name, dosage, manufacturer, expiration_date, quantity_in_stock, price)
#         if result["success"]:
#             self.product_listbox.insert("end", f"{name} ({manufacturer})")
#             self.clear_product_details()
#         else:
#             print(f"Error: {result['message']}")

#     def update_product(self):
#         selected_index = self.product_listbox.curselection()
#         if not selected_index:
#             print("Error: Please select a product to update.")
#             return

#         selected_product = self.product_listbox.get(selected_index)
#         product_name, _ = selected_product.split(" (")
#         product_id = product_name  # For simplicity, assuming product name is unique

#         name = self.name_entry.get()
#         dosage = self.dosage_entry.get()
#         manufacturer = self.manufacturer_entry.get()
#         expiration_date = self.expiration_entry.get()
#         quantity_in_stock = self.quantity_entry.get()
#         price = self.price_entry.get()

#         result = ProductController.update_product(product_id, name, dosage, manufacturer, expiration_date, quantity_in_stock, price)
#         if result["success"]:
#             self.clear_product_details()
#             self.product_listbox.delete(selected_index)
#             self.product_listbox.insert(selected_index, f"{name} ({manufacturer})")
#         else:
#             print(f"Error: {result['message']}")

#     def clear_product_details(self):
#         self.name_entry.delete(0, "end")
#         self.dosage_entry.delete(0, "end")
#         self.manufacturer_entry.delete(0, "end")
#         self.expiration_entry.delete(0, "end")
#         self.quantity_entry.delete(0, "end")
#         self.price_entry.delete(0, "end")

# if __name__ == "__main__":
#     ProductView().mainloop()









