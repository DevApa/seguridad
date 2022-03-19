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
                    message = f'Asignacion Hardward no se pudo registrar!'
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

class ItemAssigmentHardwareDetailUpdateView(UpdateView):
    model = ItemAssigmentHardwareDetail
    form_class = ItemAssigmentHardwareDetailForm
    template_name = "asignaciondethw/update.html"
    success_url = reverse_lazy('inv:list-assignment-hw')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
           if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = f'Asignacion Hardware actualizado correctamente'
                error = 'No hay error'
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 201
                return response
            else:
                message = f'{self.model.__name__} no se pudo actualizar!'
                error = form.errors
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 400
                return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Asignacion Hardware'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inv:list-assignment-hw')
        return context


class ItemAssigmentHardwareDetailDeleteView(DeleteView):
    model = ItemAssigmentHardwareDetail
    success_url = reverse_lazy('inv:list-assignment-hw')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'Asignacion Hardware eliminado correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('inv:list-assignment-hw')
