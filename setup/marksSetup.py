import plotly.express as px
import csv
import numpy as np

def plotFigure (path):
    with open(path) as csv_file:
        read = csv.DictReader(csv_file)
        fig = px.scatter(read, x="Marks In Percentage", y="Days Present")
        fig.show()

def getDataSource (path):
    marks = []
    attendance = []
    with open(path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row['Marks In Percentage']))
            attendance.append(float(row['Days Present']))
        return{"x": marks, "y": attendance}

def findCorrelation (source):
    correlation = np.corrcoef(source["x"], source["y"])
    print("Correlation between Marks vs Attendance:  \n --> ",correlation[0,1])

def setup():
    path = './data/marks.csv'
    source = getDataSource(path)
    findCorrelation(source)
    plotFigure(path)

setup()