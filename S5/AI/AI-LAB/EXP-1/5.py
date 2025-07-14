sent=input("Enter the sentence")
lowercase = sent.lower()
uppercase=sent.upper()

print("uppercase ",uppercase)
print("lowercase ",lowercase)
newsent = sent.replace(' ','_')
print("replace sentence is: ",newsent)
count = len(sent)
print("no of chars ",count)

word = input("enter the word you need to check ")

if word in sent:
	print("present")
else:
	print("not present")
