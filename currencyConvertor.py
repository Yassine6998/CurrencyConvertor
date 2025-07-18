# Import the module of time and os
import time
import os

# Make a variable for the ascii money
asciiDollar="""
||====================================================================||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||
||\\$//        ~         '------========--------'                \\$//||
||<< /        /$\              // ____ \\                         \ >>||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
||<<|        \\ //           || <||  >\  ||                        |>>||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLAR =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
"""

# Make a dictionary for the currencies
currencies={
    'USD':1.0, 
    'MAR':9.05,
    'EUR':0.86, 
    'EGP':49.42, 
    'RMB':7.17,
    'JPY':148.0,
    'GBP':0.74,
    'AUD':1.53,
    'CHF':0.8,
    'SAR':3.75,

}

# Define a function to clear the screen
def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear' )
# Define a function that shows the dashbaord
def showDashbaord():

    # Print the ascii art and the list of prices
    print('Welcome to the currency\'s convertor: ')
    print(asciiDollar)
    print('Here is the prices of every currency compared to the dollar: \n')

    for currency in currencies:
        print(f'{currency}: {currencies[currency]}')

# Define a function to convert the currency
def convertCurrency():
    # Clear the Screen
    clearScreen()

    # Show the dashbaord
    showDashbaord()

    # Take the currency to convert from the user
    currencyToConvertFrom=input('\nEnter the currency to convert from \n').upper()

    # Check if the currency in the dictionary

    if currencyToConvertFrom in currencies: 
        # Take the input of the amount from the user

        amount=float(input('Enter the amount: \n'))

        # Check if the confirmation of the user

        while input(f'You entered {amount} {currencyToConvertFrom}. Confirm (y/n)').lower()!='y':
            amount=float(input('Enter the amount: '))

        # Clear the screen
        clearScreen()

        currencyToConvertTo=input('Enter the currency to convert to \n').upper()
        # Check if the currency in the dictionary

        if currencyToConvertTo in currencies: 
            # Some time module tricks (Labor Illusion)
            print('Analyzing your request...Please wait')
            time.sleep(2)
            print(f'Checking for {currencyToConvertTo}\'s best rates available...Please wait')
            time.sleep(2)
            print(f'Getting a discount for {currencyToConvertFrom}...Please wait')
            time.sleep(2)

            # Clear the screen
            clearScreen()

            print(f'Preparing the deal from {currencyToConvertFrom} to {currencyToConvertTo}...Please wait')
            time.sleep(2)
            
            # Calculate the rate and make it an a variable
            rate=currencies[currencyToConvertTo]/currencies[currencyToConvertFrom]

            # Print the prices

            print(f'\nExchange Rate: 1 {currencyToConvertFrom} = {rate} {currencyToConvertTo}\n')
            print(f'{amount} {currencyToConvertFrom} is equal to {round(amount*rate, 2)} {currencyToConvertTo}') # Round for two numbers after the comma

            # Check if the user accpet the transaction and the price
            if input('Did you accpet this transaction (y/n)').lower()!='y':
                print('Transaction canceled!')
            else:
                print('Transaction succeed!!')

            # Check if the user want to make another transaction

            if input('Do you want to make another transaction : (y/n)').lower()=='y':
                convertCurrency()
            else:
                print('Exiting the program...')

        else:
            print('Invalid currency. Transaction failed...')
            time.sleep(4)
            convertCurrency()

    else:
        # Print that the transaciton canceled
        print('Invalid currency. Transaction failed...')
        time.sleep(4)
        convertCurrency()

# Call the function 
convertCurrency()










    
        



    




