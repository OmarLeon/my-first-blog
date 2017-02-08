from django.conf.urls import url
from . import views
from django.views.generic import DetailView, ListView
from django.views.generic.dates import *
from blog.models import VideoCategory, Video

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^category/(?P<slug>[-\w]+)/$', DetailView.as_view(
            model=VideoCategory, context_object_name='category'
        ), name='videostream_category_detail'),

    url(r'^categories/$', ListView.as_view(
            model=VideoCategory,
        ), name='videostream_category_list'),


    ## Date Based Views
    url(r'^latest/$', ArchiveIndexView.as_view(
            queryset=Video.objects.filter(is_public=True),
            date_field='publish_date',
        ), name='videostream_video_archive'),

    url(r'^(?P<year>\d{4})/(?P<month>\w+)/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', 
        DateDetailView.as_view(
            queryset=Video.objects.filter(is_public=True),
            date_field='publish_date',
        ),
        name='videostream_video_detail'),

    url(r'^(?P<year>\d{4})/(?P<month>\w+)/(?P<day>\d{1,2})/$',
        DayArchiveView.as_view(
            queryset=Video.objects.filter(is_public=True),
            date_field='publish_date',
        ), name='videostream_video_day'),

    url(r'^(?P<year>\d{4})/(?P<month>\w+)/$',
        MonthArchiveView.as_view(
            queryset=Video.objects.filter(is_public=True),
            date_field='publish_date',
        ), name='videostream_video_month'),

    url(r'^(?P<year>\d{4})/$', YearArchiveView.as_view(
            queryset=Video.objects.filter(is_public=True),
            date_field='publish_date',
        ), name='videostream_video_year'),



]