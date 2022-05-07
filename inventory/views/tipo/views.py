from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import Type
from inventory.forms import TypeForm
from django.http import JsonResponse


class TypeListView(ListView):
    model = Type
    template_name = 'tipo/list.html'
    success_url = reverse_lazy('inv:list-type')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Tipo.objects.filter(state=True):
                    data.append(i.to_json())
            else:
                data['error'] = 'Se ha presentado un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Tipos'
        context['pageview'] = 'Tipo'
        context['object_list'] = Type.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-type')
        context['url_list'] = reverse_lazy('inv:list-type')
        return context


class TypeCreateView(CreateView):
    model = Type
    form_class = TypeForm
    template_name = "tipo/create.html"
    success_url = reverse_lazy('inv:list-type')
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Tipo registrado correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Tipo no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Tipo'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-type')
        return context
    

class TypeUpdateView(UpdateView):
    model = Type
    form_class = TypeForm
    template_name = "tipo/update.html"
    success_url = reverse_lazy('inv:list-type')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
           if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = f'Tipo actualizado correctamente'
                error = 'No hay error'
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 201
                return response
            else:
                message = f'Tipo no se pudo actualizar!'
                error = form.errors
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 400
                return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Tipo'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inv:list-type')
        return context


class TypeDeleteView(DeleteView):
    model = Type
    success_url = reverse_lazy('inv:list-type')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'Tipo eliminada correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('inv:list-type')
