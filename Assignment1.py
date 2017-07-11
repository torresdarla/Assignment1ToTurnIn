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

print ""

print "-- Modified Recipe --"
print "BreadFlour: %0.2f cups." %(float(Flour)*float(factor))
print "Water: %0.2f cups." %(float(water)*float(factor))
print "Salt: %0.2f teaspoons." %(float(salt)*float(factor))
print "Yeast: %0.2f teaspoons." %(float(yeast)*float(factor))
print "Happy Baking!"
20/4
print ""
print "-- Modified Recipe in Grams--"
print "BreadFlour: %0.2f grams." %(float(Flour)*float(factor)*120.00)
print "Water: %0.2f grams." %(float(water)*float(factor)*237.00)
print "Salt: %0.2f grams." %(float(salt)*float(factor)*5.00)
print "Yeast: %0.2f grams." %(float(yeast)*float(factor)*3.00)
print "Happy Baking!"
