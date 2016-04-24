from django.conf.urls import include, url
from . import views

# URL Patterns
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail')
]
