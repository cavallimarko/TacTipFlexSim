import numpy as np
import pandas
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import os
from keras.preprocessing import image
import matplotlib.pyplot as plt  
import glob
from keras.callbacks import ModelCheckpoint


datasetmap="Dataset_4_height/"
source = datasetmap+"train"
dest = datasetmap+"validation"
img_width, img_height = 640, 480
target_img_width,target_img_height = 320,240

#filelist = glob.glob('Dataset_4_height/train/*.png')
dots=False
sim=True
modelName=""

if(sim):
    if dots:
        filelist = glob.glob('DotsSim/*.png')
        modelName = "unrealDotsModel.h5"
    else:
        filelist = glob.glob('DatasetSim/*.png')
        modelName="unrealModel.h5"
else:
    if dots:

        filelist = glob.glob('DotsReal/*.png')
        modelName = "realDotsModel.h5"
    else:
        filelist = glob.glob('DatasetReal/FlatR100V0/*.png')
        modelName="realModel.h5"


X = np.array([(np.array(image.load_img(fname,grayscale=True,target_size=(target_img_height,target_img_width)))/255)[..., np.newaxis] for fname in filelist])
#print(float(str(filelist[0]).split("\\")[1].split('_')[2][:3]))

Y = np.array([float(str(file).split("\\")[1].split('_')[3][:-4]) for file in filelist])

input_shape = (target_img_height, target_img_width,1)

    
# define base model
def baseline_model():
    # create model
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.1))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(1))
    model.add(Activation('relu'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mse', 'mae', 'mape', 'cosine'])
    return model
# fix random seed for reproducibility
seed = 7
np.random.seed(seed)
# evaluate model with standardized dataset
estimator = KerasRegressor(build_fn=baseline_model, epochs=30, batch_size=5, verbose=1)
#kfold = KFold(n_splits=10, random_state=seed)
#results = cross_val_score(estimator, X, Y, cv=kfold)
#print("Results: %.2f (%.2f) MSE" % (abs(results.mean()), results.std()))

chk = ModelCheckpoint(modelName, monitor='val_loss', save_best_only=False)
callbacks_list = [chk]
history=estimator.fit(X,Y, callbacks=callbacks_list)
plt.figure(1)  

plt.subplot(311)  
plt.plot(history.history['mse'])

plt.title('mean_squared_error') 
plt.ylabel('error')  
plt.xlabel('epoch')  
plt.legend(['train', 'test'], loc='upper left')  
plt.subplot(312)  
plt.plot(history.history['mae'])

plt.title('mean_absolute_error') 
plt.ylabel('error')  
plt.xlabel('epoch')  
plt.legend(['train', 'test'], loc='upper left')  
plt.subplot(313)  
plt.plot(history.history['mape'])

plt.title('mean_absolute_percentage_errorr')
plt.ylabel('error')  
plt.xlabel('epoch')  
plt.legend(['train', 'test'], loc='upper left')  

plt.tight_layout()
plt.show()
plt.savefig('mse2.png') 

   
