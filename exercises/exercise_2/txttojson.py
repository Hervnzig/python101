import json


def txt_to_dict():
    original_file = open("exercises/exercise_1/final_students.txt", 'r')
    data_dict = []
    for column in original_file:
        sub_dictionary = {}
        stud_info = column.strip().split(",")
        # stud_id = stud_info[0].split(":")[1]

        for key_value in stud_info:
            info = key_value.strip().split(":")
            sub_dictionary[info[0]] = info[1]

        data_dict.append(sub_dictionary)

    print(data_dict)
    with open('exercises/exercise_2/data.json', 'w') as outfile:
        json.dump(data_dict, outfile, indent=2)
    original_file.close()
    return data_dict


txt_to_dict()
