from django import forms
# from .models import Students

class Student_form(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput())
    # class Meta:
    #     model = Student   
    #     fields='__all__'  


    
