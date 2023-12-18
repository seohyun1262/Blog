from django.shortcuts import render
from blog.models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.
def index(req):
    post_latest = Post.objects.order_by("-createDate")[:4]
    context = {
        "post_latest" : post_latest
    }

    return render(req, "index.html", context = context)

class PostDetailView(generic.DetailView):
    model = Post

class PostCreateView(generic.DeleteView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "subtitle", "writer", "content"]

def delete(req, id):
    delete_blog = Post.objects.get(id= id)
    delete_blog.delete()

    return redirect('index')

class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "subtitle", "writer", "content"]
    template_name_suffix = '_edit'
