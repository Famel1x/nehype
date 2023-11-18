import plotly.express as px
import pandas as pd
import numpy as np
import os
import time

dots_iter = 0
gist_iter = 0

hype = pd.read_csv("case/dataset/1._.csv", sep=";",encoding="1251")
print(hype)

class graps:
    def __init__(self) -> None:
        if not os.path.exists("Img"):
            os.mkdir("Img")

        self.Iter = 0
        self.x_data = np.random.random(50)
        self.y_data = np.random.random(50)

    def chng_parametr_dots_iter(self):
        global dots_iter
        dots_iter +=1
        return dots_iter
    
    def chng_parametr_gist_iter(self):
        global gist_iter
        gist_iter +=1
        return gist_iter

    def graps_dots(self, X, Y) -> int:
        global dots_iter
        fig = px.scatter(x=X, y= Y)
        dir = f"Img/dots{dots_iter}.png"
        fig.write_image(dir)
        print("succes")
        dots_iter = self.chng_parametr_dots_iter()
        return dots_iter-1
    
    def main(self):
        global a
        print(self.x_data)
        fig = px.scatter(x=self.x_data, y= self.y_data)
        dir = f"Img/fig{a}.png"
        fig.write_image(dir)
        print("succes")
        a = self.chng_parametr()
        return a-1
    
    def graps_gist(self):
        global gist_iter
        global hype
        df = px.data.gapminder().query("country == 'Canada'")
        fig = px.bar(df, x='continent', y='iso_alpha',
            hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
            labels={'pop':'population of Canada'}, height=400)
        dir = f"Img/graphs{gist_iter}.png"
        fig.write_image(dir)
        print("succes")
        gist_iter = self.chng_parametr_gist_iter()
        return gist_iter-1
        

print("creating table")
fig = px.line(hype, x="РКО", y=hype.columns, title='Time Series with Range Slider and Selectors')
print("saving")
fig.write_image("Img/timeLine.png")
print("saved")
print("succes")

