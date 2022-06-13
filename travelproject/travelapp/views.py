from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from  .models import team

# Create your views here.
# def demo(request):
#     return HttpResponse("hello world")
def demo(request):
    obj=place.objects.all()
    obj1=team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})