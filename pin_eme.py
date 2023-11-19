def main():
	print("Enter you're pin password:")
	pin = int(input())

	for up_to in range(999, 9999999):
		print(up_to+1, end=" ")
		
		
		if pin <= 999:
			print("\n\nThe PIN password is supposed 4 numbers not 3 or 2 numbers.")
			break
		elif up_to == pin:
			#print(exe, end="\n")
			print("<-- we found you're pin number")
			break
		else:
			print("INCORRECT")

if __name__ == '__main__':
	main()