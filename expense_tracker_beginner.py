def expense_analyzer():
    total_expense = 0
    average = 0
    n = 0
    highest = 0 
    lowest = 0

    while True:
        inp = input("Enter your daily expense:- ")
        if inp.lower()=="done":
            break

        try:
            float_input = float(inp)
            if float_input < 0:
                print("Expense cannot be negative!!. Enter a valid number")
        except:
            print("Pls enter a valid value!!!! ")
            continue

    
        total_expense += float_input
        n += 1

        if highest is None or float_input:
            highest = float_input
        if lowest is None or float_input:
            lowest = float_input
    if n == 0:
        print("No expenses entered. Program Ended" )
        return
    

    average = total_expense/n
    print("----- Expense Summary ----- \n")
    print("Days recorded: ", n)
    print("Total expense: ", total_expense)
    print("Your average daily expense in", n, "days is", average)
    if average>500:
        print("Your average expenses per day in high range. Pls try to reduce them.")
    elif average>350:
        print("Your average is in medium range")
    elif average<350:
        print("Congratulations! Your average is in the perfect range.")
    print("Highest single day spend: ", highest)
    print("Lowest single day spend: ", lowest)

expense_analyzer()