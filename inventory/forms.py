from django.forms import *

from inventory.models import *

class TypeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['autofocus'] = True

    class Meta:
        model = Type
        fields = [ 'description']

        widgets = {
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del tipo de item'})
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class FrequencyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['autofocus'] = True

    class Meta:
        model = Frequency
        fields = {'description'}
        labels = {'description' : 'Descripcion' }
        widgets = {
            #'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Defina aquí el frecuencia'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class TechnologyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Frequency
        fields = ['name', 'description']

        labels = {
            'name': 'Nombre',
            'description': 'Descripción'
        }

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Defina aquí el Tecnología'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class BrandForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['autofocus'] = True

    class Meta:
        model = Brand
        fields = ['description']

        widgets = {
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class EModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['autofocus'] = True

    class Meta:
        model = EModel
        fields = ['description']

        widgets = {
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class LocationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departament'].widget.attrs['autofocus'] = True
        self.fields['departament'].empty_label = 'Seleccione un departamento...!'

    class Meta:
        model = Location
        fields = ['departament', 'description']
        labels = {'departament':'Departamento', 'description':'Descripcion'}
        widgets = {
            'departament': Select(attrs={'class': 'form-control select2'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class GenerationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['autofocus'] = True

    class Meta:
        model = Generation
        fields = ['description']

        widgets = {
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class SoftwareForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['autofocus'] = True

    class Meta:
        model = Software
        fields = [ 'description', 'version']

        labels = {
            'description': 'Descripción',
            'version': 'Versión'
        }

        widgets = {
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Defina aquí el software'}),
            'version': TextInput(attrs={'class': 'form-control', 'placeholder': 'Versión del software'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class HeadingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].widget.attrs['autofocus'] = True
        self.fields['item'].empty_label = 'Seleccione un item...!'
        self.fields['item'].queryset = Item.objects.filter(state=True)

    class Meta:
        model = Heading
        fields = ['item', 'description']

        widgets = {
            'item': Select(attrs={'class': 'form-control select2'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Versión del software'})
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class HeadingDetailForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['heading'].widget.attrs['autofocus'] = True
        self.fields['heading'].empty_label = 'Seleccione un rubro...!'
        self.fields['heading'].queryset = Heading.objects.filter(state=True)

    class Meta:
        model = HeadingDetail
        fields = ['heading', 'description']

        widgets = {
            'heading': Select(attrs={'class': 'form-control select2'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Versión del software'})
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class HeadingCapacityForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['heading'].widget.attrs['autofocus'] = True
        self.fields['heading'].empty_label = 'Seleccione un rubro...!'
        self.fields['heading'].queryset = Heading.objects.filter(state=True)

    class Meta:
        model = HeadingCapacity
        fields = ['heading', 'value']

        widgets = {
            'heading': Select(attrs={'class': 'form-control select2'}),
            'value': TextInput(attrs={'class': 'form-control', 'placeholder': 'Versión del software'})
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['autofocus'] = True


    class Meta:
        model = Item
        fields = ['description']

        labels = {
            'description': 'Descripción',
        }

        widgets = {
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción del item'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ItemAssignmentHeaderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].widget.attrs['autofocus'] = True
        self.fields['employee'].empty_label = 'Seleccione un Empleado...!'
        self.fields['location'].empty_label = 'Seleccione una Ubicacion...!'

    class Meta:
        model = ItemAssignmentHeader
        fields = ['employee', 'name_equipment', 'location']
        labels = {'employee': 'Empleado', 'name_equipment':'Equipo', 'location':'Ubicacion'}
        widgets = {
            'employee': Select(attrs={'class': 'form-control select2'}),
            'name_equipment': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del equipo'}),
            'location': Select(attrs={'class': 'form-control select2'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ItemAssigmentHardwareDetailForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['head'].widget.attrs['autofocus'] = True
        self.fields['head'].empty_label = 'Seleccione un Equipo...!'
        self.fields['head'].queryset = ItemAssignmentHeader.objects.filter(state=True)
        self.fields['type'].empty_label = 'Seleccione un Tipo...!'
        self.fields['type'].queryset = Type.objects.filter(state=True)
        self.fields['item'].empty_label = 'Seleccione un Item...!'
        self.fields['item'].queryset = Item.objects.filter(state=True)
        self.fields['brand'].empty_label = 'Seleccione una Marca...!'
        self.fields['brand'].queryset = Brand.objects.filter(state=True)
        self.fields['model'].empty_label = 'Seleccione una Modelo...!'
        self.fields['model'].queryset = EModel.objects.filter(state=True)
        self.fields['heading'].empty_label = 'Seleccione una Caracteristica...!'
        self.fields['heading'].queryset = Heading.objects.filter(state=True)
        self.fields['heading_detail'].empty_label = 'Seleccione una Tecnologia...!'
        self.fields['heading_detail'].queryset = HeadingDetail.objects.filter(state=True)
        self.fields['frequency'].empty_label = 'Seleccione una Frecuencia...!'
        self.fields['frequency'].queryset = Frequency.objects.filter(state=True)
        self.fields['heading_capacity'].empty_label = 'Seleccione una Capacidad...!'
        self.fields['heading_capacity'].queryset = HeadingCapacity.objects.filter(state=True)
        self.fields['generation'].empty_label = 'Seleccione una Generacion...!'
        self.fields['generation'].queryset = Generation.objects.filter(state=True)

    class Meta:
        model = ItemAssigmentHardwareDetail
        fields = ['head',
                  'item',
                  'type',
                  'brand',
                  'model',
                  'heading',
                  'heading_detail',
                  'frequency',
                  'heading_capacity',
                  'generation',
                  'code_inventory',
                  'num_serial',
                  'quantity',
                  'observation',
                  ]
        labels = {'head':'Equipo',
                  'item':'Item',
                  'type':'Tipo',
                  'brand':'Marca',
                  'model':'Modelo',
                  'heading':'Caracteristica',
                  'heading_detail': 'Teconologia',
                  'frequency':'Frecuencia',
                  'heading_capacity':'Capacidad',
                  'generation':'Generacion',
                  'code_inventory':'Codigo Inventario',
                  'num_serial':'Numero Serie',
                  'quantity': 'Cantidad',
                  'observation':'Observacion',
                  }

        widgets = {
            'head': Select(attrs={'class': 'form-control select2'}),
            'item': Select(attrs={'class': 'form-control select2'}),
            'type': Select(attrs={'class': 'form-control select2'}),
            'brand': Select(attrs={'class': 'form-control select2'}),
            'model': Select(attrs={'class': 'form-control select2'}),
            'heading':Select(attrs={'class': 'form-control select2'}),
            'heading_detail': Select(attrs={'class': 'form-control select2'}),
            'frequency': Select(attrs={'class': 'form-control select2'}),
            'heading_capacity': Select(attrs={'class': 'form-control select2'}),
            'generation': Select(attrs={'class': 'form-control select2'}),
            'code_inventory': TextInput(attrs={'class': 'form-control', 'placeholder': 'Codigo Inventario'}),
            'num_serial': TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero de Serie'}),
            'quantity': TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
            'observation': TextInput(attrs={'class': 'form-control', 'placeholder': 'Observacion'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class SoftwareDetailForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['head'].widget.attrs['autofocus'] = True
        self.fields['head'].empty_label = 'Seleccione un Equipo...!'
        self.fields['software'].empty_label = 'Seleccione Software...!'
        self.fields['type'].empty_label = 'Seleccione un Tipo...!'

    class Meta:
        model = SoftwareDetail
        fields = [
                  'head',
                  'software',
                  'type',
                  ]
        labels = {
                  'head':'Equipo',
                  'software':'Software',
                  'type':'Tipo',
                  }

        widgets = {
            'head': Select(attrs={'class': 'form-control select2'}),
            'software': Select(attrs={'class': 'form-control select2'}),
            'type': Select(attrs={'class': 'form-control select2'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data