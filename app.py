from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name="Jaggu", age=16)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')



if __name__ == '__main__':
    app.run(debug=True)


