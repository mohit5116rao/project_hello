from django.conf.urls import url

from .views import blog_list, create_blog, blog_detail, blog_delete

urlpatterns = [

    url(r'^list/', blog_list, name='list'),
    url(r'^create/', create_blog, name='create'),
    url(r'^detail/(?P<pk>\d+)$', blog_detail, name='detail'),
   # url(r'^update/(?P<pk>\d+)$', TweetUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)$',blog_delete, name='delete'),

]
