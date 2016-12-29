from sys import argv

# script, first, second, third = argv

# script, apple, orange, choclate = argv

# script, apple, = argv
script, apple, orange = argv
print "The script is called:", script
print "Your first variable is:", apple
print "Your second variable is:", orange
# print "Your third variable is:", choclate

third_variable = raw_input("What do you like to show?")

print "Now you get what you input %r" % third_variable
