from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import Generation
from inventory.forms import GenerationForm
from django.http import JsonResponse


class GenerationListView(ListView):
    model = Generation
    template_name = 'generacion/list.html'
    success_url = reverse_lazy('inv:list-generation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Generacion'
        context['pageview'] = 'Generacion'
        context['object_list'] = Generation.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-generation')
        context['url_list'] = reverse_lazy('inv:list-generation')
        return context


class GenerationCreateView(CreateView):
    model = Generation
    form_class = GenerationForm
    template_name = "generacion/create.html"
    success_url = reverse_lazy('inv:list-generation')
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'{self.model.__name__} registrada correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'{self.model.__name__} no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Generacion'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-generation')
        return context
    

class GenerationUpdateView(UpdateView):
    model = Generation
    form_class = GenerationForm
    template_name = "generacion/update.html"
    success_url = reverse_lazy('inv:list-generation')

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
        context['title'] = 'Actualizar Generación'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inv:list-generation')
        return context


class GenerationDeleteView(DeleteView):
    model = Generation
    success_url = reverse_lazy('inv:list-generation')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'{self.model.__name__} eliminada correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('inv:list-generation')
