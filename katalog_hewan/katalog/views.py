from django.shortcuts import render, redirect, get_list_or_404
from .models import Binatang
from .forms import PostForm

def binatang(request) :
    binatang = Binatang.objects.all()
    return render(request, 'binatang/binatang.html', {'binatang':binatang})

def new_binatang(request) :
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = PostForm()
    return render(request, 'binatang/new_binatang.html', {'form': form})

def detail_binatang(request, binatang_id):
    detail_binatang = get_list_or_404(Binatang, id=binatang_id)
    return render(request, 'binatang/detail_binatang.html', {'detail_binatang': detail_binatang})

def thanks(request) :
    return render(request, 'binatang/thanks.html',{})
