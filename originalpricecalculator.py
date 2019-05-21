#program to calucale original price



# ask user the discounted price and percentages, and initialise the variables

print "What is the discounted price?"
discountedPrice = int(raw_input())
print"What is the percentage discount?"
discountPercentage = int(raw_input())

#initialise formula

formula = (discountedPrice * 100)/(100 - discountPercentage)

#text that shows the answer

answerTxt = "The orignal price was EUR: "

#prints the answer
print answerTxt,formula 

