from django.views import generic as views


class ecr_info(views.base.TemplateView):
    template_name = 'resources/ecr/info.html'


class ecr_request(views.base.TemplateView):
    template_name = 'resources/ecr/request.html'


class ecr_status(views.base.TemplateView):
    template_name = 'hypatia_learn/dashboard.html'
