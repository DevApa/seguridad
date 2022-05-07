from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import Location
from inventory.forms import LocationForm
from django.http import JsonResponse


class LocationListView(ListView):
    model = Location
    template_name = 'ubicacion/list.html'
    success_url = reverse_lazy('inv:list-location')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Ubicación'
        context['pageview'] = 'Ubicación'
        context['object_list'] = Location.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-location')
        context['url_list'] = reverse_lazy('inv:list-location')
        return context


class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = "ubicacion/create.html"
    success_url = reverse_lazy('inv:list-location')
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Ubicación registrada correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Ubicación no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Ubicación'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-location')
        return context
    

class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = "ubicacion/update.html"
    success_url = reverse_lazy('inv:list-location')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
           if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = f'Ubicación actualizado correctamente'
                error = 'No hay error'
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 201
                return response
            else:
                message = f'Ubicación no se pudo actualizar!'
                error = form.errors
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 400
                return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Ubicación'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inv:list-location')
        return context


class LocationDeleteView(DeleteView):
    model = Location
    success_url = reverse_lazy('inv:list-location')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'Ubicación eliminada correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('inv:list-location')
