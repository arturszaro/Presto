from django.shortcuts import render,get_object_or_404,redirect
from PrestoApp.models import Post, ItemMenu, CategoryMenu
from django.urls import reverse, reverse_lazy
from PrestoApp.forms import PostForm, ItemMenuForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
# Create your views here.


class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'PrestoApp/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'PrestoApp/post_draft_list.html'
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True)

class MenuListView(ListView):
    model = ItemMenu
    template_name = 'PrestoApp/menu.html'
    def get_queryset(self):
        return ItemMenu.objects.order_by('number')

class MenuUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = ItemMenuForm
    model = ItemMenu

class MenuDeleteView(LoginRequiredMixin, DeleteView):
    model = ItemMenu
    success_url = reverse_lazy('menu')

class CreateItemMenuView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = ItemMenuForm
    model = ItemMenu

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def kontakt(request):
    return render(request, 'PrestoApp/kontakt.html')

def galeria(request):
    return render(request, 'PrestoApp/galeria.html')
