import flet as ft
import grapsi as gr
import os
import shutil
import Korrel as kr
import test as ts
import plotly.express as px 
from flet.plotly_chart import PlotlyChart



def main(page: ft.Page) -> ft.Page:
    """
    Главная функция Интерфейса.
    
        Что должно выводить?:
            1) Гистограмма, показывающая количество пользователей по месяцам(Визуализация первого датасета(буквально))
            2) Закономерность возраста и использования эквайринга
            3) Закономерность вида деятельности и использования эквайринга
            4) Закономерность типа организации и использования эквайринга
            5) Закономерность наличия Устройств самообслуживания и использования эквайринга
            6) Закономерность Расчетно-Кассовое Обслуживание и использования эквайринга
            7) Закономерность наличия самоинкассации и использования эквайринга
    """
    
    graph_witgout_3 = ft.Container(content=ft.Row([PlotlyChart(ts.without_3_mounth(), expand= True)]), width= 600)
    graph_with_3 = ft.Container(content=ft.Row([PlotlyChart(ts.mouyh(), expand= True)]), width= 1)
    graph_pie = ft.Container(content=ft.Row([PlotlyChart(ts.pie(), expand= True)]), width= 600)

    # if os.path.exists("Img"):
    #     shutil.rmtree("Img")

    def hypen(e):
        if graph_with_3.width == 1:
            graph_with_3.width = 600
            graph_witgout_3.width = 1
            print(")")
        else:
            graph_with_3.width = 1
            graph_witgout_3.width = 600
            print("()")
        page.update()

    first, all = (kr.predict([[0.52760, 0.61610, 0.70170, 0.78520]]))   
    first= int(first*10000)
    a = 0

    ek_now =ft.Text(value=f"Пользуются эквайренгом сейчаc: {8546}")
    ek_next =ft.Text(value=f"Пользуются эквайренгом в следующем месяце: {first}")
    procent_life =ft.Text(value=f"Процент выживаемости клиентов: {a} %")

    button = ft.ElevatedButton(text="hype", on_click=hypen)


    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Row([
                        ek_now, ft.Container(width=150),procent_life
                    ]), 
                    ek_next,
                    ft.Row([graph_with_3, graph_witgout_3, graph_pie]),
                    button,
                    
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)




ft.app(target = main)