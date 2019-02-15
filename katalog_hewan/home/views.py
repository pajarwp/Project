from django.shortcuts import render

# Create your views here.
def isi_home(request):
    return render(request, 'home/home.html', {})

def isi_about(request):
    return render(request, 'home/about.html', {})

def isi_fun(request):
    return render(request, 'home/fun.html', {})