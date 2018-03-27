from django.views import generic as views

from civicrm_api import api

from .forms import NameForm


class mentor_find(views.base.TemplateView):

    template_name = 'resources/mentor/find_mentor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        civi_api = api.CivicrmApi()
        context['info'] = civi_api.get_groupcontact_contacts(
            'Onboarding_Mentor_11')['values']
        return context


class mentor_display(views.base.TemplateView):

    template_name = 'resources/mentor/display_mentor.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        civi_api = api.CivicrmApi()
        context['info'] = civi_api.get_contact_mentor(context['cid'])
        return context


class mentor_profile_edit(views.base.TemplateView):

    template_name = 'resources/mentor/profile_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        civi_api = api.CivicrmApi()
        info = civi_api.get_contact_mentor(context['cid'])

        form_data = {}
        form_data['pronouns'] = info['custom_5']
        form_data['bio'] = info['custom_92']
        form_data['hobbies'] = info['custom_93']
        form_data['name'] = info['display_name']
        form_data['skills'] = info['tags']
        context['form'] = NameForm(initial=form_data)
        return context
