"""
 Problem: calculating powers is slow and confusing at times
target : Anyone who finds interest in this program
Target system: GNU/Linux
Functional Requirements: It should take in user input and calculate powers of the number given by the user to an extent the user requests
Testing:Simple Run Test
Maintainer:Barnerbruce93@gmail.com
"""
__version__ = 0.1 



print("""
╔┓┏╦━━╦┓╔┓╔━━╗╔╗
║┗┛║┗━╣┃║┃║╯╰║║║
║┏┓║┏━╣┗╣┗╣╰╯║╠╣
╚┛┗╩━━╩━╩━╩━━╝╚╝ 
""")

"""
Ummm this is my first  python so im not that good yet so if yr a better python programmer yr review would be greatly appreciated
you can s3nd yr review at barnerbruce93@gmail.com
"""
#well this part is self explanatory
print("this program will show the powers of a given number")
#this adds space to avoid making a confusing mess
print("\n")
#declares a variables that takes the users input
power = input("Enter the number you want to multiply\n")
#does the same as the other one
limit= input("Enter the number where the program should stop at\n")


#this declares a variable 
result = 1
counter  =0
#this is the main code that causes the loop
while result <int(limit):
	result *=int(power)
	counter +=1
	print(result,"     ","power",counter)
	#this code takes once the code above stops
else:
	print("Thanks for using my program")
	print("\n")
	print("This program was created by Its.Kenneth_zw")