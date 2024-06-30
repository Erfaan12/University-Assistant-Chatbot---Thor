def introduce():
    print("Hello! I am Thor, your university assistant chatbot.")
    print("I can help you with the following:")
    print("1. Enrollment and Registration")
    print("2. Course Details")
    print("3. Financial Information")
    print("4. Campus Resources")
    print("5. Contact Information")

def enrollment_and_registration():
    print("Enrollment and Registration Information:")
    while True:
        print("1. How to enroll?")
        print("2. Required documents?")
        print("3. Registration fee details?")
        print("4. Go back to main menu")
        
        choice = input("Your question: ")
        
        if choice == '1':
            print("To enroll, visit the university's enrollment page: https://www.university.edu/enroll")
            print("Complete the online registration form.")
        elif choice == '2':
            print("Required documents include your ID, transcripts, and proof of residency.")
        elif choice == '3':
            print("The registration fee details can be found here: https://www.university.edu/fees")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def course_details():
    print("Course Details Information:")
    while True:
        print("1. Where to find course catalog?")
        print("2. How to select courses?")
        print("3. Information on course orientation?")
        print("4. Go back to main menu")
        
        choice = input("Your question: ")
        
        if choice == '1':
            print("You can find the course catalog here: https://www.university.edu/course-catalog")
        elif choice == '2':
            print("Contact your academic advisor to help you select courses.")
        elif choice == '3':
            print("Course orientation sessions are announced here: https://www.university.edu/events")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def financial_information():
    print("Financial Information:")
    while True:
        print("1. How to apply for financial aid?")
        print("2. Information on scholarships and grants?")
        print("3. Tuition fees and payment options?")
        print("4. Go back to main menu")
        
        choice = input("Your question: ")
        
        if choice == '1':
            print("Visit the financial aid office: https://www.university.edu/financial-aid")
            print("Fill out the required forms available on their website.")
        elif choice == '2':
            print("Check the scholarships and grants information here: https://www.university.edu/scholarships")
        elif choice == '3':
            print("Tuition fees and payment options are detailed here: https://www.university.edu/tuition")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def campus_resources():
    print("Campus Resources Information:")
    while True:
        print("1. How to access library resources?")
        print("2. Information on student health center?")
        print("3. Career services and job placements?")
        print("4. Go back to main menu")
        
        choice = input("Your question: ")
        
        if choice == '1':
            print("Access library resources online through the university library portal: https://www.university.edu/library")
        elif choice == '2':
            print("Visit the student health center or check their services here: https://www.university.edu/health-center")
        elif choice == '3':
            print("Career services offer job placement assistance. Visit their office or website for more info: https://www.university.edu/career-services")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def contact_information():
    print("Contact Information:")
    while True:
        print("1. Admissions Office contact?")
        print("2. Registrar's Office contact?")
        print("3. Financial Aid Office contact?")
        print("4. Campus Resources contact?")
        print("5. Go back to main menu")
        
        choice = input("Your question: ")
        
        if choice == '1':
            print("Admissions Office: admissions@university.edu")
        elif choice == '2':
            print("Registrar's Office: registrar@university.edu")
        elif choice == '3':
            print("Financial Aid Office: finaid@university.edu")
        elif choice == '4':
            print("Campus Resources: campusresources@university.edu")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    introduce()
    while True:
        print("\nHow can I assist you today?")
        print("Enter the number corresponding to your query:")
        print("1. Enrollment and Registration")
        print("2. Course Details")
        print("3. Financial Information")
        print("4. Campus Resources")
        print("5. Contact Information")
        print("6. Exit")
        
        choice = input("Your choice: ")
        
        if choice == '1':
            enrollment_and_registration()
        elif choice == '2':
            course_details()
        elif choice == '3':
            financial_information()
        elif choice == '4':
            campus_resources()
        elif choice == '5':
            contact_information()
        elif choice == '6':
            print("Goodbye! Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
