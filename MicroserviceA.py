import os

with open("pipe.txt", "r") as file:
    if file.readline().strip() == "delete":
        date = file.readline().strip()
        lift_category = file.readline().strip()
    else:
        exit()


lift_file = lift_category + ".txt"

if os.path.isdir(date):
    file_path = os.path.join(date, lift_file)
    if os.path.exists(file_path):
        os.remove(file_path)

        with open("pipe.txt", "w") as file:
            file.write("Deletion Successful")
    else:
        with open("pipe.txt", "w") as file:
            file.write("Deletion Unsuccessful")
else:
    with open("pipe.txt", "w") as file:
        file.write("Deletion Unsuccessful")
