import csv
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


def LoadData(file):
    df = []
    try:
        df = pd.read_csv(file, delimiter=',')
    except Exception as e:
        print(e)
    finally:
        return df

def main():
    dfMariano = LoadData('Mariano.csv')
    dfYankees = LoadData('Yankees.csv')

    #Año con mas juegos salvados.
    print('Año donde Mariano termino mas juegos: ' + str(dfMariano.loc[dfMariano['GF'].idxmax()]['Year']))

    # #Grafico de barras de salvaciones por año
    # dfMariano.plot('Year', 'SV', 'bar')
    # plt.show()

    # #Boxplot de lanzamiento promedio de los yankees
    # dfYankees[dfYankees['Year'] >= dfMariano['Year'].min()].boxplot('PAge')
    # plt.show()

    #Merge de asistencia al yankee y los premios de mariano

    # #Asistencia de al yankee por año y la ERA de mariano por año
    # fig = plt.figure()
    # fig.add_subplot(1, 2, 1)
    # dfYankees[dfYankees['Year'] >= dfMariano['Year'].min()].boxplot('Attendance')
    # fig.add_subplot(1, 2, 2)
    # dfMariano.boxplot('ERA')
    # plt.show()


if __name__ == '__main__':
    main()