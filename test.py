import csv
def test(str):
    f= str
    with open(f) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            print(row["Student Name"], row["Grade"])

if __name__ == "__main__":
    test("ClassA.csv")
    test("ClassB.csv")
    test("ClassC.csv")
    test("ClassD.csv")
