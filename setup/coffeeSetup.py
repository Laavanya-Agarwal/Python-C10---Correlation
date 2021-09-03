import plotly.express as px
import csv
import numpy as np

def plotFigure (path):
    with open(path) as csv_file:
        read = csv.DictReader(csv_file)
        fig = px.scatter(read, x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource (path):
    amountCoffee = []
    hoursSleep = []
    with open(path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            amountCoffee.append(float(row['Coffee in ml']))
            hoursSleep.append(float(row['sleep in hours']))
        return{"x": amountCoffee, "y": hoursSleep}

def findCorrelation (source):
    correlation = np.corrcoef(source["x"], source["y"])
    print("Correlation between Temperature vs Ice Cream Sales:  \n --> ",correlation[0,1])

def setup():
    path = './data/coffee.csv'
    source = getDataSource(path)
    findCorrelation(source)
    plotFigure(path)

setup()