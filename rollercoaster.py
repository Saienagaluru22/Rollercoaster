print("Welcome to the Rollercoaster!!!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    bill = 0
    if age < 12:
        bill = 5
        print("You have to pay $5.")
    elif age <= 18 :
        bill = 7
        print("You have to pay $7.")
    else:
        bill = 12
        print("You have to pay $12.")

    wants_photo = input("Do you want a photo taken? Yes or No. ")
    if wants_photo == "Yes":
         bill += 3
        
    print(f"your final bill is {bill}.")

else:
    print("You can not ride the rollercoaster.Sorry, better luck next time!")
