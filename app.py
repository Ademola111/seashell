from flask import Flask, render_template, request
# from model.predict import load_image, run_example

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
        filename = request.form.get('filename')
        
        """checking pic in the model"""
        seashell = load_image(filename)
        res = run_example(seashell)
        print(res)
        return render_template('result.html')


"""contact session"""
@app.route('/contact')
def contact():
    return render_template('contact.html')

















































































































if __name__ == '__main__':
    app.run(debug=True, port=8080)