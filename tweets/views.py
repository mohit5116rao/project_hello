from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tweet


# Create your views here.

class TweetListView(ListView):
    model = Tweet
    queryset = Tweet.objects.all()
    template_name = 'tweets/tweet_list.html'


class TweetDetailView(DetailView):
    model = Tweet
    template_name = 'tweets/tweet_detail.html'


class TweetDeleteView(DeleteView):
    model = Tweet
    template_name = 'tweets/delete.html'

    def get_success_url(self):
        return reverse('tweets:list')


class TweetUpdateView(UpdateView):
    model = Tweet
    fields = [
        'tweets',
    ]
    template_name = 'tweets/update.html'

    def get_success_url(self):
        return reverse('tweets:list')


class TweetCreateView(CreateView):
    model = Tweet
    fields = [
        'tweets',
    ]
    template_name = 'tweets/create.html'

    def get_success_url(self):
        return reverse('tweets:list')














        # def tweet_list(request):
        #     object_list = Tweet.objects.all()
        #     context = {
        #         'object_list': object_list
        #     }
        #
        #     return render(request, 'tweets/tweet_list.html', context)
