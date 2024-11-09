from flask import Flask, render_template, request  # Added request import
import pandas as pd
import os

app = Flask(__name__)
# Path to the Excel file
EXCEL_FILE = os.path.join('data', 'contacts.xlsx')

# Check if the Excel file exists, if not, create it with appropriate headers
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=['Name', 'Email', 'Phone', 'Address', 'Description'])
    df.to_excel(EXCEL_FILE, index=False)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']
    description = request.form['description']
    
    # Load the existing Excel file
    df = pd.read_excel(EXCEL_FILE)

    # Create a new entry
    new_entry = pd.DataFrame({
        'Name': [name],
        'Email': [email],
        'Phone': [phone],
        'Address': [address],
        'Description': [description]
    })

    # Append the new entry to the DataFrame and save it back to the Excel file
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False)

    return "Form submitted successfully!"



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

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/contribute')
def contribute():
    return render_template('contribute.html')


@app.route('/p1')
def p1():
    return render_template('program1.html')

@app.route('/p2')
def p2():
    return render_template('program2.html')

@app.route('/p3')
def p3():
    return render_template('program3.html')

@app.route('/p4')
def p4():
    return render_template('program4.html')

# Route for the Education program page
@app.route('/program1')
def program1():
    return render_template('program1.html')

# Route for the Children Welfare program page
@app.route('/program2')
def program2():
    return render_template('program2.html')

# Route for the Volunteering program page
@app.route('/program3')
def program3():
    return render_template('program3.html')

if __name__ == '__main__':
    app.run(debug=True)
