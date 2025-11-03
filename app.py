from flask import Flask, render_template_string, request, redirect

# Initialize the Flask app
app = Flask(__name__)

# A simple list to act as our "database"
# This list will reset if the server restarts, which is fine for this assignment.
patients = []

# This is the HTML for our web page.
# It includes a form to add patients and a list to display them.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Patient Management System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1, h2 { color: #333; }
        form { background: #f4f4f4; padding: 10px; border-radius: 5px; }
        input[type="text"] { padding: 5px; width: 200px; }
        input[type="submit"] { padding: 5px 10px; background: #007bff; color: white; border: none; }
        ul { list-style-type: none; padding: 0; }
        li { background: #eee; margin-top: 5px; padding: 10px; }
    </style>
</head>
<body>
    <h1>Patient Management System</h1>

    <h2>Add a New Patient</h2>
    <form action="/add" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="age">Age:</label>
        <input type="text" id="age" name="age" required>
        
        <input type="submit" value="Add Patient">
    </form>

    <h2>Current Patients</h2>
    <ul>
        {% for patient in patient_list %}
            <li>
                <strong>Name:</strong> {{ patient.name }} <br>
                <strong>Age:</strong> {{ patient.age }}
            </li>
        {% else %}
            <li>No patients registered yet.</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# This is the main page (route)
@app.route('/')
def index():
    # Render the HTML template, passing in our current list of patients
    return render_template_string(HTML_TEMPLATE, patient_list=patients)

# This route handles the form submission
@app.route('/add', methods=['POST'])
def add_patient():
    # Get the data from the form
    patient_name = request.form['name']
    patient_age = request.form['age']
    
    # Create a new patient dictionary
    new_patient = {
        "name": patient_name,
        "age": patient_age
    }
    
    # Add the new patient to our list
    patients.append(new_patient)
    
    # Redirect back to the main page to see the updated list
    return redirect('/')

# This makes the app run (Render will use this)
if __name__ == '__main__':
    app.run(debug=True)