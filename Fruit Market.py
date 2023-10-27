Market = {}


try:
    with open("Market.txt", "r") as file:
        data = file.readlines()
        for line in data:
            Fruit_info = line.strip().split(',')
            fruitname = Fruit_info[0]
            Fruitqty = Fruit_info[1] 
            Fruitprice = float(Fruit_info[2])  
            Market[fruitname] = {'qty': Fruitqty, 'price': Fruitprice}
except FileNotFoundError:
    
    print("Market.txt file not found. Starting with an empty market.")

while True:

    print(" "*30, "Welcome To The Fruit Market")
    print("")
    print(" "*30, "1) Manager")
    print(" "*30, "2) Customer")
    print("")
    Role = int(input("Select Your Role : "))

    if Role == 1:

        while True:
            print(" "*30, "Fruit Market Manager")
            print("")
            print(" "*30, "1) Add Fruit Stock")
            print(" "*30, "2) View Fruit Stock")
            print(" "*30, "3) Update Fruit Stock")
            print("")
            Choice = int(input("Enter Your Choice :"))

            if Choice == 1:
                print("Add Fruit Stock")
                Fruitname = input("Enter Fruit Name : ")
                Fruitqty = int(input("Enter Fruit Quantity : "))
                Fruitprice = float(input("Enter Fruit Price : "))  

                Market[Fruitname] = {'qty': Fruitqty, 'price': Fruitprice}
            elif Choice == 2:
                print(Market)

            elif Choice == 3:
                fruitname = input("Enter Your Fruit Name : ")
                if fruitname in Market:
                    New_qty = int(input("Enter Fruit Quantity : "))
                    New_price = float(input("Enter Fruit Price : "))  

                    Market[fruitname]['qty'] = New_qty  
                    Market[fruitname]['price'] = New_price  
                    print("Fruit Info Updated Successfully")
                else:
                    print("Given Data Is Not Found")
            else:
                print("Error")

            perform = input("Do You Want To Perform More Operations : Press 'y' for Yes or 'n' for No : ")
            if perform.lower() != 'y':
                break

    else:
        print("Error")

    perform = input("Do You Want To Perform More Operations : Press 'y' for Yes or 'n' for No : ")
    if perform.lower() != 'y':
        break


with open("Market.txt", "w") as file:
    for fruitname, fruitdata in Market.items():
        file.write(f"{fruitname},{fruitdata['qty']},{fruitdata['price']}\n")
