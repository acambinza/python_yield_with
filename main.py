data_source = "./data_source/blackfriday.csv"


def read_csv(file):
    with open(file, "r") as fileObj:
        return fileObj.readlines()


def read_csv_yield(file):
    for row in open(file, "r"):
        yield row


def read_csv_yield_two(file):
    yield from open(file, "r")

# example one
#data_blackfriday = read_csv(data_source)
#for item in data_blackfriday:
#    print(item)


# example two
data_blackfriday_yield = read_csv_yield(data_source)

for item in data_blackfriday_yield:
    print(item)

data_blackfriday_yield_two = read_csv_yield_two(data_source)

for item_two in data_blackfriday_yield_two:
    print(item_two)