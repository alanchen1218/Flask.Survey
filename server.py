from flask import Flask , render_template, redirect, request
app = Flask(__name__)  

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def next():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    # print(name, location, language, comment)

    return render_template('results.html', name=name, location=location, language=language, comment=comment)

if __name__=="__main__":
    app.run(debug=True) 