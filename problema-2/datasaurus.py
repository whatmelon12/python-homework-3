#Omar Mejia
#Rafael Segistan
import numpy as np
import csv
import matplotlib.pyplot as plt

class PlotPoints:
    def __init__(self, plots):
        self.plots = np.array(plots).astype(np.float)
        self.x, self.y = self.plots.T

    def getVariance(self):
        return np.std(self.plots)

    def getMean(self):
        return np.mean(self.plots)

    def getCorrelation(self):
        return np.correlate(self.x, self.y)
    
    def graphScatter(self):
        plt.scatter(self.x, self.y)
        plt.show()
    
    def graphPlot(self):
        plt.plot(self.x, self.y)
        plt.show()

def LoadData():
    data = []
    with open('DatasaurusDozen-wide.tsv', 'r') as f:
        try:
            data = list(csv.reader(f, delimiter='\t'))
        except Exception as e:
            print(e)
        finally:
            f.close()
    return data
    
def GetDataGroup(data, dataColumn):
    baseColumnIndex = data[0].index(dataColumn)
    dataList = [[x[baseColumnIndex], x[baseColumnIndex + 1]] for x in data]
    return dataList[2:]

def GetDataHeader(data):
    return set(data[0])

def MapPlotPoints(data):
    headers =  GetDataHeader(data)
    return {header: PlotPoints(GetDataGroup(data, header)) for header in headers}

def CreatePlotGraph(headers, dictionary):
    fig = plt.figure()

    for i in range(len(headers)):
        item = dictionary.get(headers[i])
        fig.add_subplot(3, 4, i + 1).plot(item.x, item.y)
    plt.show()

def main():
    data = LoadData()
    plotDictionary = MapPlotPoints(data)
    notDinoList = [x for x in plotDictionary.keys() if x != 'dino']
    CreatePlotGraph(notDinoList, plotDictionary)
    plotDictionary.get('dino').graphScatter()

if __name__ == '__main__':
    main()