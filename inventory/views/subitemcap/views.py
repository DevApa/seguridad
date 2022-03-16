from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import HeadingCapacity
from inventory.forms import HeadingCapacityForm
from django.http import JsonResponse


class HeadingCapacityListView(ListView):
    model = HeadingCapacity
    template_name = 'subitemcap/list.html'
    success_url = reverse_lazy('inv:list-subitem-cap')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Rubro Capacidad'
        context['pageview'] = 'Rubro Capacidad'
        context['object_list'] = HeadingCapacity.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-subitem-cap')
        context['url_list'] = reverse_lazy('inv:list-subitem-cap')
        return context


class HeadingCapacityCreateView(CreateView):
    model = HeadingCapacity
    form_class = HeadingCapacityForm
    template_name = "subitemcap/create.html"
    success_url = reverse_lazy('inv:list-subitem-cap')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Capacidad Rubro registrado correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Capacidad Rubro no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Capacidad Rubro'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-subitem-cap')
        return context