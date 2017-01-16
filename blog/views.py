from django.shortcuts import render
from django.utils import timezone
from .models import Post #el punto significa el mismo directorio, views y models están en el mismo directorio.
# Post es el modelo de models.

def post_list(request):
    posts= Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

# Create your views here.
