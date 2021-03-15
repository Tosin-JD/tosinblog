from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Blog


# Create your views here.
class BlogList(generic.ListView):
    model = Blog
    template_name = 'blog/blog_list.html'


class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'


class CreateBlog(generic.CreateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:list')


class UpdateBlog(generic.UpdateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:list')


class DeleteBlog(generic.DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog:list')


