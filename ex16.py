from sys import argv # From System Module we imported Argv functions
script, filename = argv # script and filename are the parameters to run program


print "We're going to erase %r." % filename #prints line with %r being replaced with file filename
print "If you don't want that, hit CTRL-C(^C)"#prints line telling user to use shortcut to end program
print "If you do want that, hit RETURN." #prints line telling user to hit enter to continue script

raw_input("?") #detecs user input with ? as prompt

print "Opening the file..." #tells the user that opening the file
target = open(filename, 'w') #open(filename) is the file, and its stored in the 'target' variable

print "Truncating the file. Goodbye!" #telling user that file is Truncating
target.truncate #target file has been truncated

print "Now I'm going to ask you for three lines" #message to tell user to enter three lines

line1 = raw_input("line1:") # three lines that prompts the user to enter a string	
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write these to the file." # tells user that its writing to file

target.write(line1) #target. write = writing the lines to 'target'
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And now, we will close the file" #tells user target is closing

target.close() # 'target' is closed using .close method
