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


# Пример предсказания количества пользователей
def predict(arr1):
    test_data = np.array(arr1)
    for i in range(3):
        temp = perceptron.predict(test_data)
        test_data = test_data[0][1:]
        test_data = np.append(test_data, temp)

    return temp



print("Предсказанное количество пользователей:", predict([[0.01800, 0.01790, 0.29100, 0.70170]]))