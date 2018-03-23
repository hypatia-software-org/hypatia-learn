from django.views import generic as views


class mentor_find(views.base.TemplateView):
    template_name = 'hypatia_learn/dashboard.html'
