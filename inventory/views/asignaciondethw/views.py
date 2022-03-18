from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import ItemAssigmentHardwareDetail, Heading
from inventory.forms import ItemAssigmentHardwareDetailForm
from django.http import JsonResponse


class ItemAssigmentHardwareDetailListView(ListView):
    model = ItemAssigmentHardwareDetail
    template_name = 'asignaciondethw/list.html'
    success_url = reverse_lazy('inv:list-assignment-hw')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Asignacion Hardware'
        context['pageview'] = 'Asignacion Hardware'
        context['object_list'] = ItemAssigmentHardwareDetail.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-assignment-hw')
        context['url_list'] = reverse_lazy('inv:list-assignment-hw')
        return context


class ItemAssigmentHardwareDetailCreateView(CreateView):
    model = ItemAssigmentHardwareDetail
    form_class = ItemAssigmentHardwareDetailForm
    template_name = "asignaciondethw/create.html"
    success_url = reverse_lazy('inv:list-assignment-hw')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Asignacion Hardware registrada correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Asignacion Hardwar no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Asignacion Hardware'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-assignment-hw')
        return context