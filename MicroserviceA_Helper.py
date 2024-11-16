import time

date = input("Please enter the date of the lift category you would like to delete (YYYY-MM-DD): ")
lift_category = input("Please enter the lift category you would like to delete: ")

text = ["delete\n", date, "\n", lift_category]

with open("pipe.txt", "w") as file:
    for element in text:
        file.write(element)

time.sleep(20)

with open("pipe.txt", "r") as file:
    res = file.readline()
    print(res)