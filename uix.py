import flet as ft
import grapsi as gr
import os
import shutil

def main(page: ft.Page) -> ft.Page:
    if os.path.exists("Img"):
            shutil.rmtree("Img")
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

    def hype(e):
        hype_button.disabled = True
        page.update()
        i = gr.graps().main()
        img.src = None
        page.update()
        dir = f"Img/dots{i}.png"
        img.src = dir
        hype_button.disabled = False
        page.update()

    img = ft.Image(src= "Img/fig1.png", width= 500)
    hype_button = ft.ElevatedButton(text="Хайпануть", on_click=hype)
 
    page.add(img, hype_button)
    page.update()




ft.app(target = main)