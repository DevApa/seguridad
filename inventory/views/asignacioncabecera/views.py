from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import ItemAssignmentHeader
from inventory.forms import ItemAssignmentHeaderForm
from django.http import JsonResponse


class ItemAssignmentHeaderListView(ListView):
    model = ItemAssignmentHeader
    template_name = 'asignacion/list.html'
    success_url = reverse_lazy('inv:list-assignment-cap')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Asignacion'
        context['pageview'] = 'Asignacion'
        context['create_url'] = reverse_lazy('inv:create-assignment-cap')
        context['url_list'] = reverse_lazy('inv:list-assignment-cap')
        return context


class ItemAssignmentHeaderCreateView(CreateView):
    model = ItemAssignmentHeader
    form_class = ItemAssignmentHeaderForm
    template_name = "asignacion/create.html"
    success_url = reverse_lazy('inv:list-assignment-cap')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Asignacion registrada correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Asignacion no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Asignacion'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-assignment-cap')
        return context