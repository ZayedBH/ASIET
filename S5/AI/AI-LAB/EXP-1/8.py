n = int (input("enter the mark"))

if n>= 90 and n <= 100:
	print("grade A")
elif n>= 75 and n<= 89:
	print("grade B")
elif n>= 60 and n<= 74:
	print("grade C")
elif n>=40 and n<= 59:
	print("grade D")
elif n<40 and n >= 0: 
	print("fail")
else:
	print("enter valid grade")
