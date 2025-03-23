#Task 1
def first_name(my_first_name:str):
    return(my_first_name)

    """
    Returns the first name.

    Args:
        my_first_name (str): The first name to return.

    Returns:
        str: The first name.
    """

def last_name(my_last_name:str):
    return(my_last_name)

    """
    Returns the last name.

    Args:
        my_last_name (str): The last name to return.

    Returns:
        str: The last name.
    """

def fullname(my_first_name: str, my_last_name: str):
    
    """
    Combines the first and last names into a full name.

    Args:
        my_first_name (str): The first name.
        my_last_name (str): The last name.

    Returns:
        str: A string displaying the full name.
    """
    return f"My full name is {first_name(my_first_name)} {last_name(my_last_name)}"

print(fullname("Mahmud", "Amatullah"))



#Task 2 solution 1
attribute_list = ["first name", "last_name", "date of birth"]
converted_value = []
for attribute in attribute_list:
    if " " in attribute:
        converted_value.append(attribute.replace(" ", "_"))
    else:
        converted_value.append(attribute)
print(converted_value)

#Task 2 Solution 2
attribute_list = ["first name", "last_name", "date of birth"]
converted_value = []

for attribute in attribute_list:
    if " " in  attribute[0]:
        converted_value.append(attribute.replace(" ", "_"))
    else:
        converted_value.append(attribute)
print(converted_value)

#Task 3
names = ["Mayowa", "chizoba", "Chigozie"]
new_list = []

for name in names:
    if name[0].isupper() and name.endswith("a"): #Going in without an index is giving an empty list and that is because upper is a method
        new_list.append(name)
    elif name[0].isupper() and not name.endswith("a"):
        new_list.append(name[:-1] + "a")
print(new_list)


#Task 4
data_names = ["Wofai", "Zainab", "A4atullah"]
new = []

def error_spotter(): #are we going to have a the list or element as a parameter? can we have a list as a parameter?
    """
    Code for possible errors in the names generated listed in `data_names`.
    
    If a name contains any non-alphabetic character, it prints a message 
    identifying the name as having a foreign value.
    """
    for name in data_names:
        for letter in name:
            if not letter.isalpha():
                 print (f"The name {name} in the data received contains a foreign value")

   
            
error_spotter()


data_names = ["Wofai", "Zainab", "A4atullah", 3.5, "Ab99aa"]
errors= []

def error_spotter(data_names): #are we going to have a the list or element as a parameter? can we have a list as a parameter?
    """
    Code for possible errors in the names generated listed in `data_names`.
    
    If a name contains any non-alphabetic character, it prints a message 
    identifying the name as having a foreign value.
    """
    for name in data_names:
        for letter in name:
            if not letter.isalpha():
                print (f"The name {name} in the data received contains a foreign value")
           
error_spotter(data_names)