
is_sunny = False

have_umbrella=True

is_sunny = input("is it sunny y/n ")
if is_sunny == "y":
	is_sunny=True
else:
	is_sunny=False
	
have_umbrella = input("do you have umbrella y/n ")
if have_umbrella == "y":
	have_umbrella=True
else:
	have_umbrella=False

if is_sunny == True and have_umbrella == True :
	print("you should go outside")
elif is_sunny == False and have_umbrella == True:
	print("do  carry umbrella")
elif is_sunny == True and have_umbrella == False:  
	print("no need f0r umbrella")
else:
	print("dont go outside")
