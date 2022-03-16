from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import HeadingDetail
from inventory.forms import HeadingDetailForm
from django.http import JsonResponse


class HeadingDetailListView(ListView):
    model = HeadingDetail
    template_name = 'subitemdet/list.html'
    success_url = reverse_lazy('inv:list-subitem-det')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Rubro Detalle'
        context['pageview'] = 'Rubro Detalle'
        context['object_list'] = HeadingDetail.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-subitem-det')
        context['url_list'] = reverse_lazy('inv:list-subitem-det')
        return context


class HeadingDetailCreateView(CreateView):
    model = HeadingDetail
    form_class = HeadingDetailForm
    template_name = "subitemdet/create.html"
    success_url = reverse_lazy('inv:list-subitem-det')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Detalle Rubro registrado correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Detalle Rubro no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Detalle Rubro'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-subitem-det')
        return context