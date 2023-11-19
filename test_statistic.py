def main():
    subject = input("Enter the subject of the test: ")
    items = int(input("Enter the items of the test: "))
    minutes = int(input("Enter the max minute time: "))
    seconds = minutes * 60

    answer = seconds / items
    if(answer >= 60):
        print("That's good you have plenty of time doing a single question")
    elif(answer <= 59 and answer >= 30):
        print("You can do it goodluck!")
    elif(answer <= 29 and answer >= 10):
        print("Speed is important than accuracy")
    elif(answer <=9 and answer >= 0):
        print("HOLYSHET")
    else:
        print("ERROR/404")        

    print(f"The {subject} test each items need to answer in {answer} seconds")
    again = input("Do you wanna enter again (y/n)")
    if again.lower() in 'y':
        main()
    else:
        print("Goodbye........... luv u")
main()