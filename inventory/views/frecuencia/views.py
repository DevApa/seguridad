from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import Frequency
from inventory.forms import FrequencyForm
from django.http import JsonResponse


class FrequencyListView(ListView):
    model = Frequency
    template_name = 'frecuencia/list.html'
    success_url = reverse_lazy('inv:list-frequency')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Frequency.objects.all():
                    data.append(i.to_json())
            else:
                data['error'] = 'Se ha presentado un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Frecuencia'
        context['pageview'] = 'Frecuencia'
        context['object_list'] = Frequency.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-frequency')
        context['url_list'] = reverse_lazy('inv:list-frequency')
        return context


class FrequencyCreateView(CreateView):
    model = Frequency
    form_class = FrequencyForm
    template_name = "frecuencia/create.html"
    success_url = reverse_lazy('inv:list-frequency')
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Frecuencia registrada correctamente'
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
        context['title'] = 'Creación de Frecuencia'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-frequency')
        return context
    

class FrequencyUpdateView(UpdateView):
    model = Frequency
    form_class = FrequencyForm
    template_name = "frecuencia/update.html"
    success_url = reverse_lazy('inv:list-frequency')

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
        context['title'] = 'Actualizar Frecuencia'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inv:list-frequency')
        return context


class FrequencyDeleteView(DeleteView):
    model = Frequency
    success_url = reverse_lazy('inv:list-frequency')

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
            return redirect('inv:list-frequency')
