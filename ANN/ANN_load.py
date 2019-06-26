import numpy as np
from keras.models import load_model
from keras import regularizers

# Load model
def loadCSV(filename):
    f = open("data.csv")
    data = np.loadtxt(f, delimiter = ',')
    X = data[:, 2:]
    y = data[:, 0:2]
    return X,y

from keras.regularizers import l1

model = load_model('ANN.h5')
model.summary()
   
X, y = loadCSV("data.csv")
X_train = X[:4000, 0:]
U_train = y[:4000, 0:]
X_test = X[4000:, 0:]
U_test = y[4000:, 0:]

prediction = model.evaluate(X_test, U_test)
print(prediction)

U_comp = model.predict(X_test)

for i in range(len(U_test)):
	abs_error = U_comp[i] - U_test[i]
	rel_error = abs_error/U_test[i]
	#print("U_comp = %s, U_test = %s" % (U_comp[i], U_test[i]))
	#print(rel_error)
	

import csv
with open('test.csv', 'w', newline='') as csvfile:
    testwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for j in range(len(U_test)):
        testwriter.writerow(U_comp[j])
    
