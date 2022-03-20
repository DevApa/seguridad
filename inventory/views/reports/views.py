import datetime
import os.path

from bs4.builder import HTML
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import View
from weasyprint import CSS

from authentication.models import Usuario
from inventory.models import Location
from organization.models import University
from seguridad import settings


class ReportViewer(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('reports/results/result.html')
            context = {
                'location': Location.objects.all(),
                'aditionalData': {
                    'institution': University.objects.filter(state=True),
                    'date': datetime.date.today(),
                    'user': Usuario.objects.filter(id=self.request.user.id)
                },
                'icon': '{}{}'.format(settings.MEDIA_URL, 'static/images/sigocd/logo-sigocd-512.png')
            }

            html = template.render(context)
            css_url = os.path.join(settings.BASE_DIR, 'static/libs/css/bootstrap.min.css')
            pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('inv:report-location'))
