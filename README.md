A. Requesting Data

You are able to request data from the microservice by first getting the date and lift category data of the file you want to delete from the user. This data will be stored in an array
with the string "delete" in the first slot. Then the program will open a pipe txt. file, and write each piece of data into its own line within the file. The program will then
go to sleep in order to wait for the microservice to run. 

Request Example:

```python
date = input("Please enter the date of the lift category you would like to delete (YYYY-MM-DD): ")
lift_category = input("Please enter the lift category you would like to delete: ")

text = ["delete\n", date, "\n", lift_category]

with open("pipe.txt", "w") as file:
    for element in text:
        file.write(element)

time.sleep(10)
```

B. Receiving Data

After the microservice is finished processing by writing whether it has successfully or unsuccessfully deleted the lift category file into the pipe txt. file, the program will stop sleeping and
can recieve the deletion status message by reading the pipe txt. file. This message can then be stored in a variable, and that variable can be printed so that the user is informed if the request was
successful or not. 

Receive Example:

```python
with open("pipe.txt", "r") as file:
    message = file.readline()
    print(message)
```

C. UML Sequence Diagram

![image](https://github.com/user-attachments/assets/9db8e380-6bbb-4693-a247-ddac652bb06c)
