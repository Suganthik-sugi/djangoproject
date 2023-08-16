from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import contactus
from firstapp.forms import StudentForm ,Student
from django import forms
from .models import Details,Employee
from django.forms import ModelForm
import pandas as pd
from django.db.models.signals import post_save
from django.dispatch import receiver
import csv
from reportlab.pdfgen import canvas
from firstapp.function.functions import handle_uploaded_file
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from .utils.validation import validate_form_data 
from django.contrib import messages
import pytz
import os
import xlsxwriter



# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    default_value="some value"
    if request.method == 'POST':
        form = contactus(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            validation_errors = validate_form_data(cleaned_data)

            if not validation_errors:
                # Return an HttpResponse for successful form submission
                # return HttpResponse(cleaned_data['fname'])
                    contact_data = Details(
                         fname=cleaned_data['fname'],lname=cleaned_data['lname'],username=cleaned_data['username'],
                         email=cleaned_data['email'],phno=cleaned_data['phno'],address=cleaned_data['address'],
                         gstin=cleaned_data['gstin'],officename=cleaned_data['officename'],gmname=cleaned_data['gmname'],
                         officeaddress=cleaned_data['officeadd'])
                    contact_data.save()
                    created=contact_data.id
                    Details.objects.filter(id=created).update(created_by=created)

                    emp_data=Employee(
                    designation=cleaned_data['designation'],
                    bankname=cleaned_data['bankname'],
                    pfnumber=cleaned_data['pfnumber'],
                    empid_id=contact_data.id)
                    emp_data.save()
                    created1=emp_data.id
                    Employee.objects.filter(id=created1).update(created_by=created1,empid_id=created)
                    details_data=Details.objects.all()
                    num_fields = len(details_data)
                    if num_fields % 10 == 0:
                      indian_time_zone = pytz.timezone('Asia/Kolkata')
                      current_time =  pd.Timestamp.now(indian_time_zone)

                       # Format the time in 12-hour format with AM/PM and the time zone abbreviation
                      formatted_time = current_time.strftime('%I:%M')

                      current_datetime = pd.Timestamp.now().strftime('%Y')
                      current_datetime1 = pd.Timestamp.now().strftime('%m')
                      current_datetime2 = pd.Timestamp.now().strftime('%d')

                      separator = '-'
                      separator1='_'

                      # old_filename = 'old_filename.txt'
                      filename = f'firstapp{separator}{current_datetime}{separator}{current_datetime1}{separator}{current_datetime2}{separator1}{formatted_time}.csv'

                      response = HttpResponse(content_type='text/csv')
                      response['Content-Disposition'] = f'attachment; filename={filename}'

                      writer = csv.writer(response)
                      header_row = ['firsname','lastname','username','email','address','gitin','officename']
                      writer.writerow(header_row)
                      details_data = Details.objects.all()
                      for details_obj in details_data:
                          data_row = [details_obj.fname,details_obj.lname,details_obj.username,details_obj.email]
                          writer.writerow(data_row)
                      return response
                    return JsonResponse({'message': 'User created successfully!', 'user_id': num_fields}, status=201)
            else:
                # Display validation errors in the template
                for field, error in validation_errors.items():
                    form.add_error(field, error)
        else:
            form = contactus()
    else:
        form = contactus(initial={'fname':default_value})

    context = {'form': form}
    return render(request, 'firstapp/register.html', context)

        
def result(request):
    mydata=Details.objects.filter(is_active=1)
    reg_dict={'reg':mydata}
    return render(request,'firstapp/template.html',reg_dict)

def edit(request, id):
    employee = Details.objects.get(id=id)
    employee1=Employee.objects.get(empid_id=id)
    print(employee)
    if request.method == 'POST':
    #     form = contactus(request.POST,isinstance=employee)
    #     if form.is_valid():
    #         # print(form.cleaned_data['fname'])
    #         print("test")
    #         # Update the employee object with the submitted form data
    #         # Details.fname = form.cleaned_data['fname']
    #         # Details.lname = form.cleaned_data['lname']
    #         # Details.address = form.cleaned_data['address']
    #         # Details.officename = form.cleaned_data['officename']
    #         # Details.gmname = form.cleaned_data['gmname']
    #         # Details.officeaddress=form.cleaned_data['officeadd']
    #         # # Save the updated employee record to the database
    #         # Details.save()
    #         # # Redirect to some success page or back to the view page
    #         # return redirect('result')
    # else:
    #     # If it's a GET request, initialize the form with the employee data
    #     form = contactus(initial={
    #         'fname': employee.fname,
    #         'lname': employee.lname,
    #         'email': employee.email,
    #         'username':employee.username,
    #         'phno':employee.phno,
    #         'address':employee.address,
    #         'gstin':employee.gstin,
    #         'officename':employee.officename,
    #         'gmname':employee.gmname,
    #         'officeadd':employee.officeaddress,
    #         'designation':employee1.designation,
    #         'bankname':employee1.bankname,
    #         'pfnumber':employee1.pfnumber,
    #     })

    # return render(request, 'firstapp/update.html', {'reg': form})
     return render(request, 'firstapp/update.html')

def pdf(request):
    details_data = Details.objects.all()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename= "get_pdf.pdf"'
    p = canvas.Canvas(response)
    
    p.setFont("Times-Roman", 15)
    y_position=800

    for details_obj in details_data:
       data_row=f"Name:{details_obj.fname},Lname:{details_obj.lname}"
       p.drawString(100,y_position, data_row)
       y_position-=20
    
    
    p.showPage()
    p.save()
    return response

def fileup(request):
    
     if request.method=='POST':
        student=StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfully")
     else:
      student=Student()
      return render(request, 'firstapp/file.html', {'form':student})
     
def mail(request):
 try:
  sender = "suginkl@gmail.com"
  app_password = "gqklgxwicjjijwnf"  # Replace this with the actual app password
  rec = "veluthambi12041997.erode@gmail.com"
    

# Create a secure connection to Gmail's SMTP server
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()

# Login to your Gmail account using the app password
  s.login(sender, app_password)

# Create the email message
  message = MIMEMultipart("alternative")
  message['Subject'] = "image attachment test"
  message['From'] = sender
  message['To'] = rec
  
# Define the HTML content of the email
  html = "<html><body><p>Hello Suganthi,<br>Your order has been placed successfully!</p></body></html>"

# Attach the HTML content to the email message
  htmlPart = MIMEText(html, 'html')
  message.attach(htmlPart)
  
  image_path = r'D:\django-class\newproject\static\firstapp\images'
  image_data = None
  try:
    with open(image_path, 'rb') as file:
        image_data = file.read()
        image = MIMEImage(image_data, name='image.png')
        message.attach(image)
  except Exception as e:
       print(f"Error occurred: {e}")
        
# Send the email
  s.sendmail(sender, rec, message.as_string())

# Close the connection
  s.quit()
  return HttpResponse('Email sent successfully!')

 except smtplib.SMTPException as e:
        # If there was an error during the email sending process, handle the exception and return an error response
  return HttpResponse(f'Error sending email: {str(e)}', status=500)
   
def delete(request,id):
    product_detail = Details.objects.get(id=id)
    Details.objects.filter(id=id).update(is_active=0,is_deleted=1)
    messages.error(request,"Delete Successfully completed")
    return redirect('result')

from .forms import UserPanelForm

def user_panel(request):
    if request.method == 'POST':
        form = UserPanelForm(request.POST)
        if form.is_valid():
            return redirect('result')
    else:
        form = UserPanelForm()

    return render(request, 'firstapp/demo.html', {'form': form})

def excelfile(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    # Create a new Excel workbook and add a worksheet
    workbook = xlsxwriter.Workbook(response, {'in_memory': True})
    worksheet = workbook.add_worksheet()
    heading_format = workbook.add_format({'bold': True, 'align': 'center'})
    heading_format = workbook.add_format({'border': 1, 'border_color': 'black'})
    heading_format.set_font_color('blue')
    heading_format.set_font_name('Arial')
    data_format = workbook.add_format({'align': 'left'})
    data_format.set_font_color('green')
    data_format.set_font_name('Times New Roman')
    heading_format.set_bold(True)
    # Add some data to the worksheet
    data = [['firsname','lastname','username','email','address','gitin','officename'],
            ["John", 25, "New York"],
            ["Jane", 30, "Los Angeles"]]
    worksheet.write_row(0, 0, data[0],heading_format)
    for row_num, row_data in enumerate(data[1:],start=1):
        for col_num, cell_value in enumerate(row_data):
            worksheet.write(row_num, col_num, cell_value,data_format)

    # Close the workbook
    workbook.close()

    return response




    

