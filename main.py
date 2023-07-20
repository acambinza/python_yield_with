def read_csv(file):
    with open(file, "r") as fileObj:
        return fileObj.readlines()


data_blackfriday = read_csv("./data_source/blackfriday.csv")

for item in data_blackfriday:
    print(item)


