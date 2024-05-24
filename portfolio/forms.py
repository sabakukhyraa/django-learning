from django import forms

class EmailForm(forms.Form):
  email = forms.EmailField(
    label='',
    max_length=100, 
    required=True,
    widget=forms.EmailInput(attrs={
      'class': 'outline-none rounded-md shadow-lg py-2 px-4 border',
      'placeholder': 'Enter your email',
      'id': 'email-field'
    })
  )
