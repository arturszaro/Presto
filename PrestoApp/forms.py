from django import forms
from PrestoApp.models import Post, ItemMenu


class PostForm(forms.ModelForm):

        class Meta():
            model = Post
            fields=('author','title','text')



class ItemMenuForm(forms.ModelForm):

        class Meta():
            model = ItemMenu
            fields=('category','number', 'title', 'ingredients', 'price1','price2')
