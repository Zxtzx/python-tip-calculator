def get_numbers(question):
    while True:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter a valid number")

while True:
    bill = get_numbers("What was the total price of the bill?: ")
    while True:
        tip_type = input("Would you like % or Dollar Amount for tip? (%/$): ")

        if tip_type == "%":
            tip_precent = get_numbers("What precentage of tip would you like to leave?: ")
            tip = bill * tip_precent / 100
            break

        elif tip_type == "$":
            tip = get_numbers("How much of a tip would you like to leave?: ")
            break
        else:
            print("Please enter valid number")

    tax = bill * 0.13
    total = bill + tax + tip

    print(f"Bill: ${bill:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Tip: ${tip:.2f}")
    print(f"Total: ${total:.2f}")


    while True:
        again = input("Would you like to calculate another bill? (Yes/No): ").lower()

        if again == "yes":
            break
        elif again == "no":
            quit()
        else:
            print("Please enter either Yes or No!")
            
            


   
        









    