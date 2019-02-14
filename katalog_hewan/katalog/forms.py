from django import forms

from .models import Binatang

class PostForm(forms.ModelForm):

    class Meta:
        model = Binatang
        fields = ('gambar', 'nama', 'latin', 'deskripsi')