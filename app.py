from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
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
        file.save(secure_filename(file.filename))
        """filename should be full name with the .jpg extension"""
        """checking pic in the model"""
        res = classify(file.filename)
        print(res)
        return render_template('result.html',res=res)


"""contact session"""
@app.route('/contact')
def contact():
    return render_template('contact.html')

















































































































if __name__ == '__main__':
    app.run(debug=True, port=8080)