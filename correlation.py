import numpy as np
import csv 
import pandas as pd
import plotly.express as px

def scatter_graph():
    df = pd.read_csv("student_data.csv")
    scatterPlot = px.scatter(df,x="Marks In Percentage",y="Days Present")
    scatterPlot.show()
    df1 = pd.read_csv("coffee_data.csv")
    scatterPlot1 = px.scatter(df1,x="Coffee in ml",y="sleep in hours")
    scatterPlot1.show()

def get_data_source(data_path1,data_path2):
    marks=[]
    present=[]
    coffee=[]
    hours=[]
    with open(data_path1) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            present.append(float(row["Days Present"]))
    with open(data_path2) as csv_file:
        csv_reader1=csv.DictReader(csv_file)
        for row in csv_reader1:
            coffee.append(float(row["Coffee in ml"]))
            hours.append(float(row["sleep in hours"]))

    return {"x1":marks, "y1":present,"x2":coffee, "y2":hours}
def find_correlation_coefficients(data_source):
    correlation=np.corrcoef(data_source["x1"],data_source["y1"])
    print(f"Correlation(Student Data) : {correlation[0,1]}")
    correlation1=np.corrcoef(data_source["x2"],data_source["y2"])
    print(f"Correlation(Coffee Data) : {correlation1[0,1]}")
def main():
    path1 = "student_data.csv"
    path2 = "coffee_data.csv"
    source = get_data_source(path1,path2)
    find_correlation_coefficients(source)
    scatter_graph()
main()
