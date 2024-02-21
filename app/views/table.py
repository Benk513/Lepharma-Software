import customtkinter
from CTkTable import *

def hover(event):
    selected_row = event['row']

    # Deselect the previous selected row
    table.deselect_row(selected_row - 1)
   

    # Toggle selection for the current row
    table.select_row(selected_row)
    table.deselect_row(selected_row +1)
    print(table.get_row(selected_row))    
        
root = customtkinter.CTk()

value = [
    ["Nom","Age","Engagé","Credit","Adresse"],
    ["ben kuyu",22,"Oui",441,"n°5, av niangi 16eme rue"],
]       
    
table = CTkTable(
    master=root,
    row=5,
    column=5,
    values=value,
    header_color='#aaa',
    colors=["yellow", "green"],corner_radius=0,
    hover=True,command=hover)

table.add_column([12])


table.pack(expand=True, fill="x", padx=20, pady=20)





root.mainloop()





# Example usage with CTkTable
# from CTkTable import CTkTable  # Adjust the import based on the actual structure

# # Create an instance of CTkTable
# table = CTkTable()

# Bind the hover function to the cell click event
 # Adjust the event binding based on the actual event in CTkTable

# You may need to update the method names based on the actual implementation of CTkTable
# For example, replace `get_selected_row` with the appropriate method provided by CTkTable



# {
#  'row': 2,
#  'column': 4,
#  'value': ' ', 
#  'args': {'text_color': ['gray10', '#DCE4EE'], 'height': 28, 'width': 140, 'fg_color': 'yellow', 'anc{'row': 1, 'column': 4, 'value': 'n°5, av niangi 16eme rue', 'args': 
# _color': 'green', 'anchor': 'c', 'hover_color': ['#36719F', '#144870'], 'hover': True}}