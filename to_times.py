print("MATH TABLE!!!")
help = """
   x = times 
   / = divide
   + = plus
   - = minus
"""
print(help)
respond = str(input("enter a specific math table: "))



if respond.lower() == 'x' or respond.lower() == 'times':
   print("Multiplication Table.\nEnter a number to times!")
   times = int(input())

   for i in range(1, 11):
      print(f"{i} x {times} = {i * times}")

elif respond.lower() == '/' or respond.lower() == 'divide':
   print("Division Table\nEnter a number to divide!")
   divide = int(input())

   for i in range(1, 11):
      print(f"{i} / {divide} = {i / divide}")

elif respond.lower() == '+' or respond.lower() == 'plus':
   print("The addition have no Table")
   print("There's a addition calculator if you want to use it [Y/N]")
   add_it = str(input())

   while True:
      if add_it.lower() == 'y':
         num1 = int(input("   "))
         num2 = int(input("+  "))
         print("_____\n", num1 + num2)
         break
      elif add_it.lower() == 'n':
         print("ok byeeeee")
         break
      else:
         print("please enter a specific letter\nTry again")
      add_it = str(input()) 

