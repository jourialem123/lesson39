height=int(input("Enter height"))
weight=int(input("Enter weight"))

bmi=weight/(height/100)**2
#if elif else
if bmi<=18:
    print ("You are underweight ",bmi)

elif bmi<=24.9:
    print("You are healthy ",bmi)

elif bmi<=29.9:
    print ("You are overweight ",bmi)
 
elif bmi<=34.9:
    print("You are severly overweight ",bmi)

elif bmi<=39.9:
    print("You are obese ",bmi)

else:
    print("You are severly obese ",bmi)
