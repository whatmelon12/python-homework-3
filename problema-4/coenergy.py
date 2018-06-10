import csv

def LoadData():
    data = []
    with open('fcoenergy.csv', 'r') as f:
        try:
            data = list(csv.reader(f, delimiter='\t'))
        except Exception as e:
            print(e)
        finally:
            f.close()
    return data