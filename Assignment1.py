#Programmed by Darla Torres
#July 10, 2017

print "-- Original Recipe --"

print "Enter the amount of Flour (cups):",
Flour = raw_input()
print "Enter the amount of water (cups):",
water = raw_input()
print "Enter the amount of salt (teaspoons):",
salt = raw_input()
print "Enter the amount of yeast (teaspoons):",
yeast = raw_input()
print "Enter the loaf adjustment factor (e.g. 2.0 doubles the size):",
factor = raw_input()

print "-- Modified Recipe --"
print "BreadFlour: %0.2f cups." %(float(Flour)*int(factor))
print "Water: %0.2f cups." %(float(water)*int(factor))
print "Salt: %0.2f teaspoons." %(float(salt)*int(factor))
print "Yeast: %0.2f teaspoons." %(float(yeast)*int(factor))
print "Happy Baking!"

