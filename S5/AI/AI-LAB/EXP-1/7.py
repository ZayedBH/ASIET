
a=int(input("enter the first number"))


b=int(input("enter the second number"))

n = int(input("enter the choice of operation \n1:addition \n2 :subtraction \n3 : multiplication \n4 division:"))


if n == 1:
	print("addition ",a+b)
elif n==2:
	print("subtraction ",a-b)
elif n==3:
	print("multiplication ",a*b)
elif n==4:

	if b == 0:
		print("error")
	else:
		print("division ",a/b)
else:
	print("enter valid choice")
