#Array Experimenting 
from __future__ import print_function


print ("Hello, Welcome to the Answer")
print ("Is your name Nick? Y/N \n")
ques1 = str(raw_input())
if ques1 == "Y":
	isNick = True
else:
	isNick = False

print("Are you awake? Y/N \n")
ques2 = str(raw_input())
if ques2 == "Y":
	isAwake = True
else:
	isAwake = False
	

ans1 = ["The","Answer","Is","Yes"]
ans2 = ["The", "Answer", "Is", "No"]
ans3 = ["There", "Is", "No", "Answer"]
ans4 = ["There", "Is", "Nothing", "To", "See"] 

counter = 0
if isAwake == True & isNick == True:
	while counter != 100:
            for x in ans1:
                print (x, end="")
                counter = counter + 1
elif isAwake == False & isNick == True:
	while counter != 100:  
            for x in ans2:
                print (x, end="")
                counter = counter + 1
elif isAwake == True & isNick == False:
	while counter != 100:  
            for x in ans3:
                print (x, end="")
                counter = counter + 1
elif isAwake == False & isNick == False:
	while counter != 100:  
            for x in ans4:
                print (x, end="")
                counter = counter + 1
else:
    print ("You have broken me.")
          
       
		
