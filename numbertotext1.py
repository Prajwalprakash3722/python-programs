# this program is to convert any (0-9) numbers to text
phone_number = input("enter your phone number: ")
mapping = {
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine",
}
output = ""
for num in phone_number:
    output += (mapping.get(num, "!")) + " "
print(output)
