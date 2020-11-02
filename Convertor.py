a = int(input("Enter the no. here - "))
x= str(input("enter the current unit - "))
y= str(input("Select the unit in which the no has to be converted - "))
# m = "metres"
# cm = "centimetres"
# kg = "Kilogram"
# g = "grams"
if x=="cm" and y == "m" :
    print(a, "cm in metre is :" , a/100)
if x=="m" and y == "cm" :
    print(a, "m in  centimetres is :" , a*100) 
if x=="g" and y == "kg" :
    print(a, "grams in kilogram is :" , a/1000)
if x=="kg" and y == "g" :
    print(a, "kilogram in grams is :" , a*1000)



