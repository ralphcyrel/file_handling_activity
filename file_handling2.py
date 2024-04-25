#Ralph Cyrel B. Ronda
#BSCPE 1-2
#Creating a list of students with GWA

#create a text file named "student_data.txt" with 20 students with GWA in it.
def main():
    try:
    #Read the student data from file
        with open("student_data.txt", "r") as file:
            lines = file.readlines()
    #Creating student data and find highest GWA
        highest_gwa = 0.0
        highest_gwa_student = ""
        for line in line:
            parts = line.strip().split(",")
            if len(parts) == 2:
                name, gwa_str = parts
                    try:
                        gwa = float(gwa_str)
                        if gwa > highest_gwa:
                            highest_gwa = gwa
                            highest_gwa_student = name
                        excep ValueError:
                            print(f"Invalid GWA for student {name}: ({highest_gwa})")
                        else:
                            print("No valid student data found.")





highest_gwa_student = name

    #Printing the output
