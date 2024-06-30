import tkinter as tk
from tkinter import scrolledtext

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("University Assistant Chatbot - Thor")
        
        self.chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state='disabled')
        self.chat_window.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
        
        self.user_input = tk.Entry(root, width=60)
        self.user_input.grid(column=0, row=1, padx=10, pady=10)
        self.user_input.bind("<Return>", self.handle_enter_key)
        
        self.send_button = tk.Button(root, text="Send", command=self.handle_user_input)
        self.send_button.grid(column=1, row=1, padx=10, pady=10)
        
        self.introduce()
        self.current_topic = None

    def introduce(self):
        self.append_to_chat_window("Hello! I am Thor, your university assistant chatbot.")
        self.append_to_chat_window("I can help you with the following:")
        self.append_to_chat_window("1. Enrollment and Registration")
        self.append_to_chat_window("2. Course Details")
        self.append_to_chat_window("3. Financial Information")
        self.append_to_chat_window("4. Campus Resources")
        self.append_to_chat_window("5. Contact Information")
        self.append_to_chat_window("6. Exit")
        self.append_to_chat_window("Please enter the number corresponding to your query:")

    def append_to_chat_window(self, message):
        self.chat_window.config(state='normal')
        self.chat_window.insert(tk.END, message + '\n')
        self.chat_window.config(state='disabled')
        self.chat_window.see(tk.END)

    def handle_enter_key(self, event):
        self.handle_user_input()

    def handle_user_input(self):
        user_input = self.user_input.get()
        if not user_input:
            return
        self.append_to_chat_window(f"You: {user_input}")
        self.user_input.delete(0, tk.END)
        
        if self.current_topic is None:
            self.handle_main_menu(user_input)
        else:
            self.handle_sub_menu(user_input)

    def handle_main_menu(self, user_input):
        if user_input == '1':
            self.current_topic = 'enrollment'
            self.enrollment_and_registration()
        elif user_input == '2':
            self.current_topic = 'course'
            self.course_details()
        elif user_input == '3':
            self.current_topic = 'financial'
            self.financial_information()
        elif user_input == '4':
            self.current_topic = 'resources'
            self.campus_resources()
        elif user_input == '5':
            self.current_topic = 'contact'
            self.contact_information()
        elif user_input == '6':
            self.append_to_chat_window("Goodbye! Have a great day!")
            self.root.quit()
        else:
            self.append_to_chat_window("Invalid choice. Please try again.")

    def handle_sub_menu(self, user_input):
        if self.current_topic == 'enrollment':
            self.handle_enrollment_sub_menu(user_input)
        elif self.current_topic == 'course':
            self.handle_course_sub_menu(user_input)
        elif self.current_topic == 'financial':
            self.handle_financial_sub_menu(user_input)
        elif self.current_topic == 'resources':
            self.handle_resources_sub_menu(user_input)
        elif self.current_topic == 'contact':
            self.handle_contact_sub_menu(user_input)

    def enrollment_and_registration(self):
        self.append_to_chat_window("Enrollment and Registration Information:")
        self.append_to_chat_window("1. How to enroll?")
        self.append_to_chat_window("2. Required documents?")
        self.append_to_chat_window("3. Registration fee details?")
        self.append_to_chat_window("4. Go back to main menu")

    def handle_enrollment_sub_menu(self, user_input):
        if user_input == '1':
            self.append_to_chat_window("To enroll, visit the university's enrollment page: https://www.university.edu/enroll")
            self.append_to_chat_window("Complete the online registration form.")
        elif user_input == '2':
            self.append_to_chat_window("Required documents include your ID, transcripts, and proof of residency.")
        elif user_input == '3':
            self.append_to_chat_window("The registration fee details can be found here: https://www.university.edu/fees")
        elif user_input == '4':
            self.current_topic = None
            self.introduce()
        else:
            self.append_to_chat_window("Invalid choice. Please try again.")

    def course_details(self):
        self.append_to_chat_window("Course Details Information:")
        self.append_to_chat_window("1. Where to find course catalog?")
        self.append_to_chat_window("2. How to select courses?")
        self.append_to_chat_window("3. Information on course orientation?")
        self.append_to_chat_window("4. Go back to main menu")

    def handle_course_sub_menu(self, user_input):
        if user_input == '1':
            self.append_to_chat_window("You can find the course catalog here: https://www.university.edu/course-catalog")
        elif user_input == '2':
            self.append_to_chat_window("Contact your academic advisor to help you select courses.")
        elif user_input == '3':
            self.append_to_chat_window("Course orientation sessions are announced here: https://www.university.edu/events")
        elif user_input == '4':
            self.current_topic = None
            self.introduce()
        else:
            self.append_to_chat_window("Invalid choice. Please try again.")

    def financial_information(self):
        self.append_to_chat_window("Financial Information:")
        self.append_to_chat_window("1. How to apply for financial aid?")
        self.append_to_chat_window("2. Information on scholarships and grants?")
        self.append_to_chat_window("3. Tuition fees and payment options?")
        self.append_to_chat_window("4. Go back to main menu")

    def handle_financial_sub_menu(self, user_input):
        if user_input == '1':
            self.append_to_chat_window("Visit the financial aid office: https://www.university.edu/financial-aid")
            self.append_to_chat_window("Fill out the required forms available on their website.")
        elif user_input == '2':
            self.append_to_chat_window("Check the scholarships and grants information here: https://www.university.edu/scholarships")
        elif user_input == '3':
            self.append_to_chat_window("Tuition fees and payment options are detailed here: https://www.university.edu/tuition")
        elif user_input == '4':
            self.current_topic = None
            self.introduce()
        else:
            self.append_to_chat_window("Invalid choice. Please try again.")

    def campus_resources(self):
        self.append_to_chat_window("Campus Resources Information:")
        self.append_to_chat_window("1. How to access library resources?")
        self.append_to_chat_window("2. Information on student health center?")
        self.append_to_chat_window("3. Career services and job placements?")
        self.append_to_chat_window("4. Go back to main menu")

    def handle_resources_sub_menu(self, user_input):
        if user_input == '1':
            self.append_to_chat_window("Access library resources online through the university library portal: https://www.university.edu/library")
        elif user_input == '2':
            self.append_to_chat_window("Visit the student health center or check their services here: https://www.university.edu/health-center")
        elif user_input == '3':
            self.append_to_chat_window("Career services offer job placement assistance. Visit their office or website for more info: https://www.university.edu/career-services")
        elif user_input == '4':
            self.current_topic = None
            self.introduce()
        else:
            self.append_to_chat_window("Invalid choice. Please try again.")

    def contact_information(self):
        self.append_to_chat_window("Contact Information:")
        self.append_to_chat_window("1. Admissions Office contact?")
        self.append_to_chat_window("2. Registrar's Office contact?")
        self.append_to_chat_window("3. Financial Aid Office contact?")
        self.append_to_chat_window("4. Campus Resources contact?")
        self.append_to_chat_window("5. Go back to main menu")

    def handle_contact_sub_menu(self, user_input):
        if user_input == '1':
            self.append_to_chat_window("Admissions Office: admissions@university.edu")
        elif user_input == '2':
            self.append_to_chat_window("Registrar's Office: registrar@university.edu")
        elif user_input == '3':
            self.append_to_chat_window("Financial Aid Office: finaid@university.edu")
        elif user_input == '4':
            self.append_to_chat_window("Campus Resources: campusresources@university.edu")
        elif user_input == '5':
            self.current_topic = None
            self.introduce()
        else:
            self.append_to_chat_window("Invalid choice. Please try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
