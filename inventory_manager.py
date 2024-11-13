import products as products
#This inventory class willmanage entire inventory managment tasks such as addition, updation, deletion etc.
class Inventory:
    def __init__(self):
        self.products = {}

    #Function for Addition of Products
    def add_product (self, product):
        self.products[product.product_id] = product
        print(f"\nProduct '{product.name}' added successfully")
    
    #Funciton to Edit Product
    def edit_product(self, product_id, **kwargs):
        product = self.products.get(product_id)
        if product: 
            for key, value in kwargs.items():
                #setattr dynamically sets the attribute key of the product object to the value passed in kwargs.
                setattr( product, key, value) 
            print(f"\nProduct {product_id} updated sucessfully")
        else:
            print(f"\nProduct wih ID {product_id} not found")

    #Funciton to delete Products   
    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"\nProduct with ID {product_id} has been deleted")
        else:
            print(f"\nProduct wih ID {product_id} not found")
    
    #Funtion to view all products
    def view_all_products(self):
        if not self.products:
            print("\nNo products in inventory.")
        else:
            for product in self.products.values():
                print(product)
    
    #Function to search product by name
    def search_by_name (self, name):
        results = [product for product in self.values()]
        if results:
            for product in results:
                print(product)
        else:
            print(f"\nNo products found with name '{name}'.")
    #Function to find products with low stock
    def filter_by_stock(self, threshold):
        low_stock = [product for product in self.products.values() if product.stock_qty <= threshold]
        if low_stock:
            for product in low_stock:
                print(product)
        else:
            print("\nNo products are below the stock threshold.")
    #Function for re-stocking if a product is low_stock
    def restock_product(self, product_id, quantity):
        product = self.products.get(product_id)
        if product:
            product.stock_qty += quantity
            print(f"\nProduct {product_id} restocked by {quantity}. New Stock: {product.stock_qty}")
        else:
            print(f"\nProduct with ID {product_id} not found.")


    