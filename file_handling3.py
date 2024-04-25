#Ralph Cyrel B. Ronda
#BSCPE 1-2
#Creating a line text (while using loop)

#creating a function to write mylife.txt
def write_to_file(filename):
    with open(filename. 'a') as file:
#will ask the user to enter any line of text and press 'n' to finish the loop
        while True:
            line = input("Enter a line to add to the file (or type 'n' to finish)")
            if line.lower() == 'n':
                break
            file.write(line + '\n')

#To print the line text into the file