sum = 0
Name = input("Enter Name : ")
Item = input('Enter Product : ')
while (True):
	userInput = input("Enter the price of Item : ")
	if (userInput!='q'):
		sum = sum + int(userInput)
		print(f"Order total : {sum}")
	else:
		print(f"Your Bill total is {sum}. Thanks for shopping with us")
		break
