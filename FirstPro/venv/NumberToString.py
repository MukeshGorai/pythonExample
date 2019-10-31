phone = input("phone: ")
digites_mapping={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
}
output = ""
for ch in phone:
    output += digites_mapping.get(ch, "!")+ " "
print(output)