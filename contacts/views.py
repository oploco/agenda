from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404
from django.shortcuts import get_object_or_404, render


from .models import Contacto,Telefono

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'contacts/index.html'
    context_object_name = 'latest_contact_list'

    def get_queryset(self):
        """Return the last five published questions."""

        return Contacto.objects.filter(
            date__lte=timezone.now()
        ).order_by('-nombre')[:5]


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")