# Seashell

## Seashell is a website application that is used to identify different seashell.

## With the integration of Machine Learning and some seashell dataset

## the webappis able to identify each object uploaded and state it's name.

Dataset is taken from this website.
[Dataset](https://www.nature.com/articles/s41597-019-0230-3)

To generate the CNN model -

```
cd model
pip install -r requirements.txt
python cnn_final_model.py
python predict.py
```

The process to prediction is shown in the model/predict.py\
Please generate the model first from cnn_final_model.py before using predict.py\
Note the image preprocessing done in predict before using the model for precition
