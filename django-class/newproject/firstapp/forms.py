from django import forms
from django.http import JsonResponse
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout, Row, Column



class contactus(forms.Form):
    fname = forms.CharField(label='First name:',max_length=30,widget=forms.TextInput(attrs={'style': 'width: 300px;','autofocus': 'autofocus'}))
    lname=forms.CharField(label='Last name:',
    max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    username=forms.CharField(label='Username',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    email=forms.CharField(label='Email',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    phno=forms.CharField(label='Phone Number',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    address=forms.CharField(label='Address',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    gstin=forms.CharField(label='GSTIN Number',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    officename=forms.CharField(label='Office Name',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    gmname=forms.CharField(label='Gm Name',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    officeadd=forms.CharField(label='Officeaddress',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    designation=forms.CharField(label='Designation',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    bankname=forms.CharField(label='BankName',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    pfnumber=forms.CharField(label='PFnumber',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))

class StudentForm(forms.Form):
    fname = forms.CharField(
    label='First name:',
    max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;','autofocus': 'autofocus'}))
    lname=forms.CharField(label='Last name:',
    max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    username=forms.CharField(label='Username',max_length=30,initial='eeeeee',required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    email=forms.CharField(label='Email',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    phno=forms.CharField(label='Phone Number',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    gstin=forms.CharField(label='GSTIN Number',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    officename=forms.CharField(label='Office Name',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    gmname=forms.CharField(label='Gm Name',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    officeadd=forms.CharField(label='Officeaddress',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    designation=forms.CharField(label='Designation',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    bankname=forms.CharField(label='BankName',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
    pfnumber=forms.CharField(label='PFnumber',max_length=30,required=False,widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
   
def __init__(self, *args, **kwargs):
        super(contactus, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(Column('fname', css_class='col-4')),  # Set the column width for the input field
            Submit('submit', 'Submit')
        )
  
from django import forms

class UserPanelForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class Student(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)
    lastname = forms.CharField(label="Enter last name", max_length=10)
    email = forms.EmailField(label="Enter email")
    file = forms.FileField()


 
