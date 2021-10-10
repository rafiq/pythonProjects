total = 0
count = 0
average = 0
# data = None

# while True:
#     data = input("Enter a number: ")

#     if data == "done" or data == "Done":
#         print(total,count,average)
#         break
#     elif type(data) == int:
#         dataInt = float(data)
#         total = total + dataInt
#         count = count + 1
#         average = total / count
#     else :
#         print("Invalid input")
#         continue


while True:
    str_val = input("Enter a number: ")
    if str_val == "done":
        print(total,count,average)
        break
    try:
        val = float(str_val)
    except:
        print("Invalid input")
        continue
    total += val
    count += 1
    average = total / count