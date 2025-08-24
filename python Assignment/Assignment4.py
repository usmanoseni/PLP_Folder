
# code that helps to read a file
file = open('input.txt', 'r')
data = file.read()
print(data)

hold = open('input.txt', 'w')
hold.write("This is a new line added to the new file created.")
hold.close()

# code that accept file name from the user and perform error handling
fileName = str(input("Enter the file name with their extension: "))

# Validate file extension
while not (fileName.endswith('.txt') or fileName.endswith('.pdf')):
    print("Invalid file name. Please enter a valid .txt or .pdf file name.")
    fileName = str(input("Enter the file name with their extension: "))

try:
    with open(fileName, 'r') as files:
        dataInfo = files.read()
        print(dataInfo)
except FileNotFoundError:
    print(
        f"The file {fileName} was not found. Please check the file name and try again.")
finally:
    print("Thank you for using the file reader program.")
