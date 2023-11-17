import numpy as np
import tensorflow as tf
from tensorflow import keras
import tkinter as tk
from tkinter import messagebox

# Задаем данные обучения
# Входные данные - возраст, доход, количество детей
# Выходные данные - категория клиента (0 - низкий, 1 - средний, 2 - высокий)
X = np.array([[25, 50000, 0],
              [40, 60000, 2],
              [35, 80000, 1],
              [50, 100000, 3]])
y = np.array([0, 1, 2, 2])

# Нормализуем входные данные
X = X / np.amax(X, axis=0)

# Создаем модель нейронной сети
model = keras.Sequential([
    keras.layers.Dense(4, input_shape=(3,), activation='sigmoid'),
    keras.layers.Dense(3, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Обучаем модель
model.fit(X, y, epochs=10000, verbose=0)

# Создаем графический интерфейс с помощью библиотеки tkinter
window = tk.Tk()
window.title("Предсказание категории клиента")

# Функция для обработки нажатия кнопки предсказания
def predict_category():
    age = float(entry_age.get())
    income = float(entry_income.get())
    children = float(entry_children.get())
    test_data = np.array([[age, income, children]])
    normalized_test_data = test_data / np.amax(X, axis=0)
    predicted_category = model.predict_classes(normalized_test_data)[0]
    class_predictictions = np.argmax(predicted_category, axis =- 1)
    messagebox.showinfo("Результат", f"Предсказанная категория клиента: {predicted_category}")

# Создаем элементы интерфейса
label_age = tk.Label(window, text="Возраст:")
label_age.pack()
entry_age = tk.Entry(window)
entry_age.pack()

label_income = tk.Label(window, text="Доход:")
label_income.pack()
entry_income = tk.Entry(window)
entry_income.pack()

label_children = tk.Label(window, text="Количество детей:")
label_children.pack()
entry_children = tk.Entry(window)
entry_children.pack()

button_predict = tk.Button(window, text="Предсказать", command=predict_category)
button_predict.pack()

# Запускаем главный цикл окна
window.mainloop()