from django.views.generic import ListView
from django.utils import timezone

from .models import Ente, Registro


class RegistroListView(ListView):

    model = Registro

    def get_context_data(self, **kwargs):
        context = super(RegistroListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

