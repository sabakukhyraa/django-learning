from django.shortcuts import render
from .models import GeneralSetting

# Create your views here.
def generalSetting(request):
  generalSettings = GeneralSetting.objects.all()
  return render(request, 'base.html', {'generalSettings': generalSettings})