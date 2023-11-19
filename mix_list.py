
mix_list = ['matt', 3.141262, True, 13, 15, 'pogi', 6, False, 2.5]

integers = []
strings = []
floats = []
booleans = []

for items in mix_list:
	if type(items) == int:
		integers.append(items)
	
	elif type(items) == str:
		strings.append(items)
	
	elif type(items) == float:
		floats.append(items)
	
	elif type(items) == bool:
		booleans.append(items)
	
	else:
		print("Unknown data type")

print(f"This is the original list:\n{mix_list}")

print(f"\nThis is the string of the\noriginal list: {strings}")

print(f"\nThis is the integer of the\noriginal list: {integers}")

print(f"\nThis is the float of the\noriginal list: {floats}")

print(f"\nThis is the boolean of the\noriginal list: {booleans}")

