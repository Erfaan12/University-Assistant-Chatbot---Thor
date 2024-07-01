from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

app = Flask(__name__)

def handle_user_input(user_input):
    response = ""
    if app.current_topic is None:
        response = handle_main_menu(user_input)
    else:
        response = handle_sub_menu(user_input)
    return response

def handle_main_menu(user_input):
    if user_input == '1':
        app.current_topic = 'enrollment'
        return enrollment_and_registration()
    elif user_input == '2':
        app.current_topic = 'course'
        return course_details()
    elif user_input == '3':
        app.current_topic = 'financial'
        return financial_information()
    elif user_input == '4':
        app.current_topic = 'resources'
        return campus_resources()
    elif user_input == '5':
        app.current_topic = 'contact'
        return contact_information()
    elif user_input == '6':
        return "Goodbye! Have a great day! 👋"
    else:
        return "Invalid choice. Please try again. ❌"

def handle_sub_menu(user_input):
    if app.current_topic == 'enrollment':
        return handle_enrollment_sub_menu(user_input)
    elif app.current_topic == 'course':
        return handle_course_sub_menu(user_input)
    elif app.current_topic == 'financial':
        return handle_financial_sub_menu(user_input)
    elif app.current_topic == 'resources':
        return handle_resources_sub_menu(user_input)
    elif app.current_topic == 'contact':
        return handle_contact_sub_menu(user_input)

def enrollment_and_registration():
    return (
        "Enrollment and Registration Information 📋:<br>"
        "1. How to enroll? 📝<br>"
        "2. Required documents 📑<br>"
        "3. Registration fee details 💵<br>"
        "4. Go back to main menu 🔙"
    )

def handle_enrollment_sub_menu(user_input):
    if user_input == '1':
        return (
            "To enroll, visit the university's enrollment page: "
            "<a href='https://www.stcloudstate.edu/apply/default.aspx' target='_blank'>https://www.stcloudstate.edu/apply/default.aspx</a><br>"
            "Complete the online registration form. 📝"
        )
    elif user_input == '2':
        return "Required documents include your ID, transcripts, and proof of residency. 📑"
    elif user_input == '3':
        return (
            "The registration fee details can be found here: "
            "<a href=' https://www.stcloudstate.edu/businessservices/student-services/cost-of-attendance.aspx' target='_blank'> https://www.stcloudstate.edu/businessservices/student-services/cost-of-attendance.aspx</a> 💵"
        )
    elif user_input == '4':
        app.current_topic = None
        return introduce()
    else:
        return "Invalid choice. Please try again. ❌"

def course_details():
    return (
        "Course Details Information 📚:<br>"
        "1. Where to find course catalog? 📖<br>"
        "2. How to select courses? 🗂️<br>"
        "3. Information on course orientation? 🧭<br>"
        "4. Go back to main menu 🔙"
    )

def handle_course_sub_menu(user_input):
    if user_input == '1':
        return (
            "You can find the course catalog here: "
            "<a href=' https://www.stcloudstate.edu/academics/default.aspx' target='_blank'> https://www.stcloudstate.edu/academics/default.aspx</a> 📖"
        )
    elif user_input == '2':
        return "Contact your academic advisor to help you select courses. 🗂️"
    elif user_input == '3':
        return (
            "Course orientation sessions are announced here: "
            "<a href='https://www.stcloudstate.edu/advising/orientation/default.aspx' target='_blank'>https://www.stcloudstate.edu/advising/orientation/default.aspx</a> 🧭"
        )
    elif user_input == '4':
        app.current_topic = None
        return introduce()
    else:
        return "Invalid choice. Please try again. ❌"

def financial_information():
    return (
        "Financial Information 💰:<br>"
        "1. How to apply for financial aid? 📑<br>"
        "2. Information on scholarships and grants 🎓<br>"
        "3. Tuition fees and payment options 💵<br>"
        "4. Go back to main menu 🔙"
    )

def handle_financial_sub_menu(user_input):
    if user_input == '1':
        return (
            "Visit the financial aid office: "
            "<a href='https://www.stcloudstate.edu/financialaid/default.aspx' target='_blank'>https://www.stcloudstate.edu/financialaid/default.aspx</a><br>"
            "Fill out the required forms available on their website. 📑"
        )
    elif user_input == '2':
        return (
            "Check the scholarships and grants information here: "
            "<a href='https://www.stcloudstate.edu/financialaid/types-of-aid/default.aspx' target='_blank'>https://www.stcloudstate.edu/financialaid/types-of-aid/default.aspx</a> 🎓"
        )
    elif user_input == '3':
        return (
            "Tuition fees and payment options are detailed here: "
            "<a href='https://www.stcloudstate.edu/businessservices/default.aspx' target='_blank'>https://www.stcloudstate.edu/businessservices/default.aspx</a> 💵"
        )
    elif user_input == '4':
        app.current_topic = None
        return introduce()
    else:
        return "Invalid choice. Please try again. ❌"

def campus_resources():
    return (
        "Campus Resources Information 🏫:<br>"
        "1. How to access library resources? 📚<br>"
        "2. Information on student health center 🏥<br>"
        "3. Career services and job placements 🧑‍💼<br>"
        "4. Go back to main menu 🔙"
    )

def handle_resources_sub_menu(user_input):
    if user_input == '1':
        return (
            "Access library resources online through the university library portal: "
            "<a href='https://www.stcloudstate.edu/library/' target='_blank'>https://www.stcloudstate.edu/library/</a> 📚"
        )
    elif user_input == '2':
        return (
            "Visit the student health center or check their services here: "
            "<a href='https://www.stcloudstate.edu/medicalclinic/default.aspx' target='_blank'>https://www.stcloudstate.edu/medicalclinic/default.aspx</a> 🏥"
        )
    elif user_input == '3':
        return (
            "Career services offer job placement assistance. Visit their office or website for more info: "
            "<a href='https://www.stcloudstate.edu/careercenter/' target='_blank'>https://www.stcloudstate.edu/careercenter/</a> 🧑‍💼"
        )
    elif user_input == '4':
        app.current_topic = None
        return introduce()
    else:
        return "Invalid choice. Please try again. ❌"

def contact_information():
    return (
        "Contact Information 📞:<br>"
        "1. Admissions Office contact 📧<br>"
        "2. Registrar's Office contact 📧<br>"
        "3. Financial Aid Office contact 📧<br>"
        "4. Campus Resources contact 📧<br>"
        "5. Go back to main menu 🔙"
    )

def handle_contact_sub_menu(user_input):
    if user_input == '1':
        return "Admissions Office: scsu4u@stcloudstate.edu 📧"
    elif user_input == '2':
        return "Registrar's Office: registrar@stcloudstate.edu 📧"
    elif user_input == '3':
        return "Financial Aid Office: FinancialAid@StCloudState.Edu 📧"
    elif user_input == '4':
        return "Campus Resources: https://www.stcloudstate.edu/deanofstudents/campus-resources/default.aspx 📧"
    elif user_input == '5':
        app.current_topic = None
        return introduce()
    else:
        return "Invalid choice. Please try again. ❌"

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
