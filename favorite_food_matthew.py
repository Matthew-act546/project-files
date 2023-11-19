fav_food = ['pancit canton', 'hotdog', 'egg']

print("Matthew favourite food is\n" + str(fav_food))

print("\nDo you want to add matthew favorite\nfood?\nyes or no?")
typo = input()

if typo == "yes" or typo == "YES":
	print("What food you want to add?")
	addFood = input()
	fav_food.append(addFood)
	if addFood == fav_food[1] or addFood == fav_food[2]:
		print("The food " + str("'" + addFood +"'") + " is in the\nfavourite food " +"already")
	if addFood == fav_food[0]:
		print("The food " + str("'" + addFood +"'") + " is in the\nfavourite food " +"already")
	else:
		fav_food.sort()
		print(fav_food)
elif typo == "no" or typo == "NO":
	print("Sadly you're not matthew friends or\nreletive because you didn't no about matthew favourite food. bye...")
else:
	print("404/ERROR")
