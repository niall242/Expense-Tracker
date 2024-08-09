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
print(title)

def get_data():

    initiate= input("Would you like to log any spending?: ").lower()

    if initiate in ["yes", "y", "ok"]:

        month = input("Please enter month: ").lower()
        
        while True:
            try:
                expense = input("Enter amount spent: ").lower()
                expense = expense.replace('£', '').replace(' ', '')
                expense = f"£{float(expense):.2f}"
                break
            except ValueError:
                print("Please use only \"£\" symbol or no symbol at all eg. \"3.33\"")
        
        while True:
            category = input("Enter category (bills, petrol, groceries, presents or extra): ").lower()

            if category in ["bills", "petrol", "groceries", "presents", "extra"]:
                break
            else:
                print(f"'{category}' is not a valid category. Please try again.")


        
        description = input("Enter description (optional): ").lower()

        save_data(month, expense, category, description)

    else:
        return

def save_data(month, expense, category, description):
    try:
        if month in data:
            number = max(data[month].keys(), default=0) + 1
            data[month][number] = {"expense": expense, "category": category, "description": description}
            
            with open('data.py', 'w') as f:
                f.write(f"data = {repr(data)}\n")
        
        else:
            print("Invalid month")
    
    except Exception as e:
        print(f"An error occurred while saving data: {e}")
        
def read_data():

    initiate = input("Would you like to read any data?: ").lower()

    if initiate in ["yes", "y", "ok"]:
        request = input("Enter month you would like the data from, or type \"all\" to see all data: ").lower()
        if request == "all":
            total_cost = calculate_spendings(request)
            print()
            print(f"TOTAL SPENDING ACROSS ALL MONTHS: £{total_cost:.2f}")
            print()

            for month, expenses in data.items():
                print(f"Month: {month.capitalize()}")
                for number, details in expenses.items():
                    print(f"  Entry {number}:")
                    print(f"    Expense: {details['expense']}")
                    print(f"    Category: {details['category']}")
                    print(f"    Description: {details['description']}")
                print()

        elif request in data:
            total_cost = calculate_spendings(request)
            print()
            print(f"TOTAL SPENDING IN {request.upper()}: £{total_cost:.2f}")
            print()

            print(f"Month: {request.capitalize()}")
            for number, details in data[request].items():
                print(f"  Entry {number}:")
                print(f"    Expense: {details['expense']}")
                print(f"    Category: {details['category']}")
                print(f"    Description: {details['description']}")
                print()

        else:
            print("Invalid month entry")

        return
    
def calculate_spendings(request):

    total_cost = 0.0

    try:
        if request == "all":
            for month, expenses in data.items():
                for details in expenses.values():
                    cost = (details['expense'])
                    cost_float = float(cost.replace('£', '').replace(' ', ''))
                    total_cost += cost_float
            return total_cost
            
        
        elif request in data:
            for details in data[request].values():
                cost = details['expense']
                cost_float = float(cost.replace('£', '').replace(' ', ''))
                total_cost += cost_float
            return total_cost
    
    except Exception as e:
        print(f"An error occurred while calculating spendings: {e}")
        return 0.0

get_data()

read_data()

print("Thank you for using expense tracker")















