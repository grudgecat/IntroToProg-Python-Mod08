# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Sheri Elgin, Dec 6, 2021, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Sheri Elgin, Dec 6, 2021, Modified code to complete assignment 8
    """

    # --Fields--
    # strFirstName = ""

    # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties --
    # NAME
    @property #GETTER
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter #SETTER
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers")

    # PRICE
    @property #GETTER
    def product_price(self):
        return str(self.__product_price)

    @product_price.setter #SETTER
    def product_price(self, value):
        self.__product_price = value
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Sheri Elgin, Dec 6, 2021, Modified code to complete assignment 8
    """
   
    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        """ Reads data from a file into a list of product objects

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) you want filled with file data:
        :return: (list) of products:
        """
        list_of_product_objects.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            product, price = line.split(",")
            product.strip()
            price.strip()
            objProduct = Product(product, price)
            # print(type(objProduct))
            list_of_product_objects.append(objProduct)
        file.close()
        return list_of_product_objects

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Save list_of_product_objects data to file

               :param file_name: (string) file to write to:
               :param list_of_product_objects: (list) list of product objects:
               :return: (list) of product objects
               """
        try:
            f = open(file_name, "w")
            for item in list_of_product_objects:
                f.write(item.product_name + "," + item.product_price + '\n')
            f.close()
        except:
            print('Unable to open/write to source file')
        return list_of_product_objects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks

    methods:
        print_menu_options()
        input_menu_choice() -> (str: menu choice)
        print_current_products_in_list(list_of_product_objects)
        input_yes_no_choice(message) -> (str:reply from user)
        input_press_to_continue(optional_message='')
        input_new_product_and_price() -> (obj: new product object)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Sheri Elgin, Dec 6, 2021, Modified code to complete assignment 8
    """
    @staticmethod
    def print_menu_options():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current list of products
        2) Add product to list
        3) Save data to file  
        4) Exit program without save    
        ''')
        print()  # Add an extra line

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line
        return choice

    @staticmethod
    def print_current_products_in_list(list_of_product_objects):
        """ Shows the current Products in the list

        :param list_of_product_objects: (list) of rows you want to display
        :return: nothing
        """
        print("******* Current Products: *******")
        for item in list_of_product_objects:
            print(item.product_name + ", " + item.product_price)
        print("*******************************************")
        # print()  # Add an extra line

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message + '\n')
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product_and_price():
        """ Get product and price from user

        :return: Product object
        """
        product = input("Please enter product name: ").upper()
        price = input("Product price: ")
        if price == '':
            price = 0
        # elif price is not float:
        #     price = 0
        else:
            price = format(float(price), '.2f')
        objProduct = Product(product, price)

        return objProduct

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #


# Step 1 - When the program starts, Load data from ToDoFile.txt.
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_products_in_list(lstOfProductObjects)  # Show current data from file
    IO.print_menu_options()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Show current list
        IO.print_current_products_in_list(lstOfProductObjects)
        IO.input_press_to_continue()
        continue  # to show the menu

    elif strChoice == '2':  # Add a product and price to list
        objProd = IO.input_new_product_and_price()
        lstOfProductObjects.append(objProd)
        IO.input_press_to_continue()
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save all product data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue()
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice != '4':  # Invalid menu option
        print("Warning: Invalid menu option selected, please only enter 1, 2, 3 or 4.")
        continue  # to show the menu

    else:  #  Exit Program
        print("Goodbye!")
        break   # and Exit
