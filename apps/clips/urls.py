from django.conf.urls import patterns, url

from .views import (ClipsListView, ClipsListViewSelectRelated,
                    ClipsListViewPrefetchRelated)


urlpatterns = patterns('',
    url(r'^$', ClipsListView.as_view(), name='clips_list'),
    url(r'^select_related/$', ClipsListViewSelectRelated.as_view(), name='clips_list2'),
    url(r'^prefetch_related/$', ClipsListViewPrefetchRelated.as_view(), name='clips_list3'),
)
