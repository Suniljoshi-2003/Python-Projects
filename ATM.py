
# import time
# print("Please insert your CARD")
# time.sleep(5)
# password = 1234
# pin = int(input("enter your ATM Pin..."))
# balance = 5000
# if pin == password:
#     while True:

#         print("""
#             1 == balance
#             2 == withdraw amount
#             3 == deposie balance
#             4 == exit
#             """)
#         try :
#             option = int (input("Please enter your choice "))
#         except :
#             print("Please enter valid option")
        
#         if option == 1:
#             print(f"your current balance is {balance}")
#         if option == 2:
#             withdraw_amount = int(input("Please enter withdraw_amount"))
#             balance = balance - withdraw_amount
#         print(f"{withdraw_amount} is debited from your account")
#         print(f"your current balance is {balance}")

#         if option == 3:
#             deposite_amount =int(input("please entere deposite _amount"))
#             balance = balance + deposite_amount
#             print(f"{deposite_amount} is creadited to ypur account")
#             print(f"your updated balance is {balance}")

#         if option == 4:
#           break


# else:
#     print("Worng Pin...! Please try again.")    

import time

# Initial setup
print("Please insert your CARD")
time.sleep(5)
password = 1234
balance = 5000

# PIN validation
pin = int(input("Enter your ATM Pin: "))
if pin == password:
    while True:
        print("""
        1 == Check Balance
        2 == Withdraw Amount
        3 == Deposit Amount
        4 == Exit
        """)
        
        # Handle invalid input for the menu option
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 4.")
            continue
        
        # Check Balance
        if option == 1:
            print(f"Your current balance is Rs.{balance}")
        
        # Withdraw Amount
        elif option == 2:
            try:
                withdraw_amount = int(input("Please enter withdraw amount: "))
                if withdraw_amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= withdraw_amount
                    print(f"Rs.{withdraw_amount} has been debited from your account.")
                    print(f"Your current balance is Rs.{balance}")
            except ValueError:
                print("Invalid input! Please enter a valid amount.")
        
        # Deposit Amount
        elif option == 3:
            try:
                deposit_amount = int(input("Please enter deposit amount: "))
                balance += deposit_amount
                print(f"Rs.{deposit_amount} has been credited to your account.")
                print(f"Your updated balance is Rs.{balance}")
            except ValueError:
                print("Invalid input! Please enter a valid amount.")
        
        # Exit
        elif option == 4:
            print("Thank you for using the ATM. Have a nice day!")
            break
        
        # Handle invalid menu options
        else:
            print("Invalid choice! Please enter a number from 1 to 4.")
else:
    print("Wrong Pin! Please try again.")
    
def odd_or_even(number):
    if number / 2 ==0:
        return "Even"
    else:
        return "Odd"