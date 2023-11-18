import flet as ft
import grapsi as gr
import os
import shutil
import Korrel as kr

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

    # if os.path.exists("Img"):
    #     shutil.rmtree("Img")

    a = int((kr.pred_by_len(1)[0])*10000)   
    ek_now =ft.Text(value=f"Пользуются эквайренгом сейчаc: {8546}")
    ek_next =ft.Text(value=f"Пользуются эквайренгом в следующем месяце: {a}")
    procent_life =ft.Text(value=f"Процент выживаемости клиентов: {a} %")

    img_without = ft.Image(src= "Img/test_without.png", width=400)


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
                    img_without
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