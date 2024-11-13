import main as main
import inventory_manager as inventory_manager
#Product class is used to define products with detailed description.
class Product:
    def __init__(self, product_id, name, category, price, stock_qty):  # Constructor to initialize attributes
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_qty = stock_qty
        
    def __repr__(self): #This function is used to display products in an efficient way.
        return f"Product ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock_qty}"