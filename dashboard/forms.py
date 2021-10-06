from django import forms 
from dashboard.models import *
from django.contrib.auth.forms import *

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title", "description"]
        widgets = {"title":forms.TextInput(attrs = {"class":"form-control"}),
        "description":forms.Textarea(attrs = {"class":"form-control"})}


class DateTimeInput(forms.DateTimeInput):
    input_type = "date"

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ["subject", "title", "description", "due", "is_finished"]
        widgets = {"subject":forms.TextInput(attrs = {"class":"form-control"}), "due":DateTimeInput(),
        "title":forms.TextInput(attrs = {"class":"form-control"}),
        "description":forms.Textarea(attrs = {"class":"form-control"}),
        }        
        
class DashboardForm(forms.Form):
    text = forms.CharField(max_length = 100, label = "Enter your Search:")


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "is_finished"]
        widgets = {"title":forms.TextInput(attrs = {"class":"form-control"}),

        }

class ConversionForm(forms.Form):
    CHOICES = [("length", "Length"), ("mass","Mass")]
    measurement = forms.ChoiceField(choices= CHOICES, widget = forms.RadioSelect)
class ConversionLengthForm(forms.Form):
    CHOICES = [("yard", "Yard"), ("foot", "Foot")]
    input = forms.CharField(required= False, widget = forms.TextInput( 
    attrs = {"type":"number", "placeholder":"Enter the Number", "class":"form-control"}

    ))
    measure1 = forms.CharField(
        label = "", widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label = "", widget = forms.Select(choices = CHOICES)
    )
class ConversionForm(forms.Form):
    CHOICES = [("length", "Length"), ("mass","Mass")]
    measurement = forms.ChoiceField(choices= CHOICES, widget = forms.RadioSelect)
class ConversionMassForm(forms.Form):
    CHOICES = [("pound", "Pound"), ("kilogram", "Kilogram")]
    input = forms.CharField(required= False, widget = forms.TextInput( 
    attrs = {"type":"number", "placeholder":"Enter the Number", "class":"form-control"}

    ))
    measure1 = forms.CharField(
        label = "", widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label = "", widget = forms.Select(choices = CHOICES)
    )


class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput(attrs = {"autofocus":True, "class":"form-control"}))
    password = forms.CharField(label = "Password", widget = forms.PasswordInput(attrs = {"autocomplete":"current-password", "class":"form-control"}))
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label = "username", widget = forms.TextInput(attrs = {"class":"form-control"}))
    password1 = forms.CharField(label = "Password", widget = forms.PasswordInput(attrs = {"class":"form-control"}))
    password2 = forms.CharField(label = "Confirm Password (again)", widget = forms.PasswordInput(attrs = {"class":"form-control"}))
    class meta:
        model = User
        fields = ["username", "password1", "password2"]