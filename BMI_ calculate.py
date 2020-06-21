weight = int(input("Enter your weight(kg): "))
high= int(input("Enter your high(cm): "))
high = high/100
bmi = weight/(high*high)
print("BMI = ",bmi)