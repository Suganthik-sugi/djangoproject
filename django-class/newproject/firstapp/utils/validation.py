
# validation.py
import re

def is_valid_email(email):
    # Regular expression for email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None




def validate_form_data(data):
    # Perform validation logic here
    errors = {}
    # Check data and add errors to the errors dictionary if necessary
    # if not data['email'].endswith('@example.com'):
        # errors['email'] = "Email must be from example.com domain."

    if not data['email'] and not is_valid_email(data['email']):
            errors['email'] = "Enter your email "
    
    phno=data.get('phno','')
    if 'phno' in data:
        phone_number = data['phno']
        pattern = r'^91\d{10}$'

    if not re.match(pattern, phone_number):
            errors['phno'] = "Phone number must start with '91' and have exactly 12 digits."
    
    if len(data['phno']) < 10:
        errors['phno'] = "Phonenumber must be at least 10 characters long."
    
    fname = data.get('fname', '')
    if not fname:
        errors['fname'] = "First Name is required."
    elif not fname[0].isupper():
        errors['fname'] = "Name must start with a capital letter."

    lname = data.get('lname', '')
    if not lname:
        errors['lname'] = "Last Name is required."
    elif not lname[0].isupper():
        errors['lname'] = "Name must start with a capital letter."

    username = data.get('username', '')
    if not username:
        errors['username'] = "Username is required."

    address = data.get('address', '')
    if not address:
        errors['address'] = "Address is required."    
    
    officename = data.get('officename', '')
    if not officename:
        errors['officename'] = "Office Name is required."

    gmname = data.get('gmname', '')
    if not gmname:
        errors['gmname'] = "GM name is required."

    officeadd = data.get('officeadd', '')
    if not officeadd:
        errors['officeadd'] = "Office address is required."

    designation = data.get('designation', '')
    if not designation:
        errors['designation'] = "Designation is required."

    bankname = data.get('bankname', '')
    if not bankname:
        errors['bankname'] = "Bank Name is required."

    if len(data['gstin']) < 10:
        errors['gstin'] = "gstin must be at least 10 characters long."

    if len(data['pfnumber']) < 10:
        errors['pfnumber'] = "PF number must be at least 10 characters long."

    return errors  # Return empty dictionary if data is valid

    
