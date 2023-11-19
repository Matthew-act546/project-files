def main():
    code = ["AB0001", "CT0102", "JFO203", "AR0304", "JA0405", "CL0506", "RN06070"]

    employee_code = input("Enter employee code: ")

    if employee_code in code:
        if employee_code == "ab0001":
            print("Aileen Bisnar")
        elif employee_code.upper() in "CT0102":
            print("Christine Torres")
        elif employee_code.upper() in "Jf0203":
            print("Jennylyn Forte")
        elif employee_code.upper() in "AR0304":
            print("Alan Ranario")
        elif employee_code.upper() in "JA0405":
            print("Jeffrey arienza")
        elif employee_code.upper() in "CL0506":
            print("Christopher Lanoria")
        elif employee_code.upper() in "RN0607":
            print("Ramil Nacario")
        else:
            print(f"The code that you enter does not exist in our employee_code")
    # else:
    #     print("Pls enter the right employee code")
    #     main()

main()