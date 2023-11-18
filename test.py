import plotly.express as px
import pandas as pd

data = pd.read_csv("ha/Книга1.csv", sep=";", encoding="1251")
print(data)
df = px.data.stocks()
fig = px.line(data, x='Date', y="PCO")
# print(df)



dir = f"Img/test.png"
fig.write_image(dir)
print("succes")