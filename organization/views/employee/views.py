from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from organization.models import Employee
from organization.forms import EmployeeForm
from django.http import JsonResponse
from django.contrib import messages


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/list.html'
    success_url = reverse_lazy('org:emp-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Empleado'
        context['pageview'] = 'Empleado'
        context['object_list'] = Employee.objects.filter(state=True)
        context['create_url'] = reverse_lazy('org:emp-create')
        context['url_list'] = reverse_lazy('org:emp-list')
        return context


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/create.html'
    success_url = reverse_lazy('org:emp-list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            identificacion = request.POST['identification']
            if not verificar(identificacion):
                message = f'El número de identificación es inválida!'
                error = ''
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 400
                return response

            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Empleado registrado correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Empleado no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Empleado'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('org:emp-list')
        return context


def verificar(nro):
    l = len(nro)
    if l == 10 or l == 13:  # verificar la longitud correcta
        cp = int(nro[0:2])
        if 1 <= cp <= 24:  # verificar codigo de provincia
            tercer_dig = int(nro[2])
            if 0 <= tercer_dig < 6:  # numeros enter 0 y 6
                if l == 10:
                    return __validar_ced_ruc(nro, 0)
                elif l == 13:
                    return __validar_ced_ruc(nro, 0) and nro[
                                                         10:13] == '001'  # se verifica que los ultimos numeros sean 001
            elif tercer_dig == 6:
                return __validar_ced_ruc(nro, 1) and nro[10:13] == '001'  # sociedades publicas
            elif tercer_dig == 9:  # si es ruc
                return __validar_ced_ruc(nro, 2) and nro[10:13] == '001'  # sociedades privadas
            else:
                return False
        else:
            return False
    else:
        return False


def __validar_ced_ruc(nro, tipo):
    total = 0
    if tipo == 0:  # cedula y r.u.c persona natural
        base = 10
        d_ver = int(nro[9])  # digito verificador
        multip = (2, 1, 2, 1, 2, 1, 2, 1, 2)
    elif tipo == 1:  # r.u.c. publicos
        base = 11
        d_ver = int(nro[8])
        multip = (3, 2, 7, 6, 5, 4, 3, 2)
    elif tipo == 2:  # r.u.c. juridicos y extranjeros sin cedula
        base = 11
        d_ver = int(nro[9])
        multip = (4, 3, 2, 7, 6, 5, 4, 3, 2)
    for i in range(0, len(multip)):
        p = int(nro[i]) * multip[i]
        if tipo == 0:
            total += p if p < 10 else int(str(p)[0]) + int(str(p)[1])
        else:
            total += p
    mod = total % base
    val = base - mod if mod != 0 else 0
    return val == d_ver

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/update.html'
    success_url = reverse_lazy('org:emp-list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:

            identificacion = request.POST['identification']
            if not verificar(identificacion):
                message = f'El número de identificación es inválida!'
                error = ''
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 400
                return response

            if request.is_ajax():
                form = self.form_class(request.POST, instance=self.get_object())
                if form.is_valid():
                    form.save()
                    message = f'Empleado actualizado correctamente'
                    error = 'No hay error'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Empleado no se pudo actualizar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Empleado'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('org:emp-list')
        return context


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('org:emp-list')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'Empleado eliminado correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('org:emp-list')
