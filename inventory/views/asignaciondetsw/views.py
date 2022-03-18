from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import SoftwareDetail
from inventory.forms import SoftwareDetailForm
from django.http import JsonResponse


class SoftwareDetailListView(ListView):
    model = SoftwareDetail
    template_name = 'asignaciondetsw/list.html'
    success_url = reverse_lazy('inv:list-assignment-sw')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Asignacion Software'
        context['pageview'] = 'Asignacion Software'
        context['create_url'] = reverse_lazy('inv:create-assignment-sw')
        context['url_list'] = reverse_lazy('inv:list-assignment-sw')
        return context


class SoftwareDetailCreateView(CreateView):
    model = SoftwareDetail
    form_class = SoftwareDetailForm
    template_name = "asignaciondetsw/create.html"
    success_url = reverse_lazy('inv:list-assignment-sw')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Asignacion Software registrada correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Asignacion Software no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Asignacion Software'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-assignment-sw')
        return context