import re

initial_students_file = 'students.txt'
final_students = 'final_students.txt'
no_trials = [0]

try:
    with open(final_students) as file:
        pass
except IOError:
    open(final_students, 'x')

id_input = input("Please provide studentID: ")


def check_if_id_exists(input_id, initial_initial_students_file):
    check_id_existence = False
    opened_file = open(initial_initial_students_file, 'r')

    for line in opened_file:

        student_id = line.split(',')[0].split(':')[1]
        if student_id == input_id:
            check_id_existence = True
            print(student_id)
            break
        else:
            check_id_existence = False
    return check_id_existence


def password_validation(password_input):
    error_prompt = []
    valid_special_char_regex = re.compile('[@_#$%^&*()\-\"<>?/\|}{~:]')
    reserved_special_char_regex = re.compile('[!=+]')
    is_valid = True

    # check for upper case
    if not any(char.isupper() for char in password_input):
        is_valid = False
        error_prompt.append("No upper cases")

    # check for lower case
    if not any(char.lower() for char in password_input):
        is_valid = False
        error_prompt.append("No lower cases")

    # check for digit character
    if not any(char.isdigit() for char in password_input):
        is_valid = False
        error_prompt.append("No numbers in your password")

    # check for length
    if len(password_input) < 8:
        is_valid = False
        error_prompt.append("Minimum of 8 charcter")

    # check for allowed special charcter
    if valid_special_char_regex.search(password_input) is None:
        is_valid = False
        error_prompt.append("No special character")

    # check for reserved special charcter
    if reserved_special_char_regex.search(password_input) is None:
        pass
    else:
        is_valid = False
        error_prompt.append('These characters (+,! or = ) are not allowed')

    #  display errors commited if password is not valid
    if not is_valid:
        print("Try again, Below is the error details: ")

        for error in error_prompt:
            print(error)
        print("______________________________________________________________ \n \n")
    return is_valid


def set_password(student_id):
    password_input = input("Please provide a password: ")
    no_trials[0] = no_trials[0] + 1

    if not password_validation(password_input):

        if no_trials < [3]:
            print("You still have: ", 3 - no_trials[0], " trials")
            return set_password(student_id)
        else:
            print("You have reached your 3 trials... Bye!")
            return -1
    else:
        update_password(password_input, student_id)


def update_password(password_input, student_id):
    opened_file = open(initial_students_file, 'r')

    if check_if_id_exists(student_id, final_students):
        print("Your password is already updated")
        pass
    else:
        for line in opened_file:
            line_array = line.split(',')
            id_section = line_array[0]
            id_section_array = id_section.split(':')
            id_student = id_section_array[1]
            if id_student == student_id:
                firstnamePart = line_array[1]
                firstnamePartArray = firstnamePart.split(':')
                firstname = firstnamePartArray[1]
                lastnamePart = line_array[2]
                lastnamePartArray = lastnamePart.split(':')
                lastname = lastnamePartArray[1].strip()
                write_to_final_file = open(final_students, 'a')
                L = ["id:" + student_id + "," + "firstname:" + firstname + "," + "lastname:" + lastname +
                     ",password:" + password_input + "\n"]
                write_to_final_file.writelines(L)
                print("Successfully updated student password")

                break


if check_if_id_exists(id_input, initial_students_file):
    set_password(id_input)
else:
    print("that student does not exist")