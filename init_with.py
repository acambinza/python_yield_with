# With Structure - Open and close the file your self

# without "with structure"

file = open("./data_source/input.txt", "w")
file.write("Texto de exemplo")
file.close()


# with "with structure"

with open("./data_source/input_with.txt", "w") as file_with:
    file_with.write("outro texto de teste usando o with")


