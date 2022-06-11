from flask import Flask, render_template, request
from model.predict import load_image, run_example

app = Flask(__name__)

"""homepahe"""
@app.route('/')
def home():
    return "index template will be rendered here"
    
"""upload pic section"""  
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method =="GET":
        return "upload template will be rendered here to see upload form"

    if request.method == "POST":
        """getting form from server"""
        filename = request.form.get('pic')
        
        """checking pic in the model"""
        seashell = load_image(filename)
        res = run_example(seashell)
        print(res)
        return f"upload template will be rendered here for {res}"


"""contact session"""
@app.route('/contact')
def contact():
    return "contact template will be rendered here "

















































































































if __name__ == '__main__':
    app.run(debug=True, port=8080)