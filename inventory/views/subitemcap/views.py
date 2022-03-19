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

class HeadingCapacityUpdateView(UpdateView):
    model = HeadingCapacity
    form_class = HeadingCapacityForm
    template_name = "subitemcap/update.html"
    success_url = reverse_lazy('inv:list-subitem-cap')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
           if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = f'Capacidad Rubro actualizado correctamente'
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
        context['title'] = 'Actualizar Capacidad Rubro'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inv:list-subitem-cap')
        return context


class HeadingCapacityDeleteView(DeleteView):
    model = HeadingCapacity
    success_url = reverse_lazy('inv:list-subitem-cap')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'Capacidad Rubro eliminado correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('inv:list-subitem-cap')
