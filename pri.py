import numpy as np

# Задаем входные данные
X = np.array([[0.01860, 0.00010, 0.00020, 0.00030],
              [0.00010, 0.00090, 0.00030, 0.00070],
              [0.00020, 0.05120, 0.06940, 0.07360],
              [0.06780, 0.07730, 0.10140, 0.09320]])

# Задаем обучающие выходы
y = np.array([0.00010, 0.00010, 0.08650, 0.03260])

# Создаем класс персептрона
class Perceptron:
    def __init__(self, input_size):
        # self.weights = np.load('weights.npy', allow_pickle= True)
        # self.bias = np.load('bias.npy', allow_pickle= False)
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
# epochs = 20000
# learning_rate = 0.0315
# perceptron.train(X, y, epochs, learning_rate) 


# Пример предсказания количества пользователей
def predict(arr1):
    predictions = [ 0.01860, 0.00010, 0.00020, 0.00030,
                    0.00010, 0.00090, 0.00030, 0.00070,
                    0.00020, 0.05120, 0.06940, 0.07360,
                    0.06780, 0.07730, 0.10140, 0.09320 ]

    

    test_data = np.array(arr1)
    for i in range(3):
        if i == 0:
            temp = perceptron.predict(test_data)
            test_data = test_data[0][1:]
            test_data = np.append(test_data, temp)
            firstmonth = temp[0]
            predictions.append(temp[0])
        else:
            temp = perceptron.predict(test_data)
            test_data = test_data[1:]
            test_data = np.append(test_data, temp)
            predictions.append(temp)
    return firstmonth, predictions

print("Предсказанное количество пользователей:", predict([[0.08830, 0.05680, 0.02080, 0.01430,]]))

 