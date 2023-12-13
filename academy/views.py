from django.views.generic import TemplateView


class AcademyHomeView(TemplateView):
    template_name = 'academy/index.html'
