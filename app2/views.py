from django.shortcuts import render

# Create your views here.
def bro(request):
    return render(request,'bro.html')