def calculate(height, weight):

    return round((weight/height**2), 1)

def body(user):

    for i in range(user):
          name = input("Enter your name:")
          print(f"user{i}=", name)

          h = float(input("Enter your height in meters: "))
          w = float(input("Enter your weight in kg: "))

          bmi = calculate(h, w)
          print("BMI is:"+str(bmi))

          if bmi < 18.5:
             print('Underweight')
          elif bmi >= 18.5 and bmi < 25:
             print("Normal")
          elif bmi >= 25 and bmi < 30:
             print('Overweight')
          else:
             print('Obesity')
    print("Thank you! Process has been finished ")

user =int(input("Enter how many people:"))
body(user)






