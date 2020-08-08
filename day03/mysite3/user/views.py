from django.shortcuts import render

# Create your views here.
def UserIndex(request):
    return render(request,'UserIndex.html')