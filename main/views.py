from django.views.generic import ListView, DetailView, CreateView,FormView
from main.models import Post, Comment
from .forms import CommentForm
from django.urls import reverse
from django.shortcuts import render
from main.forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages


class ListPageView(ListView):
    template_name = 'home.html'
    model = Post
    paginate_by= 10


class DetailPageView(DetailView,FormView):
    model = Post
    template_name = 'detail_page.html'
    form_class = CommentForm
   

def add_comment_page(request, **kwargs):
    form = CommentForm()
    slug = kwargs['slug']
    post =Post.objects.get(slug=slug)
    if request.method == 'POST':
       
        form = CommentForm(request.POST)
        if form.is_valid:
            form.instance.post_id = post.id
            form.save(commit=True)
            messages.success(request,'Your comment has been submitted and will be visible after the site owner approves',extra_tags='alert')
            return HttpResponseRedirect(reverse('content',kwargs={'slug':slug}) + '#comments')

