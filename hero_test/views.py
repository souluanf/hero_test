from django.views.generic import TemplateView
import os


class ReadMeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        markdowntext = open(os.path.join(os.path.dirname(__file__), '../README.md')).read()

        context = super(ReadMeView, self).get_context_data(**kwargs)
        context['markdowntext'] = markdowntext

        return context
