#Ralph Cyrel B. Ronda
#BSCPE 1-2
#Creating a text file (double or triple)

#creating a list of 20 integers in text file named "integers.txt"
def process_integers(integers_txt, output_double_filename, output_triple_filename):
#create a code that will read the file
    try:
        with open("integers.txt", "r") as input_file:
            numbers = [int(line.strip()) for line in input_file.readlines()]

#creating a code that will find the double and triple of the following integers.
        even_numbers_squared = [num ** 2 for num in numbers if num % 2 == 0]
        odd_numbers_square = [num ** 3 for num in numbers if num % 2 != 0]

#extracting the integers to its respective file