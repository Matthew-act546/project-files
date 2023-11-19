#incomplete shitz
def main():
    print("How many digits are there in you're pin number?")
    num_pin = int(input(""))
    pin = int(input("Enter the you're pin here(space per number e.g 2 3 1 4):"))
    if num_pin == pin:
        pass
    else:
        list = [*range(pin[0], num_pin)]
        list.append(num_pin)

        print(list)
        
        def convertList(list1):  
            str = ''  # initializing the empty string  
            for i in list1: #Iterating and adding the list element to the str variable  
                str += i  
        return str  
  
    list1 = ["Hello"," My", " Name is ","Devansh"] #passing string   
    print(convertList(list1))

    for up_to in range(1, 9999999999):
        print(up_to)
    
        """
        factorial = 1
        num = 4
        for i in range(1,num + 1):
            factorial = factorial*i
            print(int("The factorial of",num,"is",factorial))"""


main()