from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import SoftwareDetail
from inventory.forms import SoftwareDetailForm
from django.http import JsonResponse


class SoftDetList(ListView):
    model = SoftwareDetail
    template_name = 'asignaciondetsw/list.html'
    success_url = reverse_lazy('inv:list-assign-sw')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Asignacion Software'
        context['pageview'] = 'Asignacion Software'
        context['object_list'] = SoftwareDetail.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-assign-sw')
        context['url_list'] = reverse_lazy('inv:list-assign-sw')
        return context


class SoftDetCreate(CreateView):
    model = SoftwareDetail
    form_class = SoftwareDetailForm
    template_name = "asignaciondetsw/create.html"
    success_url = reverse_lazy('inv:list-assign-sw')

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
        context['title'] = 'Creaci??n de Asignacion Software'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-assign-sw')
        return context

class SoftDetUpdate(UpdateView):
    model = SoftwareDetail
    form_class = SoftwareDetailForm
    template_name = "asignaciondetsw/update.html"
    success_url = reverse_lazy('inv:list-assign-sw')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
           if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = f'Asignacion Software actualizado correctamente'
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
        context['title'] = 'Actualizar Asignacion Software'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inv:list-assign-sw')
        return context


class SoftDetDelete(DeleteView):
    model = SoftwareDetail
    success_url = reverse_lazy('inv:list-assign-sw')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'Asignacion Software eliminado correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('inv:list-assign-sw')
