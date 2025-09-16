import random

class DayConditions:
    """
    This DayConditions class is to be used at the beginning of each day.
    Its purpose is to define the conditions for the day - temperature, climate, and potential customers.
    """
    def __init__(self):
        self.temp = random.randint(55, 92)  #get random temperature between 55-92 degrees
        self.climate = random.choice(["Sunny", "Sunny and Dry", "Cloudy", "Rainy"])  #get random climate
        self.potential_customers = 0  #initializes potential customers of the day to 0

    def __str__(self):
        return f'{self.temp} degrees and {self.climate} \n{self.potential_customers} potential customers'

    def customers_from_temp(self):  #calculates amount of potential customers based on temperature (before climate)
        if 55 <= self.temp <= 64:
            cust_from_temp = 50
            return cust_from_temp
        elif 65 <= self.temp <= 74:
            cust_from_temp = 65
            return cust_from_temp
        elif 75 <= self.temp <= 84:
            cust_from_temp = 80
            return cust_from_temp
        elif 85 <= self.temp <= 92:
            cust_from_temp = 100
            return cust_from_temp

    def total_pot_customers(self):  #calculates total amount of potential customers
        cust_from_temp = self.customers_from_temp()
        if self.climate == "Sunny":
            # takes customers calculated from temperature and adds/subtracts based on the climate condition
            tot_pot_customers = cust_from_temp + (cust_from_temp * 0.6)
            self.potential_customers = round(tot_pot_customers)
        elif self.climate == "Sunny and Dry":
            tot_pot_customers = cust_from_temp + (cust_from_temp * 0.75)
            self.potential_customers = round(tot_pot_customers)
        elif self.climate == "Cloudy":
            tot_pot_customers = cust_from_temp - (cust_from_temp * 0.25)
            self.potential_customers = round(tot_pot_customers)
        elif self.climate == "Rainy":
            tot_pot_customers = cust_from_temp - (cust_from_temp * 0.65)
            self.potential_customers = round(tot_pot_customers)


