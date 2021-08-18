from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from catalog.models import *
from django.forms import ModelForm
from django import forms

# class DateInput(forms.DateInput):
# 	input_type = 'date'



# class CreateUserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['username','email','password1','password2' ]

# class RegisterbookForm(ModelForm):
# 	class Meta:
# 		model = Book
# 		fields = '__all__'
		

# class RegisterAutoForm(ModelForm):
# 	class Meta:
# 		model = Author
# 		fields = '__all__'
# 		widgets= {'author_date_of_birth':DateInput(),'author_date_of_death': DateInput()}

# class RegisterLanguageForm(ModelForm):
# 	class Meta:
# 		model = Language
# 		fields = ['name']

# class RegisterGenreForm(ModelForm):
	# class Meta:
	# 	model = Genre
	# 	fields = '__all__'

