# tathastu_week_of_code
def duplicate(string):
    duplicateString=""
    for x in string:
        if x not in duplicateString:
            duplicateString+=x
    return duplicateString

string=input("enter the string")
print("string remove after the duplicates is",duplicate(string))
