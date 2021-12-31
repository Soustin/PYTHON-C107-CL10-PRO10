import csv
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('attempts-level.csv')
student_df = df.loc[df['student_id']=="TRL_987"]

mean = student_df.groupby("level", as_index = False)["attempt"].mean()
print(mean)

Fig=go.Figure(go.Bar(
    x = mean,
    y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'],
    orientation = 'h'
))

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="levels", y="attempts")
        fig.show()

def getDataSource(data_path):
    level = []
    attempt = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            level.append(float(row["level"]))
            attempt.append(float(row["attempt"]))

    return {"x" : level, "y": attempt}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = mean

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

Fig.show()
setup()