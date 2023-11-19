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

    df = px.data.stocks()
    fig = px.line(data, x='Date', y="EK")

    return  fig


    
def mouyh():
    data = pd.read_csv("ha/Книга13.csv", sep=";", encoding="1251")
    print(data)
    
    a,b = Korrel.predict([[0.52760, 0.61610, 0.70170, 0.78520]])
    b = pd.Series(b)
    b =  b*10000
    print(b)

    df = px.data.stocks()
    fig = px.line(data, x='Date', y=b)

    return fig

def pie():
    data = pd.read_csv("ha/okved_eq.csv", sep=";", encoding="1251")
    print(data)
    
    # This dataframe has 244 lines, but 4 distinct values for `day`

    data_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(data, x='Name', y='Active', text_auto='.2s',
            title="Default: various text sizes, positions and angles")
    
    return fig

def line_2():
    data = pd.read_csv("ha/12cfd776f4e63d1b.csv", sep=";", encoding="1251")
    print(data)

    df = px.data.gapminder().query("continent=='Oceania'")
    print(df)

    fig = px.line(data, x="Даты", y="Пользователи", color='Типы')
    print(fig)
    return fig

line_2()