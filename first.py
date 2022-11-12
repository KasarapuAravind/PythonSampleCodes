bill = 0

height = int(input("enter your height"))
if height >= 120:
    print("you can ride rollercoaster")
    age = int(input("enter your age"))
    if age < 12 :
        bill = 5
        print("at $5")
    elif age < 18 :
        bill = 7
        print("at $7")
    elif age >= 45 and age <= 55:
        print("you can ride for free")
    else:
        bill = 12
        print("at $12")
    pic = input("do you want to take pic?")
    if pic == "Y":
        bill += 3

    print(f"final bil is{bill}")

else: 
    print("you cannot ride")
