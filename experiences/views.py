from django.shortcuts import render
from .models import Experience

# Create your views here.
def experience_list(request):
  experiences = Experience.objects.all().order_by('startDate').reverse()
  return render(request, 'experiences/experience_list.html', {'experiences': experiences})