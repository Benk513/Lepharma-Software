# app/models/product_model.py

from datetime import datetime, timedelta

class ProductModel:
    def __init__(self, name, dosage, manufacturer, expiration_date, quantity_in_stock, price):
        self.name = name
        self.dosage = dosage
        self.manufacturer = manufacturer
        self.expiration_date = expiration_date
        self.quantity_in_stock = quantity_in_stock
        self.price = price

    @staticmethod
    def validate_date(date_str):
        try:
            # Attempt to parse the date string
            date_object = datetime.strptime(date_str, '%Y-%m-%d')
            # Check if the expiration date is not in the past
            if date_object < datetime.now():
                raise ValueError("Expiration date must be in the future.")
            return date_object
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")

    @staticmethod
    def validate_quantity(quantity):
        try:
            # Check if the quantity is a positive integer
            quantity = int(quantity)
            if quantity < 0:
                raise ValueError("Quantity must be a non-negative integer.")
            return quantity
        except ValueError as e:
            raise ValueError(f"Invalid quantity: {e}")

    @staticmethod
    def validate_price(price):
        try:
            # Check if the price is a positive float
            price = float(price)
            if price < 0:
                raise ValueError("Price must be a non-negative float.")
            return price
        except ValueError as e:
            raise ValueError(f"Invalid price: {e}")

    @classmethod
    def add_product(cls, name, dosage, manufacturer, expiration_date, quantity_in_stock, price):
        expiration_date = cls.validate_date(expiration_date)
        quantity_in_stock = cls.validate_quantity(quantity_in_stock)
        price = cls.validate_price(price)

        product = cls(
            name=name,
            dosage=dosage,
            manufacturer=manufacturer,
            expiration_date=expiration_date,
            quantity_in_stock=quantity_in_stock,
            price=price
        )

        inventory.append(product)
        return product

    @classmethod
    def update_product(cls, product_id, name, dosage, manufacturer, expiration_date, quantity_in_stock, price):
        if not (0 <= product_id < len(inventory)):
            raise ValueError("Invalid product ID.")

        expiration_date = cls.validate_date(expiration_date)
        quantity_in_stock = cls.validate_quantity(quantity_in_stock)
        price = cls.validate_price(price)

        product = cls(
            name=name,
            dosage=dosage,
            manufacturer=manufacturer,
            expiration_date=expiration_date,
            quantity_in_stock=quantity_in_stock,
            price=price
        )

        inventory[product_id] = product
        return product

    @classmethod
    def get_all_products(cls):
        return inventory

    @classmethod
    def get_product_by_id(cls, product_id):
        if not (0 <= product_id < len(inventory)):
            raise ValueError("Invalid product ID.")
        return inventory[product_id]

    @classmethod
    def delete_product(cls, product_id):
        if not (0 <= product_id < len(inventory)):
            raise ValueError("Invalid product ID.")
        deleted_product = inventory.pop(product_id)
        return deleted_product

# Example in-memory storage (replace with database interaction in a real application)
inventory = []
