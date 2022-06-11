import sys
from matplotlib import pyplot
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator

def define_model():
    model=Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(200, 200, 3)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.2))
    model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.2))
    model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dropout(0.5))
    model.add(Dense(8, activation='softmax'))
    #output layer must contain the same number of neurons as the number of classes
    #8 here since 8 categories are present
	# compile model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def summarize_diagnostics(history):
	# plot loss
	pyplot.subplot(211)
	pyplot.title('Cross Entropy Loss')
	pyplot.plot(history.history['loss'], color='blue', label='train')
	pyplot.plot(history.history['val_loss'], color='orange', label='test')
	# plot accuracy
	pyplot.subplot(212)
	pyplot.title('Classification Accuracy')
	pyplot.plot(history.history['accuracy'], color='blue', label='train')
	pyplot.plot(history.history['val_accuracy'], color='orange', label='test')
	# save plot to file
	filename = sys.argv[0].split('/')[-1]
	pyplot.savefig(filename + '_plot.png')
	pyplot.close()

def run_test_harness():
    model=define_model()
    datagen=ImageDataGenerator(rescale=1.0/255.0)
    train_it=datagen.flow_from_directory('dataset/train',class_mode='categorical',batch_size=32,target_size=(200,200))
    test_it=datagen.flow_from_directory('dataset/test',class_mode='categorical',batch_size=32,target_size=(200,200))
    history=model.fit(train_it,steps_per_epoch=len(train_it), validation_data=test_it,validation_steps=len(test_it),epochs=8)
    _,acc=model.evaluate(test_it,steps=len(test_it))
    print('> %.3f' % (acc * 100.0))
    #learning curve
    summarize_diagnostics(history)

run_test_harness()