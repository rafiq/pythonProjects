# name = input("What is your name?\n")
# print("Hello " + name + ". I am glad to meet you.")

hours = float(input("How many hours did you work?"))
rate = float(input("What was your hourly rate?"))
over_time_rate = 1.5
extra_pay = 0

if hours > 40:
    overHours = abs(40 - hours)
    hours = hours - overHours
    extra_pay = overHours * over_time_rate

result = float(hours) * float(rate) + extra_pay
print("Pay: " + str(result),extra_pay)