from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import Item
from inventory.forms import ItemForm
from django.http import JsonResponse


class ItemListView(ListView):
    model = Item
    template_name = 'item/list.html'
    success_url = reverse_lazy('inv:list-item')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Item'
        context['pageview'] = 'Item'
        context['object_list'] = Item.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-item')
        context['url_list'] = reverse_lazy('inv:list-item')
        return context


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = "item/create.html"
    success_url = reverse_lazy('inv:list-item')
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Item registrada correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Item no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Item'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-item')
        return context
    

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "item/update.html"
    success_url = reverse_lazy('inv:list-item')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
           if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = f'Item actualizado correctamente'
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
        context['title'] = 'Actualizar Item'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inv:list-item')
        return context


class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('inv:list-item')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'Item eliminado correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('inv:list-item')
