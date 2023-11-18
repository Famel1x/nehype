import plotly.express as px
import pandas as pd
import os
import shutil
import Korrel

if not os.path.exists("Img"):
            os.mkdir("Img")


def without_3_mounth():
    data = pd.read_csv("ha/Книга1_without_3.csv", sep=";", encoding="1251")
    print(data)
    a,b = Korrel.pred_by_len(3)
    print(b)

    df = px.data.stocks()
    fig = px.line(data, x='Date', y="EK")


    dir = f"Img/test_without.png"
    fig.write_image(dir)
    print("succes")

def mouyh():
    data = pd.read_csv("ha/Книга13.csv", sep=";", encoding="1251")
    print(data)
    a,b = Korrel.pred_by_len(3)
    print(b)

    df = px.data.stocks()
    fig = px.line(data, x='Date', y=b)


    dir = f"Img/test_with.png"
    fig.write_image(dir)
    print("succes")


mouyh()