class Inventory:

    def __init__(self, player_name):
        self.profit = 20
        self.cups = 0
        self.lemons = 0
        self.sugar = 0
        self.ice = 0
        self.price = 1.00
        self.name = player_name
        self.inv_list = [self.cups, self.lemons, self.sugar, self.ice]

    def __str__(self):
        return (f"\n{self.name.upper()}'S INVENTORY ~ ${self.profit:.2f}\n____________________\n{self.cups} cups"
            f"\n{self.lemons} lemons \n{self.sugar} cups of sugar\n{self.ice} ice cubes")

    def update_inventory(self):
        inv_dict = {"cups":self.cups, "lemons":self.lemons, "cups of sugar":self.sugar, "ice cubes":self.ice}

        item_dict = {
            "cups":{'25':'0.90', '50':'1.50', '100':'3.00'},
            "lemons":{'10':'0.60', '30':'2.50', '75':'4.50'},
            "cups of sugar":{'10':'0.65', '20':'1.75','50':'3.45'},
            "ice cubes":{'100':'0.95', '250':'2.30', '450':'3.50'}
        }

        update_again = True
        while update_again:
            for string, instance in inv_dict.items():
                add = input(f'\nWould you like to buy more {string}? ').lower()
                while add != 'yes' and add != 'no':
                    print('Please answer "Yes" or "No"')
                    add = input(f'\nWould you like to buy more {string}? ').lower()
                if add == 'yes':

                    amount = input(
                        f'\n{list(item_dict[string].keys())[0]} {string} ~ ${list(item_dict[string].values())[0]}'
                        f'\n{list(item_dict[string].keys())[1]} {string} ~ ${list(item_dict[string].values())[1]}'
                        f'\n{list(item_dict[string].keys())[2]} {string} ~ ${list(item_dict[string].values())[2]}'
                        f'\nHow many {string} would you like to buy? ')
                    while amount not in list(item_dict[string].keys()):
                        print(f'\nPlease answer {list(item_dict[string].keys())[0]}, {list(item_dict[string].keys())[1]},'
                              f' or {list(item_dict[string].keys())[2]}')
                        amount = input(
                            f'\n{list(item_dict[string].keys())[0]} {string} ~ ${list(item_dict[string].values())[0]}'
                            f'\n{list(item_dict[string].keys())[1]} {string} ~ ${list(item_dict[string].values())[1]}'
                            f'\n{list(item_dict[string].keys())[2]} {string} ~ ${list(item_dict[string].values())[2]}'
                            f'\nHow many {string} would you like to buy? ')

                    cost = float(item_dict[string][amount])
                    while cost > self.profit:
                        print("You don't have enough funds to make this purchase.")
                        add = input(f'\nWould you like to buy more {string}? ').lower()
                        while add != 'yes' and add != 'no':
                            print('Please answer "Yes" or "No"')
                            add = input(f'\nWould you like to buy more {string}? ').lower()
                        if add == 'yes':

                            amount = input(
                                f'\n{list(item_dict[string].keys())[0]} {string} ~ ${list(item_dict[string].values())[0]}'
                                f'\n{list(item_dict[string].keys())[1]} {string} ~ ${list(item_dict[string].values())[1]}'
                                f'\n{list(item_dict[string].keys())[2]} {string} ~ ${list(item_dict[string].values())[2]}'
                                f'\nHow many {string} would you like to buy? ')
                            while amount not in list(item_dict[string].keys()):
                                print(
                                    f'\nPlease answer {list(item_dict[string].keys())[0]}, {list(item_dict[string].keys())[1]},'
                                    f' or {list(item_dict[string].keys())[2]}')
                                amount = input(
                                    f'\n{list(item_dict[string].keys())[0]} {string} ~ ${list(item_dict[string].values())[0]}'
                                    f'\n{list(item_dict[string].keys())[1]} {string} ~ ${list(item_dict[string].values())[1]}'
                                    f'\n{list(item_dict[string].keys())[2]} {string} ~ ${list(item_dict[string].values())[2]}'
                                    f'\nHow many {string} would you like to buy? ')
                            cost = float(item_dict[string][amount])

                        elif add == 'no':
                            break

                    if add == 'no':
                        continue



                    if string == 'cups':  # updates amount of item after purchase
                        self.cups += int(amount)
                    elif string == 'lemons':
                        self.lemons += int(amount)
                    elif string == 'cups of sugar':
                        self.sugar += int(amount)
                    elif string == 'ice cubes':
                        self.ice += int(amount)
                    self.profit -= float(item_dict[string][amount])
                    print(self)
            update_str = input(f'\nWould you like to buy more supplies? ').lower()
            while update_str != 'yes' and update_str != 'no':
                print('Please answer "Yes" or "No"')
                update_str = input(f'\nWould you like to buy more supplies? ').lower()
            if update_str == 'yes':
                update_again = True
            elif update_str == 'no':
                update_again = False

    def post_sales_inv(self, cups_sold, product):
        self.profit += (cups_sold*product.price)
        self.cups -= cups_sold
        self.lemons -= ((cups_sold//8)*product.lemons_per_pitcher) #8 cups per pitcher
        self.sugar -= ((cups_sold//8)*product.sugar_per_pitcher)
        self.ice -= (cups_sold*product.ice_per_cup)



class Product:

    def __init__(self):
        self.price = 1.00
        self.lemons_per_pitcher = 4
        self.sugar_per_pitcher = 2
        self.ice_per_cup = 4

    def __str__(self):
        return (f'\nPRICE PER CUP ~ ${self.price:.2f}'
                f'\nLEMONS PER PITCHER ~ {self.lemons_per_pitcher}'
                f'\nSUGAR PER PITCHER ~ {self.sugar_per_pitcher}'
                f'\nICE PER CUP ~ {self.ice_per_cup}')

    def update_price(self):
        print(self)
        update = input('\nWould you like to update the price of your lemonade? ').lower()
        while update != 'yes' and update != 'no':
            print('Please answer "Yes" or "No"')
            update = input('\nWould you like to update the price of your lemonade? ').lower()
        if update == 'yes':
            price_confirmed = False
            while price_confirmed == False:
                try:
                    new_price = input('What is the new price of one cup of your lemonade? $')
                    self.price = float(new_price)

                    price_confirmation = input(f'Confirm price of ${self.price:.2f}? ').lower()
                    while price_confirmation != 'yes' and price_confirmation != 'no':
                        print('Please answer "Yes" or "No"')
                        price_confirmation = input(f'Confirm price of ${self.price:.2f}? ').lower()
                    if price_confirmation == 'yes':
                        price_confirmed = True

                except ValueError:
                    print('Please enter a valid number.')
            print(self)


    def update_ingredients(self):
        ingredients = ['lemons per pitcher', 'cups of sugar per pitcher', 'ice cubes per cup']
        update = True
        while update:
            for ingredient in ingredients:
                update_ingredient = input(f'\nWould you like to update the number of {ingredient}? ').lower()
                while update_ingredient != 'yes' and update_ingredient != 'no':
                    print('Please answer "Yes" or "No"')
                    update_ingredient = input(f'\nWould you like to update the number of {ingredient}? ').lower()
                if update_ingredient == 'yes':
                    updated = False
                    while updated == False:
                        try:
                            new_value = int(input(f'How many {ingredient}? '))
                            updated = True
                        except ValueError:
                            print('Please enter a valid whole number.')
                    if ingredient == 'lemons per pitcher':
                        self.lemons_per_pitcher = new_value
                    elif ingredient == 'cups of sugar per pitcher':
                        self.sugar_per_pitcher = new_value
                    elif ingredient == 'ice cubes per cup':
                        self.ice_per_cup = new_value
                    print(self)
            update_again = input('\nWould you like to update your ingredients again? ').lower()
            while update_again != 'yes' and update_again != 'no':
                print('Please answer "Yes" or "No"')
                update_again = input('\nWould you like to update your ingredients again? ').lower()
            if update_again == 'no':
                update = False
