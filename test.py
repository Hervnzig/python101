import json
# def txt_file_to_dict(txt_file):
#     studentData = {}
#     studentHandler = st.open_file(txt_file)
#     for student in studentHandler:
#         middleDict = {}
#         studentInfo = student.strip().split(",")
#         studentId = int(studentInfo[0].split(":")[1])
#         for line in studentInfo:
#             info = line.strip().split(":")
#             middleDict[info[0]]= info[1]
#         studentData[studentId] = middleDict
#     studentHandler.close
#     return studentData




# dictionary = {}
# with open("final_students.txt") as file:
#  for line in file:
 
#     (key, value) = line.split()
 
#     dictionary[int(key)] = value
 
# print ('\ntext file to dictionary=\n',dictionary)


# myfile = open("final_students.txt", 'r')
# data_dict = {}
# for line in myfile:
#     k, v = line.strip().split(',')
#     data_dict[k.strip()] = v.strip()
 
# myfile.close()
 
# print(' text file to dictionary =\n ',data_dict)
