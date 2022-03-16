from django.forms import *

from inventory.models import *


class TypeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Tipo
        fields = ['name', 'description']

        labels = {
            'name': 'Nombre',
            'description': 'Descripción'
        }

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
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
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Frequency
        fields = ['name', 'description']

        labels = {
            'name': 'Nombre',
            'description': 'Descripción'
        }

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Defina aquí el frecuencia'}),
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
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Brand
        fields = ['name', 'description']

        labels = {
            'name': 'Nombre',
            'description': 'Descripción'
        }

        widgets = {
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
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = EModel
        fields = ['name', 'description']

        labels = {
            'name': 'Nombre',
            'description': 'Descripción'
        }

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Defina aquí el modelo'}),
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
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Location
        fields = ['name', 'description']

        labels = {
            'name': 'Nombre',
            'description': 'Descripción'
        }

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Defina aquí la ubicación'}),
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

        labels = {
            'name': 'Nombre',
            'description': 'Descripción'
        }

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
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Software
        fields = ['name', 'description', 'version']

        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'version': 'Versión'
        }

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descrpción'}),
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
        self.fields['item'].queryset = Tipo.objects.filter(state=True)

    class Meta:
        model = Heading
        fields = ['item', 'name', 'description']

        labels = {
            'item': 'Item',
            'name': 'Nombre',
            'description': 'Descripción'
        }

        widgets = {
            'item': Select(attrs={'class': 'form-control select2'}),
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'})
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
        self.fields['type'].widget.attrs['autofocus'] = True
        self.fields['type'].empty_label = 'Seleccione un tipo...!'
        self.fields['type'].queryset = Tipo.objects.all()
        self.fields['model'].empty_label = 'Seleccione un modelo..!'

    class Meta:
        model = Item
        fields = ['name', 'description']

        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
        }

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
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