#Ralph Cyrel B. Ronda
#BSCPE 1-2

#Creating a text file (odd and even)
def main():
    try:
        #read numbers from "number.txt"
        with open("number.txt", "r") as file:
            numbers = [int(line.strip()) for line in file.readlines()]
#create a text file name "number.txt" with 20 integers in it.

#extracting even and odd numbers from the file

#write even number to "even.txt" file.

#write odd number to "odd.txt" file.

#printing the proof of extracting