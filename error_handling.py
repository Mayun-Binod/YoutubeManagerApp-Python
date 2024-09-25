file=open("youtube11.txt", "w")
try:
    file.write("Binod aur code\n")
    file.write("nextline")
finally:
    file.close()

# another way
with open ("youtube2.txt","w") as file:
    file.write("with keyword for file handling")