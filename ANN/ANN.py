import numpy as np

def loadCSV(filename):
    f = open("data.csv")
    data = np.loadtxt(f, delimiter = ',')
    X = data[:, 2:]
    y = data[:, 0:2]
    return X,y 

X, y = loadCSV("data.csv")

#N = X.shape[0]
X_train = X[:4000, 0:]
#yc_train = X[:N-N//5, 1]
#Uin_train = X[:N-N//5, 2]
U_train = y[:4000, 0:]
#Vc_train = y[:N-N//5, 1]

X_test = X[4000:, 0:]
U_test = y[4000:, 0:]

# print(Xc_train, yc_train, Uin_train, Uc_train, Vc_train)

#Developing model for Neural Network

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
from keras import regularizers

model = Sequential()
model.add(Dense(32, input_dim = 3, activation = 'relu', activity_regularizer=regularizers.l1(0.00001)))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(2, activation = 'tanh'))

model.compile(loss='mean_squared_error', optimizer= 'rmsprop', metrics = ['accuracy'])

model.fit(X_train,U_train, epochs = 100)

model.summary()
prediction = model.evaluate(X_test, U_test)

#u = model.predict(X_test)

#j = U_test - u

print(prediction)
#print(u)
#print(U_test)
#print(j)

model.save("ANN.h5")
print("Saved model to Disk")




