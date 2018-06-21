import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def LoadData():
    df = []
    try:
        df = pd.read_csv('fcoenergy.csv', delimiter=',',
                         parse_dates=['Date'], index_col='Date')
    except Exception as e:
        print(e)
    finally:
        return df


def main():
    df = LoadData()
# print(dataframe)
    # # Part a
    s1 = [float(x) for x in df['2010-10'].Total.values]
    s2 = [float(x) for x in df['2011-10'].Total.values]

    ind = pd.Series(np.arange(32)[1:])
    oct2010 = pd.Series(s1)
    oct2011 = pd.Series(s2)

    df2 = pd.concat([ind, oct2010, oct2011], axis=1)
    df2.columns = ['Day', 'Oct2010', 'Oct2011']
    df2.set_index('Day', inplace=True, drop=True)
    df2.plot(grid=True)

    # Part b
    setb = df['2011-10'].loc[:, '0:00':'23:30']
    setb.plot(kind='hist', stacked=True)

    plt.show()


if __name__ == '__main__':
    main()
