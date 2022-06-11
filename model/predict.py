# make a prediction for a new image.
from os import listdir
from keras_preprocessing.image import load_img, img_to_array
from keras.models import load_model
import numpy as np
# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(200, 200))
	img=img_to_array(img)
	img=np.expand_dims(img,axis=0)
	# convert to array
	return img

# load an image and predict the class
def run_example():
	# load the image
	img = load_image('sample_image.jpg')
	# load model
	model = load_model('final_model.h5')
	# predict the class
	result = model.predict(img)
	print(result[0])
	return result


src_dir='train/'
labeldirs=[]
prev_name=None
for file in sorted(listdir(src_dir)):
    file_name=file.split('.')
    if file_name[0]!=prev_name:
        prev_name=file_name[0]
        labeldirs.append(file_name[0])
# entry point, run the example
result=run_example()
for i in range(len(result[0])):
	if result[0][i]==1:
		print("predicted sea shell is ",labeldirs[i])