# Seashell ML CLASSIFIER WEBSITE

### Seashell is a website application that is used to identify different seashell.

With the integration of Machine Learning and some seashell dataset the webapp will be able to identify each seashell uploaded and state it's name.\
Dataset is taken from this website.
[Dataset](https://www.nature.com/articles/s41597-019-0230-3)\

### Intructions for setting up in personal enviroment 
To generate the CNN model -

```
pip install -r requirements.txt
python cnn_final_model.py
```

The process to prediction is shown in the model/predict.py\
Please generate the model first from cnn_final_model.py before using predict.py\
Note the image preprocessing done in predict before using the model for prediction\
After this run the flask app from app.py

```
python app.py
```
### How our website works
First we have a landing page which explains what the purpose of the website is!

Next, we give the user the ability to upload any type of image (jpeg,png,etc) of a seashell, once the user has clicked submit, the name of the seashell will be returned! Simple!

### What are our goals for the webiste

We want to be able to help educate people of all ages and background on the hundereds of different types of seashells across the world. Seashells are a vital compoment in our eco system. For example, they are used as homes for sea snails, small fish, crabs and many different animals. Once the seashell has been discared, mother nature slowly grinds it down into tiny microscopic peices which eventually are the main material in beautiful sandy beaches! 
![]https://github.com/Ademola111/seashell/blob/main/gif1.gif
