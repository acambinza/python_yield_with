def read_csv(file):
    with open(file, "r") as fileObj:
        print(fileObj.readlines())


read_csv("./data_source/blackfriday.csv")
