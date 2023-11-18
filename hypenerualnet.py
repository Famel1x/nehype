import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

training_inputs = np.array([[   
                                [0.01860, 0.01810, 0.01810, 0.01820], 
                                [0.01790, 0.01840, 0.01840, 0.01880], 
                                [0.01590, 0.06590, 0.13410, 0.20610], 
                                [0.35620, 0.42960, 0.52760, 0.61610], 
                                
                        ]])

training_outputs = np.array([[0.01800, 0.01790,0.29100, 0.70170]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((4, 1)) - 1

print("Случайные веса: ")
print(synaptic_weights)

# Метод обратного распространени
for i in range(10000):
    input_layer = training_inputs

    outputs = sigmoid(np.dot(input_layer, synaptic_weights))
    if i == 1:
        print(outputs)
    err = training_outputs - outputs     

    adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
    synaptic_weights += adjustments

print("Веса после обучения: ")
print(synaptic_weights)

print("Результат после обучения: ")
for out in outputs:
    print(round(float(out) * 10))