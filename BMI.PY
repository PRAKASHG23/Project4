# Sample function:Evaluating the BMI
# BMI=Weght in kilograms/height in meters2
def bmi(weight ,height):
    return weight / height **2
print("Calculate your BMI")
weight=int(input("Enter your weight"))
height=int(input("Enter your height"))
print(bmi(weight,height))

# 1lb =0.45359237
def lb_to_kg(lb):
    return lb * 0.45359237
print(lb_to_kg(1))

# 1ft = 0.3048m
# 1 in =2.54cm =0.0254
def ft_and_inch_to_m(ft ,inch):
    return ft * 0.3048 + inch *0.0254
print(ft_and_inch_to_m(1,1))
