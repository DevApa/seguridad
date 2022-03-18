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
        self.fields['code'].widget.attrs['autofocus'] = True

    class Meta:
        model = Brand
        fields = ['code', 'name', 'description']

        widgets = {
            'code': TextInput(attrs={'class': 'form-control', 'placeholder': 'Código'}),
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Marca'}),
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
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Generation
        fields = ['name', 'description']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Defina aquí la generación'}),
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