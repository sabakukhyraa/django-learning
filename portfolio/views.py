from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.conf import settings
from .forms import EmailForm
import os

def home(request):
  # return HttpResponse("home")
  return render(request, 'home.html')

def about(request):
  # return HttpResponse("about")
  return render(request, 'about.html')

def send_resume_with_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_address = form.cleaned_data['email']

            pdf_path = os.path.join(settings.MEDIA_ROOT, 'MayResume2024.pdf')

            email = EmailMessage(
                'Ali Kerem Ata - CV',
                'Hi, I hope you like my resume! Thanks.',
                'alikeremata55@gmail.com',
                [email_address],
            )

            with open(pdf_path, 'rb') as pdf:
                email.attach('MayResume2024.pdf', pdf.read(), 'application/pdf')
            email.send()

            return HttpResponse('Email sent successfully')
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form})