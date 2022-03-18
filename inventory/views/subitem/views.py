from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import Heading
from inventory.forms import HeadingForm
from django.http import JsonResponse


class HeadingListView(ListView):
    model = Heading
    template_name = 'subitem/list.html'
    success_url = reverse_lazy('inv:list-sub-item')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Rubros'
        context['pageview'] = 'Frecuencia'
        context['object_list'] = Heading.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-su-item')
        context['url_list'] = reverse_lazy('inv:list-sub-item')
        return context


class HeadingCreateView(CreateView):
    model = Heading
    form_class = HeadingForm
    template_name = "subitem/create.html"
    success_url = reverse_lazy('inv:list-sub-item')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Rubro registrado correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Rubro no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Rubro'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-sub-item')
        return context


class HeadingUpdateView(UpdateView):
    model = Heading
    form_class = HeadingForm
    template_name = "tipo/update.html"
    success_url = reverse_lazy('inv:list-sub-item')

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
        context['title'] = 'Actualizar Tipo'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inv:list-sub-item')
        return context


class HeadingDeleteView(DeleteView):
    model = Heading
    success_url = reverse_lazy('inv:list-sub-item')

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
            return redirect('inv:list-sub-item')
