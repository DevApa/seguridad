import datetime

import xlwt
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from inventory.models import ItemAssigmentHardwareDetail, Heading,ItemAssignmentHeader,SoftwareDetail
from inventory.forms import ItemAssigmentHardwareDetailForm
from django.http import JsonResponse, HttpResponse


def export_hw(request):
    response = HttpResponse(content_type='application/ms-excel')
    # decide file name
    response['Content-Disposition'] = 'attachment; filename=Reporte_Inventario_al_'+str(datetime.datetime.now())+'.xls'

    # creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    # adding sheet
    ws = wb.add_sheet("Detalle Equipo Hardware")
    ws_det_sw = wb.add_sheet("Detalle Software")
    # Sheet header, first row
    row_num = 0
    row_num_det_sw = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True

    # column header names, you can use your own headers here
    columns = ['UBICACION', 'EQUIPO', 'EMPLEADO ASIGNADO', 'TIPO', 'ITEM', 'SUBITEM', 'TECNOLOGIA', 'FRECUENCIA', 'CARACTERISTICA', 'MARCA', 'MODELO', 'GENERACION', 'CANTIDAD', 'CODIGO INVENTARIO', 'NUMERO SERIE', 'OBSERVACIONES'  ]
    columns_det_sw = ['UBICACION', 'EQUIPO', 'EMPLEADO ASIGNADO', 'TIPO','SOFTWARE', 'VERSION']
    # write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    for col_num in range(len(columns_det_sw)):
        ws_det_sw.write(row_num, col_num, columns_det_sw[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    # get your data, from database or from a text file...
    data = ItemAssigmentHardwareDetail.objects.filter(head__state=True).values_list('head__location__description', 'head__name_equipment', 'head__employee__lastname', 'type__description', 'item__description', 'heading__description', 'heading_detail__description', 'frequency__description', 'heading_capacity__value', 'brand__description', 'model__description', 'generation__description', 'quantity', 'code_inventory', 'num_serial', 'observation') # dummy method to fetch data.
    for my_row in data:
        row_num = row_num + 1

        for col_num in range(len(my_row)):
            ws.write(row_num, col_num, str(my_row[col_num]), font_style)

    data_det_sw = SoftwareDetail.objects.filter(head__state=True).values_list('head__location__description',
                                                                                    'head__name_equipment',
                                                                                    'head__employee__lastname',
                                                                                    'type__description',
                                                                                    'software__description',
                                                                                    'software__version'
                                                                                    )  # dummy method to fetch data.
    for my_row in data_det_sw:
        row_num_det_sw = row_num_det_sw + 1

        for col_num in range(len(my_row)):
            ws_det_sw.write(row_num_det_sw, col_num, str(my_row[col_num]), font_style)


    wb.save(response)
    return response

class ItemAssigmentHardwareDetailListView(ListView):
    model = ItemAssigmentHardwareDetail
    template_name = 'asignaciondethw/list.html'
    success_url = reverse_lazy('inv:list-assignment-hw')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Matenimiento Asignación Hardware'
        context['pageview'] = 'Asignación Hardware'
        context['object_list'] = ItemAssigmentHardwareDetail.objects.filter(state=True)
        context['create_url'] = reverse_lazy('inv:create-assignment-hw')
        context['url_list'] = reverse_lazy('inv:list-assignment-hw')
        return context


class ItemAssigmentHardwareDetailCreateView(CreateView):
    model = ItemAssigmentHardwareDetail
    form_class = ItemAssigmentHardwareDetailForm
    template_name = "asignaciondethw/create.html"
    success_url = reverse_lazy('inv:list-assignment-hw')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.form_class(request.POST)
                if form.is_valid():
                    form.save()
                    message = f'Asignación Hardware registrada correctamente'
                    error = 'No han ocurrido errores'
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 201
                    return response
                else:
                    message = f'Asignación Hardward no se pudo registrar!'
                    error = form.errors
                    response = JsonResponse({'message': message, 'error': error})
                    response.status_code = 400
                    return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Asignación Hardware'
        context['action'] = 'add'
        context['list_url'] = reverse_lazy('inv:list-assignment-hw')
        return context

class ItemAssigmentHardwareDetailUpdateView(UpdateView):
    model = ItemAssigmentHardwareDetail
    form_class = ItemAssigmentHardwareDetailForm
    template_name = "asignaciondethw/update.html"
    success_url = reverse_lazy('inv:list-assignment-hw')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
           if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = f'Asignación Hardware actualizado correctamente'
                error = 'No hay error'
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 201
                return response
            else:
                message = f'Asignación Hardware no se pudo actualizar!'
                error = form.errors
                response = JsonResponse({'message': message, 'error': error})
                response.status_code = 400
                return response
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Asignación Hardware'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('inv:list-assignment-hw')
        return context


class ItemAssigmentHardwareDetailDeleteView(DeleteView):
    model = ItemAssigmentHardwareDetail
    success_url = reverse_lazy('inv:list-assignment-hw')

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            obj = self.get_object()
            obj.state = False
            obj.save()
            message = f'Asignación Hardware eliminado correctamente!'
            errors = 'No se encontraron errores'
            response = JsonResponse({'message': message, 'error': errors})
            response.status_code = 201
            return response
        else:
            return redirect('inv:list-assignment-hw')
