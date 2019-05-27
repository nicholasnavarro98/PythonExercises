from sys import argv

script, filename = argv

txt = open(filename)


print "Here's your file %r:" % filename 
print txt.read()
txtclose = txt.close()

print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)

print txt_again.read()
txt_again_close = txt_again.close()

print "would you like to close this file? Y/N"
fileClose = raw_input('> ')
if fileClose == 'Y':
    txtclose
    txt_again_close
else:
    print "It's important to close files once you're done with them"




