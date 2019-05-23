#program to calucale original price



# ask user the discounted price and percentages, and initialise the variables

print "What is the discounted price?"
discountedPrice = int(raw_input())


    
print"What is the percentage discount?"
discountPercentage = int(raw_input())




def calculation(x,y):
   return (x * 100)/(100 - y) 
   #this is the formula for calculating the original price of a discounted object
   #where x is the discounted price, and y is the percantage of which its discounted
   
  
    
 


#text that shows the answer

answerTxt = "The orignal price was EUR: "

#prints the answer
print answerTxt,calculation(discountedPrice,discountPercentage)
