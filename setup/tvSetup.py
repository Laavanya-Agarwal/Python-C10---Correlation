import plotly.express as px
import csv
import numpy as np

def plotFigure (path):
    with open(path) as csv_file:
        read = csv.DictReader(csv_file)
        fig = px.scatter(read, x="Size of TV", y="time in a week")
        fig.show()

def getDataSource (path):
    size = []
    hours = []
    with open(path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size.append(float(row['Size of TV']))
            hours.append(float(row['time in a week']))
        return{"x": size, "y": hours}

def findCorrelation (source):
    correlation = np.corrcoef(source["x"], source["y"])
    print("Correlation between Size vs Time in a week:  \n --> ",correlation[0,1])

def setup():
    path = './data/tv.csv'
    source = getDataSource(path)
    findCorrelation(source)
    plotFigure(path)

setup()