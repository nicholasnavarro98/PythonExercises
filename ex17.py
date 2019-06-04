from sys import argv
from os.path import exists 

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)


#we could do these two on one line, how ?

in_file = open(from_file)
in_data =in_file.read()

print "The Input file is %d bytes long" % len(in_data)
print "Ready, hit RETURN to continue, CTRL-C to Abort."
raw_input()


out_file = open(to_file, 'w')
out_file.write(in_data)


print "Alright, all done!"

out_file.close()
in_file.close()

