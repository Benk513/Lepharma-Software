# app/views/product_view.py

from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame, CTkScrollbar, CTkTextbox

from ..controllers.product_controller import ProductController
class ProductView(CTk):
    def __init__(self):
        super().__init__(title="Product Management")

        self.product_list_frame = CTkFrame(self, borderwidth=1, relief="solid")
        self.product_list_frame.pack(side="left", fill="both", expand=True)

        self.product_list_label = CTkLabel(self.product_list_frame, text="Product List")
        self.product_list_label.pack(pady=10)

        self.product_listbox = CTkTextbox(self.product_list_frame, selectmode="single", height=10)
        self.product_listbox.pack(side="left", fill="both", expand=True)

        self.product_scrollbar = CTkScrollbar(self.product_list_frame, command=self.product_listbox.yview)
        self.product_scrollbar.pack(side="right", fill="y")

        self.product_listbox.config(yscrollcommand=self.product_scrollbar.set)

        self.load_products()

        self.product_details_frame = CTkFrame(self, borderwidth=1, relief="solid")
        self.product_details_frame.pack(side="right", fill="both", expand=True, padx=10)

        self.product_details_label = CTkLabel(self.product_details_frame, text="Product Details")
        self.product_details_label.pack(pady=10)

        self.name_label = CTkLabel(self.product_details_frame, text="Name:")
        self.name_label.pack()

        self.name_entry = CTkEntry(self.product_details_frame)
        self.name_entry.pack()

        self.dosage_label = CTkLabel(self.product_details_frame, text="Dosage:")
        self.dosage_label.pack()

        self.dosage_entry = CTkEntry(self.product_details_frame)
        self.dosage_entry.pack()

        self.manufacturer_label = CTkLabel(self.product_details_frame, text="Manufacturer:")
        self.manufacturer_label.pack()

        self.manufacturer_entry = CTkEntry(self.product_details_frame)
        self.manufacturer_entry.pack()

        self.expiration_label = CTkLabel(self.product_details_frame, text="Expiration Date (YYYY-MM-DD):")
        self.expiration_label.pack()

        self.expiration_entry = CTkEntry(self.product_details_frame)
        self.expiration_entry.pack()

        self.quantity_label = CTkLabel(self.product_details_frame, text="Quantity in Stock:")
        self.quantity_label.pack()

        self.quantity_entry = CTkEntry(self.product_details_frame)
        self.quantity_entry.pack()

        self.price_label = CTkLabel(self.product_details_frame, text="Price:")
        self.price_label.pack()

        self.price_entry = CTkEntry(self.product_details_frame)
        self.price_entry.pack()

        self.add_button = CTkButton(self.product_details_frame, text="Add Product", command=self.add_product)
        self.add_button.pack(pady=10)

        self.update_button = CTkButton(self.product_details_frame, text="Update Product", command=self.update_product)
        self.update_button.pack()

        self.product_listbox.bind("<ButtonRelease-1>", self.load_selected_product)

    def load_products(self):
        result = ProductController.get_all_products()
        if result["success"]:
            products = result["products"]
            for product in products:
                self.product_listbox.insert("end", f"{product['name']} ({product['manufacturer']})")

    def load_selected_product(self, event):
        selected_index = self.product_listbox.curselection()
        if selected_index:
            selected_product = self.product_listbox.get(selected_index)
            product_name, _ = selected_product.split(" (")
            result = ProductController.get_product_by_id(product_name)
            if result["success"]:
                product = result["product"]
                self.name_entry.delete(0, "end")
                self.name_entry.insert(0, product["name"])

                self.dosage_entry.delete(0, "end")
                self.dosage_entry.insert(0, product["dosage"])

                self.manufacturer_entry.delete(0, "end")
                self.manufacturer_entry.insert(0, product["manufacturer"])

                self.expiration_entry.delete(0, "end")
                self.expiration_entry.insert(0, product["expiration_date"])

                self.quantity_entry.delete(0, "end")
                self.quantity_entry.insert(0, str(product["quantity_in_stock"]))

                self.price_entry.delete(0, "end")
                self.price_entry.insert(0, str(product["price"]))

    def add_product(self):
        name = self.name_entry.get()
        dosage = self.dosage_entry.get()
        manufacturer = self.manufacturer_entry.get()
        expiration_date = self.expiration_entry.get()
        quantity_in_stock = self.quantity_entry.get()
        price = self.price_entry.get()

        result = ProductController.add_product(name, dosage, manufacturer, expiration_date, quantity_in_stock, price)
        if result["success"]:
            self.product_listbox.insert("end", f"{name} ({manufacturer})")
            self.clear_product_details()
        else:
            print(f"Error: {result['message']}")

    def update_product(self):
        selected_index = self.product_listbox.curselection()
        if not selected_index:
            print("Error: Please select a product to update.")
            return

        selected_product = self.product_listbox.get(selected_index)
        product_name, _ = selected_product.split(" (")
        product_id = product_name  # For simplicity, assuming product name is unique

        name = self.name_entry.get()
        dosage = self.dosage_entry.get()
        manufacturer = self.manufacturer_entry.get()
        expiration_date = self.expiration_entry.get()
        quantity_in_stock = self.quantity_entry.get()
        price = self.price_entry.get()

        result = ProductController.update_product(product_id, name, dosage, manufacturer, expiration_date, quantity_in_stock, price)
        if result["success"]:
            self.clear_product_details()
            self.product_listbox.delete(selected_index)
            self.product_listbox.insert(selected_index, f"{name} ({manufacturer})")
        else:
            print(f"Error: {result['message']}")

    def clear_product_details(self):
        self.name_entry.delete(0, "end")
        self.dosage_entry.delete(0, "end")
        self.manufacturer_entry.delete(0, "end")
        self.expiration_entry.delete(0, "end")
        self.quantity_entry.delete(0, "end")
        self.price_entry.delete(0, "end")

if __name__ == "__main__":
    ProductView().mainloop()
