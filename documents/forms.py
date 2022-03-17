from django.forms import *

from documents.models import Area, Category, DocumentType, LevelAccess, Document


class AreaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['state'].queryset = Area.objects.filter(state=True)
        self.fields['name'].required = True
        self.fields['description'].required = True

    class Meta:
        model = Area
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Defina aquí el Área'}),
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


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['state'].queryset = Category.objects.filter(state=True)
        self.fields['name'].required = True
        self.fields['description'].required = True

    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Defina aquí la categoría'}),
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


class DocumentTypeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['state'].queryset = DocumentType.objects.filter(state=True)
        self.fields['name'].required = True
        self.fields['description'].required = True

    class Meta:
        model = DocumentType
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Defina aquí el tipo de documento'}),
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


class LevelAccessForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['state'].queryset = LevelAccess.objects.filter(state=True)
        self.fields['name'].required = True
        self.fields['description'].required = True

    class Meta:
        model = LevelAccess
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Defina aquí el nivel de acceso'}),
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


class DocumentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Seleccione un categaría...!'
        self.fields['level_access'].empty_label = 'Seleccione un nivel de acceso..!'
        self.fields['documentType'].empty_label = 'Seleccione un tipo de documento..!'
        self.fields['area'].empty_label = 'Seleccione un área '
        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['state'].queryset = Document.objects.filter(state=True)
        self.fields['name'].required = True
        self.fields['description'].required = True

    class Meta:
        model = Document
        fields = ['area', 'documentType', 'category', 'level_access', 'name',
                  'description', 'electronicSignature', 'manualSignature', 'pathFile', 'state']

        labels = {
            'area': 'Área',
            'documentType': 'Tipo de documento',
            'category': 'Categoría',
            'level_access': 'Nivel Acceso',
            'name': 'Nombre',
            'description': 'Descripción',
            'electronicSignature': 'Firma Electrónica',
            'manualSignature': 'Firma Manual',
            'pathFile': 'Ruta Archivo',
            'state': 'Estado',
        }

        widgets = {
            'area': Select(attrs={'class': 'form-control select2'}),
            'documentType': Select(attrs={'class': 'form-control select2'}),
            'category': Select(attrs={'class': 'form-control select2'}),
            'level_access': Select(attrs={'class': 'form-control select2'}),
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Defina aquí el nombre del documento'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
            'electronicSignature': CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}),
            'manualSignature': CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}),
            'pathFile': FileInput(attrs={'class': 'form-control'}),
            'state': CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}),
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


