# user_details_form.py

def collect_user_details():
    print("Welcome to the User Details Form")
    print("=================================")

    # Collecting user inputs
    name = input("Enter your Name*: ")
    email = input("Enter your Email*: ")
    message = input("Enter your Message (optional): ")

    # Validating required fields
    if not name or not email:
        print("Error: Name and Email are required fields. Please try again.")
        return

    # Displaying the details back to the user
    print("\nThank you! Here are the details you entered:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    if message:
        print(f"Message: {message}")
    else:
        print("Message: (No message provided)")

if __name__ == "__main__":
    collect_user_details()
