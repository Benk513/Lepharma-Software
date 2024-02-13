# app/controllers/product_controller.py

from app.models.product_model import ProductModel

class ProductController:
    @staticmethod
    def add_product(name, dosage, manufacturer, expiration_date, quantity_in_stock, price):
        try:
            product = ProductModel.add_product(
                name=name,
                dosage=dosage,
                manufacturer=manufacturer,
                expiration_date=expiration_date,
                quantity_in_stock=quantity_in_stock,
                price=price
            )
            return {"success": True, "message": "Product added successfully", "product": product.__dict__}
        except ValueError as e:
            return {"success": False, "message": str(e)}

    @staticmethod
    def update_product(product_id, name, dosage, manufacturer, expiration_date, quantity_in_stock, price):
        try:
            product = ProductModel.update_product(
                product_id=product_id,
                name=name,
                dosage=dosage,
                manufacturer=manufacturer,
                expiration_date=expiration_date,
                quantity_in_stock=quantity_in_stock,
                price=price
            )
            return {"success": True, "message": "Product updated successfully", "product": product.__dict__}
        except ValueError as e:
            return {"success": False, "message": str(e)}

    @staticmethod
    def get_all_products():
        products = ProductModel.get_all_products()
        return {"success": True, "products": [product.__dict__ for product in products]}

    @staticmethod
    def get_product_by_id(product_id):
        try:
            product = ProductModel.get_product_by_id(product_id)
            return {"success": True, "product": product.__dict__}
        except ValueError as e:
            return {"success": False, "message": str(e)}

    @staticmethod
    def delete_product(product_id):
        try:
            deleted_product = ProductModel.delete_product(product_id)
            return {"success": True, "message": "Product deleted successfully", "deleted_product": deleted_product.__dict__}
        except ValueError as e:
            return {"success": False, "message": str(e)}
