from django.shortcuts import render
from django.http import HttpResponse
from .forms import Student_form
# Create your views here.
def dashbord(request):
    if request.method== 'POST':
        print(request.POST,'++++++++++++++++++++++')
    form = Student_form()
    return render(request, 'dashbord.html',{"form":form})
