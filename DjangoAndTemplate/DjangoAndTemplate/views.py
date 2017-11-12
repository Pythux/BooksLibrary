from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


class HomePage(TemplateView):
    template_name = 'index.html'
