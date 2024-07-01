from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.current_topic = None  # Initialize a variable to keep track of conversation context

# Define your functions here (handle_user_input, handle_main_menu, etc.)

# Example function (add all other functions you have):
def introduce():
    return (
        "Hello! I am Thor 🦸‍♂️, your university assistant chatbot.<br>"
        "I can help you with the following:<br>"
        "1. Enrollment and Registration 📋<br>"
        "2. Course Details 📚<br>"
        "3. Financial Information 💰<br>"
        "4. Campus Resources 🏫<br>"
        "5. Contact Information 📞<br>"
        "6. Exit 🚪<br>"
        "Please enter the number corresponding to your query:"
    )

@app.route('/')
def index():
    app.current_topic = None
    return render_template('index.html', intro=introduce())

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = handle_user_input(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
