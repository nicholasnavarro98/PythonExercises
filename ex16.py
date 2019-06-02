from sys import argv # From System Module we imported Argv functions
script, filename = argv # script and filename are the parameters to run program


print "We're going to erase %r." % filename #prints line with %r being replaced with file filename
print "If you don't want that, hit CTRL-C(^C)"#prints line telling user to use shortcut to end program
print "If you do want that, hit RETURN." #prints line telling user to hit enter to continue script

raw_input("?") #detecs user input with ? as prompt

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate

print "Now I'm going to ask you for three lines"

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And now, we will close the file"

target.close()
