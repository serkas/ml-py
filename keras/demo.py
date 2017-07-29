from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

X, X_test, y, y_test = train_test_split(iris['data'], iris['target'], random_state=2)

from keras.utils.np_utils import to_categorical
y_binary = to_categorical(y, 4)
y_test_binary = to_categorical(y_test, 4)

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

model = Sequential()


model.add(Dense(128, activation='relu', input_dim=4))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])


model.fit(X, y_binary, epochs=20, batch_size=128)
score = model.evaluate(X_test, y_test_binary, batch_size=128)

print(score)

print(y_test_binary)