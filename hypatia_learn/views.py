from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views


@method_decorator(login_required, name='dispatch')
class dashboard(views.base.TemplateView):
    template_name = 'hypatia_learn/dashboard.html'
