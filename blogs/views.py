from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect

from .models import Blog
from .forms import BlogForm

# Create your views here.

def blog_list(request):
    queryset = Blog.objects.all()
    context = {
        'object_list': queryset,
    }

    return render(request, 'blogs/blog_list.html', context)


def create_blog(request):
    if not request.user.is_authenticated():
        return reverse('login')
    form = BlogForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect('/blogs/list')

    context = {
        'form': form,
    }

    return render(request, 'blogs/create.html', context)

def blog_detail(request, pk=None):
    instance = Blog.objects.get(pk=pk)
    context = {
        'object': instance,
    }

    return render(request, 'blogs/detail.html', context)

def blog_delete(request,pk=None):
    instance=Blog.objects.get(pk=pk)
    
    context= {
        'object': instance,
    }

    return render(request,'blogs/delete.html',context)


