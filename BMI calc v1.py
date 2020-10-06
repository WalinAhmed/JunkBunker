mass= float(input('Enter Your Mass(kg)= '))
height_ft= float(input('Enter Your Height(ft)= '))
height_mtr= height_ft * 0.3048
print('BMI Calculator')
BMI = mass / (height_mtr**2)
print('Your BMI is:', "{:.2f}".format(BMI))
msg= 'You are'
if BMI <= 15:
    print(msg, 'Very severely underweight')
elif 15< BMI <=16:
    print(msg,'Severely underweight')
elif 16< BMI <=18.5:
    print(msg, 'Underweight	')
elif 18.5< BMI <=25:
    print(msg, 'Normal (healthy weight)')
elif 25< BMI <=30:
    print(msg, 'Overweight')
elif 30< BMI <= 35:
    print(msg, 'Obese Class I (Moderately obese)')
elif 35< BMI <= 40:
    print(msg, 'Obese Class II (Severely obese)')
elif BMI > 40:
    print('Obese Class III (Very severely obese)')