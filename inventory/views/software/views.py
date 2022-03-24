from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import Software
from inventory.forms import SoftwareForm
from django.http import JsonResponse


class SoftwareListView(ListView):
    model = Software
    template_name = 'software/list.html'
    success_url = reverse_lazy('inv:list-soft')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Software'
        context['pageview'] = 'Software'
        context['object_list'] = Software.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-soft')
        context['url_list'] = reverse_lazy('inv:list-soft')
        return context


class SoftwareCreateView(CreateView):
    model = Software
    form_class = SoftwareForm
    template_name = "software/create.html"
    success_url = reverse_lazy('inv:list-soft')
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Software registrado correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Software no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Software'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-soft')
        return context
    

class SoftwareUpdateView(UpdateView):
    model = Software
    form_class = SoftwareForm
    template_name = "software/update.html"
    success_url = reverse_lazy('inv:list-soft')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
           if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = f'{self.model.__name__} actualizado correctamente'
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
        context['title'] = 'Actualizar Software'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inv:list-soft')
        return context


class SoftwareDeleteView(DeleteView):
    model = Software
    success_url = reverse_lazy('inv:list-soft')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'{self.model.__name__} eliminado correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('inv:list-soft')
