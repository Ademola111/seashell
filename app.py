from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
# from model.predict import load_image, run_example
from predict import classify
app = Flask(__name__)

"""homepahe"""
@app.route('/')
def home():
    return render_template('home.html')
    
"""upload pic section"""  
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method =="GET":
        return render_template('upload.html')

    if request.method == "POST":
        """getting form from server"""
        file = request.files['filename']
        file.save(os.path.join('static/uploads/',secure_filename(file.filename)))
        """filename should be full name with the .jpg extension"""
        """checking pic in the model"""
        res = classify(os.path.join('static/uploads/',file.filename))
        print(res)
        filename=os.path.join('static/uploads/',file.filename)
        return render_template('result.html', res=res,user_image=filename)


"""contact session"""
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    if request.method == 'POST':
        return redirect('/feedback')

# @app.route('/uploads/<filename>',methods=['GET'])
# def image(filename):
#     return render_template('result.html',user_image=os.path.join('uploads/',filename))
"""feedback"""
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')





if __name__ == '__main__':
    app.run(debug=True, port=8080)