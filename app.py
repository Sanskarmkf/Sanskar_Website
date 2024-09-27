from flask import Flask, render_template, url_for

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the contact page
@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/p1')
def p1():
    return render_template('program1.html')

@app.route('/p2')
def p2():
    return render_template('program2.html')

@app.route('/p3')
def p3():
    return render_template('program3.html')

if __name__ == '__main__':
    app.run(debug=True)
