import numpy as np
from keras.models import Sequential
from keras.layers.core import Activation, Dense

# the four different states of the XOR gate
training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")

# the four expected results in the same order
target_data = np.array([[0],[1],[1],[0]], "float32")

model = Sequential()
model.add(Dense(25, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])

h = model.fit(training_data, target_data, epochs=500, verbose=1)

model.evaluate(training_data,target_data)

print(h.history.keys())
print("Min Loss: ",h.history["loss"][-1])
print(model.predict(training_data).round())
