from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from organization.models import University
from organization.forms import UniversityForm
from django.http import JsonResponse


class UniversityListView(ListView):
    model = University
    template_name = 'universidad/list.html'
    success_url = reverse_lazy('org:uni-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Universidad'
        context['pageview'] = 'Universidad'
        context['object_list'] = University.objects.filter(state=True)
        context['create_url'] = reverse_lazy('org:uni-create')
        context['url_list'] = reverse_lazy('org:uni-list')
        return context


class UniversityCreateView(CreateView):
    model = University
    form_class = UniversityForm
    template_name = "universidad/create.html"
    success_url = reverse_lazy('org:uni-list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Universidad registrada correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Universidad no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Universidad'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('org:uni-list')
        return context


class UniversityUpdateView(UpdateView):
    model = University
    form_class = UniversityForm
    template_name = "universidad/update.html"
    success_url = reverse_lazy('org:uni-list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST, instance=self.get_object())
                if form.is_valid():
                    form.save()
                    message = f'Universidad actualizado correctamente'
                    error = 'No hay error'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Universidad no se pudo actualizar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Universidad'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('org:uni-list')
        return context


class UniversityDeleteView(DeleteView):
    model = University
    success_url = reverse_lazy('org:uni-list')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'Universidad eliminada correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('org:uni-list')
