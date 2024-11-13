import inventory_manager as inventory_manager
import products as products
import users as users

#This is the main function where Inventory Management system runs.
def main():

    print("\nWelcome to the Console Based Inventory Management System\n")   

    inventory = inventory_manager.Inventory() # Creates an inventory object
    # Adding 2 Sample product for testing 
    print("\nAdding Two Products for Stock View\n")
    inventory.add_product(products.Product(1, "Shirt", "Clothing", 250.00, 80))
    inventory.add_product(products.Product(2, "Samsung", "Mobiles", 27000.00, 75))


        # User login
    username = input("Enter username (Hint= admin/user):  ")
    password = input("Enter password (admin123/user123): ")
    try:
        role = users.login(username, password)
        print(f"\nLogin successful! You are logged in as: {role}")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Admin Menu
    if role == 'Admin':
        while True:
            print("\nAdmin Menu:")
            print("1. View All Products")
            print("2. Add Product")
            print("3. Edit Product")
            print("4. Delete Product")
            print("5. Restock Product")
            print("6. Search Products by Name")
            print("7. Filter Products by Low Stock")
            print("8. Logout")

            choice = input("Choose an action (1-8): ")

            if choice == '1':
                inventory.view_all_products()
            elif choice == '2':
                product_id = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                category = input("Enter category: ")
                price = float(input("Enter price: "))
                stock_quantity = int(input("Enter stock quantity: "))
                product = products.Product(product_id, name, category, price, stock_quantity)
                inventory.add_product(product)
            elif choice == '3':
                product_id = int(input("Enter product ID to edit: "))
                name = input("Enter new name (leave blank to skip): ")
                category = input("Enter new category (leave blank to skip): ")
                price = input("Enter new price (leave blank to skip): ")
                stock_quantity = input("Enter new stock quantity (leave blank to skip): ")

                updates = {}
                if name: updates['name'] = name
                if category: updates['category'] = category
                if price: updates['price'] = float(price)
                if stock_quantity: updates['stock_quantity'] = int(stock_quantity)

                inventory.edit_product(product_id, **updates)
            elif choice == '4':
                product_id = int(input("Enter product ID to delete: "))
                inventory.delete_product(product_id)
            elif choice == '5':
                product_id = int(input("Enter product ID to restock: "))
                quantity = int(input("Enter quantity to restock: "))
                inventory.restock_product(product_id, quantity)
            elif choice == '6':
                name = input("Enter product name to search: ")
                inventory.search_by_name(name)
            elif choice == '7':
                threshold = int(input("Enter stock threshold: "))
                inventory.filter_by_stock(threshold)
            elif choice == '8':
                print("Logging out...")
                break

    # User Menu (User can only view products)
    elif role == 'User':
        while True:
            print("\nUser Menu:")
            print("1. View All Products")
            print("2. Search Products by Name")
            print("3. Logout")

            choice = input("Choose an action (1-3): ")

            if choice == '1':
                inventory.view_all_products()
            elif choice == '2':
                name = input("Enter product name to search: ")
                inventory.search_by_name(name)
            elif choice == '3':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
