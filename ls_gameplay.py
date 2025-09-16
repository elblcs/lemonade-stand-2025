import ls_classes


def price_threshold(potential_customers, price):

    if potential_customers < 40:
        if price <= 0.25:
            return 1.0*0.4
        elif 0.26 <= price <= 1:
            return 0.75*0.4
        elif 1.01<= price <= 1.75:
            return 0.5*0.4
        elif 1.76 <= price <= 3.50:
            return 0.25*0.4
        elif price > 3.50:
            return 0.1*0.4

    elif 40 <= potential_customers <= 80:
        if price <= 0.50:
            return 1.0*0.4
        elif 0.51 <= price <= 1.50:
            return 0.75*0.4
        elif 1.51<= price <= 2.50:
            return 0.5*0.4
        elif 2.51 <= price <= 3.50:
            return 0.25*0.4
        elif price > 3.50:
            return 0.1*0.4

    elif 81 <= potential_customers <= 120:
        if price <= 0.75:
            return 1.0*0.4
        elif 0.76 <= price <= 2.00:
            return 0.75*0.4
        elif 2.01<= price <= 3.25:
            return 0.5*0.4
        elif 3.26 <= price <= 4.50:
            return 0.25*0.4
        elif price > 4.50:
            return 0.1*0.4

    elif potential_customers >= 121:
        if price <= 1.00:
            return 1.0*0.4
        elif 1.01 <= price <= 2.25:
            return 0.75*0.4
        elif 2.26<= price <= 3.50:
            return 0.5*0.4
        elif 3.51 <= price <= 5.00:
            return 0.25*0.4
        elif price > 5:
            return 0.1*0.4

def lemons_threshold(lemons_per_pitcher):
    if 5<=lemons_per_pitcher<=7:
        return 1.0*0.2
    elif lemons_per_pitcher == 4:
        return 0.75*0.2
    elif lemons_per_pitcher == 3:
        return 0.5*0.2
    elif lemons_per_pitcher == 2:
        return 0.25*0.2
    elif 7 < lemons_per_pitcher < 2:
        return 0.1*0.2

def sugar_threshold(sugar_per_pitcher):
    if sugar_per_pitcher == 3:
        return 1.0*0.2
    elif sugar_per_pitcher == 2:
        return 0.75*0.2
    elif sugar_per_pitcher == 4:
        return 0.5*0.2
    elif sugar_per_pitcher == 1 or sugar_per_pitcher == 5:
        return 0.25*0.2
    elif sugar_per_pitcher > 5:
        return 0.1*0.2

def ice_threshold(temp, ice_per_pitcher):
    if 55 <= temp <= 64:
        if ice_per_pitcher >= 3:
            return 1.0*0.2
        elif ice_per_pitcher == 2:
            return 0.75*0.2
        elif ice_per_pitcher < 2:
            return 0.1*0.2

    elif 65 <= temp <= 74:
        if ice_per_pitcher >= 4:
            return 1.0*0.2
        elif ice_per_pitcher == 3:
            return 0.75*0.2
        elif ice_per_pitcher == 2:
            return 0.5*0.2
        elif ice_per_pitcher < 2:
            return 0.1*0.2

    elif 75 <= temp <= 84:
        if ice_per_pitcher >= 5:
            return 1.0*0.2
        elif ice_per_pitcher == 4:
            return 0.75*0.2
        elif ice_per_pitcher == 3:
            return 0.5*0.2
        elif ice_per_pitcher == 2:
            return 0.25*0.2
        elif ice_per_pitcher < 2:
            return 0.1*0.2

    elif temp >= 85:
        if ice_per_pitcher >= 6:
            return 1.0*0.2
        elif ice_per_pitcher == 5:
            return 0.75*0.2
        elif ice_per_pitcher == 4:
            return 0.5*0.2
        elif ice_per_pitcher == 3:
            return 0.25*0.2
        elif ice_per_pitcher < 3:
            return 0.1*0.2



def max_cups_sold(inventory, product, cups_demanded):
    cups_sold = cups_demanded

    if cups_sold > inventory.cups:
        cups_sold = inventory.cups

    max_cups_ice = inventory.ice // product.ice_per_cup
    if cups_sold > max_cups_ice:
        cups_sold = max_cups_ice

    max_pitchers_sugar = inventory.sugar / product.sugar_per_pitcher
    max_cups_sugar = int(max_pitchers_sugar*8)
    if cups_sold > max_cups_sugar:
        cups_sold = max_cups_sugar

    max_pitchers_lemons = inventory.lemons / product.lemons_per_pitcher
    max_cups_lemons = int(max_pitchers_lemons*8)
    if cups_sold > max_cups_lemons:
        cups_sold = max_cups_lemons

    return cups_sold


def find_cups_sold(potential_customers, product, temp, inventory):
    cups_sold = 0
    customers_percent = price_threshold(potential_customers, product.price) + lemons_threshold(product.lemons_per_pitcher) + sugar_threshold(product.sugar_per_pitcher) + ice_threshold(temp, product.ice_per_cup)
    cups_sold = round(customers_percent*potential_customers)
    max_cups = max_cups_sold(inventory, product, cups_sold)
    if cups_sold > max_cups:
        cups_sold = max_cups #FINAL
    return cups_sold



def new_day(inventory, day, product):
    day_conditions = ls_classes.DayConditions()  #creates conditions for day
    day_conditions.total_pot_customers() #calculates total potential customers of the day
    print(f'\nDAY {day}\nConditions: {day_conditions}')
    inp = input("Press ENTER to continue")
    print(inventory)
    inventory.update_inventory() #user may buy new items for their inventory
    product.update_price()
    product.update_ingredients()
    cups_sold = find_cups_sold(day_conditions.potential_customers, product, day_conditions.temp, inventory)
    print(f'You sold {cups_sold} cups of lemonade and earned ${cups_sold*product.price:.2f}!')
    inventory.post_sales_inv(cups_sold, product)


def main():
    directions_pointer = open('ls_directions.txt', 'r')
    directions = directions_pointer.read()  #reads file contents to a string
    directions_pointer.close()

    player_name = str(input("Please enter your name: "))
    intro = input(f"\nHello, and welcome to {player_name}'s Lemonade Stand! Press ENTER for directions.")
    print(directions)

    high_score = 0
    play_again = True
    start_game = input('Are you ready to play? ')

    while play_again:
        inventory = ls_classes.Inventory(player_name)
        product = ls_classes.Product()
        day = 1

        while day <= 7:
            new_day(inventory, day, product)
            day += 1

        print(f"\nYour final earnings were ${inventory.profit:.2f}!")
        if inventory.profit > high_score:
            high_score = inventory.profit
            print("NEW HIGH SCORE!!!")
        else:
            print(f'Better luck next time!\nScore to beat: ${high_score:.2f}')

        play_again_inp = input('Do you want to play again? ')
        while play_again_inp.lower() != 'yes' and play_again_inp.lower() != 'no':
            print('Please answer "Yes" or "No"')
            play_again_inp = input('Do you want to play again? ')
        if play_again_inp.lower() == 'yes':
            play_again = True
        elif play_again_inp.lower() == 'no':
            play_again = False



main()

