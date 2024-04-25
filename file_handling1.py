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
        with open("even.txt", "w") as even_file:
            for num in even_numbers:
                even_file.write(str(num) + "\n")

        #write odd number to "odd.txt" file.
        with open("odd.txt", "w") as odd_file:
            for num in odd_numbers:
                odd_file.write(str(num) + "\n")

        #printing the proof of extracting
            print("Even and Odd numbers extracted and saved successfully.")

    except FileNotFoundError:
        print("Error: file 'number.txt' not found.")
    except Exception as e:
        print("An error has occurred: ", e)

if __name__ == "__main__":
    main()