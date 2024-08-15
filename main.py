from data import data

title = """
$$$$$$$$\                                                                   $$$$$$$$\                           $$\                           
$$  _____|                                                                  \__$$  __|                          $$ |                          
$$ |      $$\   $$\  $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$$\  $$$$$$\           $$ | $$$$$$\  $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$$$$\    \$$\ $$  |$$  __$$\ $$  __$$\ $$  __$$\ $$  _____|$$  __$$\          $$ |$$  __$$\ \____$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
$$  __|    \$$$$  / $$ /  $$ |$$$$$$$$ |$$ |  $$ |\$$$$$$\  $$$$$$$$ |         $$ |$$ |  \__|$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
$$ |       $$  $$<  $$ |  $$ |$$   ____|$$ |  $$ | \____$$\ $$   ____|         $$ |$$ |     $$  __$$ |$$ |      $$  _$$<  $$   ____|$$ |      
$$$$$$$$\ $$  /\$$\ $$$$$$$  |\$$$$$$$\ $$ |  $$ |$$$$$$$  |\$$$$$$$\          $$ |$$ |     \$$$$$$$ |\$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
\________|\__/  \__|$$  ____/  \_______|\__|  \__|\_______/  \_______|         \__|\__|      \_______| \_______|\__|  \__| \_______|\__|      
                    $$ |                                                                                                                      
                    $$ |                                                                                                                      
                    \__|                                                                                                                      
"""

# This expense tracker has 4 functions; get data, save data, read data and calculate spendings
# Any logged expenses is added to the data dictionary
# The data can be accessed in a user-friendly, readable format using the read data function
# you can also choose between reading all the data or just for a specific month
# the inputs are formatted and there is exception handling to minimise any errors

print(title)

def get_data():

    initiate= input("Would you like to log any spending?: ").lower()

    if initiate in ["yes", "y", "ok"]:
        
        while True: # loops over until input is correct format
            month = input("Please enter month: ").lower()
            if month in data:
                break
            else:
                print("Invalid month")
        
        while True: # loops over until input is correct format
            try:
                expense = input("Enter amount spent: ").lower()
                expense = expense.replace('£', '').replace(' ', '') # removes any £ sign and spaces
                expense = f"£{float(expense):.2f}" # always to 2 decimal places
                break
            except ValueError:
                print("Please use only \"£\" symbol or no symbol at all eg. \"3.33\"")
        
        while True: # loops over until input is correct format
            category = input("Enter category (bills, petrol, groceries, presents or extra): ").lower()

            if category in ["bills", "petrol", "groceries", "presents", "extra"]:
                break
            else:
                print(f"'{category}' is not a valid category. Please try again.")

        description = input("Enter description (optional): ").lower()

        save_data(month, expense, category, description) # calls save data function

    else:
        return

def save_data(month, expense, category, description):
    try:
        number = max(data[month].keys(), default=0) + 1 # creates a new entry for the month with the keys being saved as "1", "2", "3" etc.
        data[month][number] = {"expense": expense, "category": category, "description": description} # adds all the values
        
        with open('data.py', 'w') as f:
            f.write(f"data = {repr(data)}\n") # writes the data to data.py
    
    except Exception as e:
        print(f"An error occurred while saving data: {e}") # allows for any error that may occur
        
def read_data():

    initiate = input("Would you like to read any data?: ").lower()

    if initiate in ["yes", "y", "ok"]:
        while True: # loops over until input is correct format
            request = input("Enter month you would like the data from, or type \"all\" to see all data: ").lower()
            if request == "all":
                total_cost = calculate_spendings(request) # calls calculate spendings function
                print() # spacing for readability
                print(f"TOTAL SPENDING ACROSS ALL MONTHS: £{total_cost:.2f}")
                print()

                for month, expenses in data.items(): # for every month in data...
                    print(f"Month: {month.capitalize()}") # print the month...
                    for number, details in expenses.items(): # then print the details of every number entry in that month
                        print(f"  Entry {number}:")
                        print(f"    Expense: {details['expense']}")
                        print(f"    Category: {details['category']}")
                        print(f"    Description: {details['description']}")
                    print()

                return

            elif request in data:
                total_cost = calculate_spendings(request) # calls calculate spendings function
                print() # spacing for readability
                print(f"TOTAL SPENDING IN {request.upper()}: £{total_cost:.2f}")
                print()

                print(f"Month: {request.capitalize()}")
                for number, details in data[request].items(): # print the details of every number entry in that month
                    print(f"  Entry {number}:")
                    print(f"    Expense: {details['expense']}")
                    print(f"    Category: {details['category']}")
                    print(f"    Description: {details['description']}")
                    print()

                return

            else:
                print("Invalid month entry")
        
def calculate_spendings(request):

    total_cost = 0.0

    try:
        if request == "all":
            for month, expenses in data.items(): # for every month in data...
                for details in expenses.values(): # for every number entry...
                    cost = (details['expense']) # access the expense
                    cost_float = float(cost.replace('£', '').replace(' ', '')) # convert to float removing £ sign and spaces
                    total_cost += cost_float # add it to total cost
            return total_cost
            
        
        elif request in data:
            for details in data[request].values(): # for ever number entry of specified month
                cost = details['expense'] # access the expense
                cost_float = float(cost.replace('£', '').replace(' ', '')) # convert to float removing £ sign and spaces
                total_cost += cost_float # add it to total cost
            return total_cost
    
    except Exception as e: # allows for any error that may occur
        print(f"An error occurred while calculating spendings: {e}")
        return 0.0

get_data() # calls get data function

read_data() # calls read data function

print("Thank you for using expense tracker")















