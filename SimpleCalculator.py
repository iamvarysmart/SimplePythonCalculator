

def main():
	print("\nWelcome to the simple calculations!\n")
	numOne = input("Please enter the first number!")
	numTwo = input("Please enter the second number!")

	print("\n\nSelect mathematical operation from the list provided")
	print("1-Addition")
	print("2-Subtraction")
	print("3-Multiplication")
	print("4-Division")

	process = raw_input("user selection:")

	if process == "1":
		total = Addition(numOne,numTwo)
		
	elif process == "2":
			total = Subtraction(numOne, numTwo)
	elif process == "3":
			total = Multipication(numOne, numTwo)
	elif process == "4":
			total = Division(numOne,numTwo)
	else:
		print("You did not select a proper option")


def Addition(numOne, numTwo):
	total = numOne + numTwo
	print("\n\nwhen " + str(numOne) + " is added to " + str(numTwo) + " the total is " + str(total))

def Subtraction(numOne, numTwo):
	total = numOne - numTwo
	print("\n\nwhen " + str(numTwo) + " is subtracted from " + str(numOne) + " the total is " + str(total))

def Multipication(numOne, numTwo):
	total = numOne * numTwo
	print("\n\nwhen " + str(numOne) + " is multiplied by " + str(numTwo) + " the total is " + str(total))

def Division(numOne, numTwo):
	total = numOne / numTwo
	print("\n\nwhen " + str(numOne) + " is divided by " + str(numTwo) + " the total is " + str(total))

main()
