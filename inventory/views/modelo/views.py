from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import EModel
from inventory.forms import EModelForm
from django.http import JsonResponse


class EModelListView(ListView):
    model = EModel
    template_name = 'modelo/list.html'
    success_url = reverse_lazy('inv:list-model')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Módelo'
        context['pageview'] = 'Módelo'
        context['object_list'] = EModel.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-model')
        context['url_list'] = reverse_lazy('inv:list-model')
        return context


class EModelCreateView(CreateView):
    model = EModel
    form_class = EModelForm
    template_name = "modelo/create.html"
    success_url = reverse_lazy('inv:list-model')
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Módelo registrado correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Módelo no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Módelo'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-model')
        return context
    

class EModelUpdateView(UpdateView):
    model = EModel
    form_class = EModelForm
    template_name = "modelo/update.html"
    success_url = reverse_lazy('inv:list-model')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
           if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = f'Módelo actualizado correctamente'
                error = 'No hay error'
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 201
                return response
            else:
                message = f'Módelo no se pudo actualizar!'
                error = form.errors
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 400
                return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Módelo'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inv:list-model')
        return context


class EModelDeleteView(DeleteView):
    model = EModel
    success_url = reverse_lazy('inv:list-model')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'Módelo eliminado correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('inv:list-model')
