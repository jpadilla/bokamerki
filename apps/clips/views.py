from django.views.generic import ListView

from .models import Clip


class ClipsListView(ListView):
    model = Clip

class ClipsListViewSelectRelated(ListView):
    queryset = Clip.objects.select_related('user').all()

class ClipsListViewPrefetchRelated(ListView):
    queryset = Clip.objects.select_related(
        'user').prefetch_related('likes', 'comments').all()
