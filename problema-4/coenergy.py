import csv
import pandas as pd
import matplotlib as plt

def LoadData():
    data = []
    try:
        data = pd.read_csv('fcoenergy.csv', delimiter=',', parse_dates=['Date'], index_col='Date')
    except Exception as e:
        print(e)
    finally:
        return data

def main():
    data = LoadData()
    print(data['0:00'])
    

if __name__ == '__main__':
    main()