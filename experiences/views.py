from django.shortcuts import render

# Create your views here.
def experience_list(request):
  return render(request, 'experiences/experience_list.html')