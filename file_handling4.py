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

        with open(output_double_filename, "w") as output_double_file:
            for num_squared in even_numbers_squared:
                output_double_filewrite(str(num_squared) + "\n")

        with open(output_triple_filename, "w") as output_triple_file:
            for num_cubed in odd_numbers_cubed:
                output_triple_file.write(str(num_cubed) + "\n")

        print("Completed. Check the files.")
#extracting the integers to its respective file