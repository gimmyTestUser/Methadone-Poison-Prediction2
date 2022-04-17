import pandas as pd
import pickle 
import numpy as np
with open('model_pkl' , 'rb') as f:
    model = pickle.load(f)



def predict_fields(myArray):
    values = np.array(myArray)
    new = np.expand_dims(values,axis=0)
    myVal =  model.predict(new)
    print(myVal)
    return myVal
