from django.conf.urls import url
from . import views

urlpatterns = [
       # url(r'^$',views.home_page,name='home_page'),
       # url(r'^$',views.post_list,name='post_list'),
        url(r'^$',views.practice_profiles,name='practice_profiles'),
       # url(r'^post/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
       # url(r'^post/new/$',views.post_new,name='post_new'),
       # url(r'^post/(?P<pk>\d+)/edit/$',views.post_edit,name='post_edit'),
       # url(r'^drafs/$',views.post_draft_list,name='post_draft_list'),
       # url(r'post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
]
