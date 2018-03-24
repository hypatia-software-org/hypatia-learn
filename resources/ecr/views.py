from django.views import generic as views

from civicrm_api import api


class ecr_info(views.base.TemplateView):
    template_name = 'resources/ecr/info.html'


class ecr_request(views.base.TemplateView):
    template_name = 'resources/ecr/request.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        civi_api = api.CivicrmApi()
        context['info'] = civi_api.query_api(self.request.user.id)
        return context


class ecr_status(views.base.TemplateView):
    template_name = 'hypatia_learn/dashboard.html'
