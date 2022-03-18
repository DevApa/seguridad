from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from documents.models import Area
from documents.forms import AreaForm
from django.http import JsonResponse


class AreaListView(ListView):
    model = Area
    template_name = 'areas/list.html'
    success_url = reverse_lazy('docs:list-area')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Áreas'
        context['pageview'] = 'Áreas'
        context['object_list'] = Area.objects.filter(state=True)
        context['action'] = 'add'
        context['create_url'] = reverse_lazy('docs:create-area')
        context['url_list'] = reverse_lazy('docs:list-area')
        return context


class AreaCreateView(CreateView):
    model = Area
    form_class = AreaForm
    template_name = "areas/create.html"
    success_url = reverse_lazy('docs:list-area')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Área registrada correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Área no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Área'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('docs:list-area')
        return context


class AreaUpdateView(UpdateView):
    model = Area
    form_class = AreaForm
    template_name = "areas/update.html"
    success_url = reverse_lazy('docs:list-area')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST, instance=self.get_object())
                if form.is_valid():
                    form.save()
                    message = f'Área actualizado correctamente'
                    error = 'No hay error'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Área no se pudo actualizar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Área'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('docs:list-area')
        return context


class AreaDeleteView(DeleteView):
    model = Area
    success_url = reverse_lazy('docs:list-area')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'Área eliminada correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('docs:list-area')
