#Step 1st: create and open file

# Creating a file and writing initial student data

file=open("students_details.txt","w")

file.write("101,Adil, 90\n")
file.write("102,Pawan, 99\n")
file.write("103,Rahul, 70\n")

file.close()
