def format_name(f_name, l_name):
    formated_fname = f_name.title()
    formated_lname = l_name.title()
    return f"{formated_fname} {formated_lname}"

print(format_name("shree", "nayak"))

def functin1(text):
    return text + text

def function2(text):
    return text.title()

print(function2(functin1("hello")))