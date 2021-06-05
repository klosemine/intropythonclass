# is comments aka notes
name = "Elon Musk"    # String  -
age = 49     # Integer
isGoodLooking = True    # boolean  -
height = 1.88    # float
height = height * 1.02    # Elon Musk grew taller by 2%   - assignment
name = "Sir Elon Musk"

# Genius Elon Musk is 49 this year and stands at 1.88 m tall
print("Genius {} is {} this year and stands at {:.2f} m tall".format(name, age, height))
age = age + 10 # 49 + 10 = 59 --> age variable
# variable = <value>
print("He will be {} years old in 10 years' time.".format(age))

if isGoodLooking:    # if isGoodLooking == True
    print("{} looks very handsome".format(name))
else:
    print("{} needs to take care of his face".format(name))

