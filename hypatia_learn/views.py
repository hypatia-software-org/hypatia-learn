from django.views import generic as views

from civicrm_api import api


class dashboard(views.base.TemplateView):
    template_name = 'hypatia_learn/dashboard.html'
