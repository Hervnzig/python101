original_file = open("final_students.txt", 'r')
data_dict = {}
def txt_to_dict(original_f):
    for column in original_file:
        sub_dictionary = {}
        stud_info = column.strip().split(",")
        stud_id = int(stud_info[0].split(":")[1])

        for key_value in stud_info:
            info = key_value.strip().split(":")
            sub_dictionary[info[0]]= info[1]
        
        data_dict[stud_id] = sub_dictionary

    
    print(data_dict)
    with open('data.json', 'w') as outfile:
        json.dump(data_dict, outfile)
    original_file.close
    return data_dict


txt_to_dict(original_file)