import numpy as np


# Задаем входные данные
X = np.array([[0.01860, 0.01810, 0.01810, 0.01820],
              [0.01790, 0.01840, 0.01840, 0.01880],
              [0.01590, 0.06590, 0.13410, 0.20610],
              [0.35620, 0.42960, 0.52760, 0.61610]])

# Задаем обучающие выходы
y = np.array([0.01800, 0.01790, 0.29100, 0.70170])

# Создаем класс персептрона
class Perceptron:
    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            for i in range(len(X)):
                output = self.predict(X[i])
                error = y[i] - output
                self.weights += learning_rate * error * X[i]
                self.bias += learning_rate * error

# Создаем экземпляр персептрона
input_size = X.shape[1]
perceptron = Perceptron(input_size)

# Обучаем персептрон
epochs = 10000
learning_rate = 0.04
perceptron.train(X, y, epochs, learning_rate)

def pred_by_len(len):
    next_m = 0
    prediction = [  0.01860, 0.01810, 0.01810, 0.01820, 0.01800,
                    0.01790, 0.01840, 0.01840, 0.01880, 0.01790,
                    0.01590, 0.06590, 0.13410, 0.20610, 0.29100,
                    0.35620, 0.42960, 0.52760, 0.61610, 0.70170,
                    0.78520, 0.83960, 0.85110, 0.85460, 
                    ]
    for i in range(len):
    # Пример предсказания количества пользователей
        test_data = np.array([[0.7852, 0.8396, 0.8511, 0.8546]])
        predicted_users = perceptron.predict(test_data)
        print("Предсказанное количество пользователей:", predicted_users)
        if i == 0:
            next_m = predicted_users
            prediction.append(predicted_users[0])
        else:
            new_test_data =[] 
            new_test_data.append(test_data[0][1])
            new_test_data.append(test_data[0][2])
            new_test_data.append(test_data[0][3])
            prediction.append(predicted_users[0])

    return next_m, prediction

pred_by_len(2)