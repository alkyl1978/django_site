from django.views.generic import ListView
from .models import Repository

class repository_listViews(ListView):
    template_name='gitweb/repository_list.html'
    model = Repository
    context_object_name = 'repository_list'
    queryset = Repository.objects.all()
