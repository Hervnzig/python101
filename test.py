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


original_file = open("final_students.txt", 'r')
data_dict = {}
def txt_to_dict(original_f):
    for line in original_file:
        sub_dictionary = {}
        stud_info = line.strip().split(",")
        stud_id = int(stud_info[0].split(":")[1])

        for sub_section in stud_info:
            info = sub_section.strip().split(":")
            sub_dictionary[info[0]]= info[1]
        
        data_dict[stud_id] = sub_dictionary

    
    original_file.close
    # return data_dict
    print(data_dict)


txt_to_dict(original_file)

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
