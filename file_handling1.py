#Ralph Cyrel B. Ronda
#BSCPE 1-2
#create a text file name "number.txt" with 20 integers in it.
#Creating a text file (odd and even)
def main():
    try:
        #read numbers from "number.txt"
        with open("number.txt", "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]
#extracting even and odd numbers from the file
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
#write even number to "even.txt" file.

#write odd number to "odd.txt" file.

#printing the proof of extracting