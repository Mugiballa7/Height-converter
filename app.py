Height = input("Height : ")
unit = input("cm or ft or po")
cmSize = float(Height)
poSize = float(Height)*0.3937007874
ftSize = float(poSize)*0.83333333333

if unit == "cm":
    print("you measure " + Height + " cm")

elif unit == "po":
    print("in pouce, you measure:")
    print(poSize)

elif unit == "ft":
    print("in pouce, you measure:")
    print(ftSize)
