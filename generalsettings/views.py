from django.shortcuts import render
from .models import GeneralSetting

# Create your views here.
def generalSetting(request):
  generalSettings = GeneralSetting.objects.all()
  print(generalSettings)
  return render(request, 'home.html', {'generalSettings': generalSettings})