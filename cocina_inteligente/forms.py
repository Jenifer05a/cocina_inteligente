from django import forms
from .models import Platillo
from django.core import validators


class PlatilloForm(forms.ModelForm):

    class Meta:

        model = Platillo

        fields = '__all__'

        widgets = {

            'nombre': forms.TextInput(attrs={

                'class': 'form-control',

                'placeholder': 'Ingresa el nombre del platillo'

            }),

            'descripcion': forms.Textarea(attrs={

                'class': 'form-control',

                'placeholder': 'Ingresa la descripción del platillo',

                'rows': 4

            }),

            'precio': forms.NumberInput(attrs={

                'class': 'form-control',

                'placeholder': 'Ingresa el precio'

            }),

            'categoria': forms.Select(attrs={

                'class': 'form-control'

            }),

            'disponible': forms.CheckboxInput(attrs={

                'class': 'form-check-input'

            }),

            'imagen': forms.ClearableFileInput(attrs={

                'class': 'form-control'

            }),

        }

        labels = {

            'nombre': 'Nombre',

            'descripcion': 'Descripción',

            'precio': 'Precio',

            'categoria': 'Categoría',

            'disponible': '¿Disponible?',

            'imagen': 'Imagen'

        }

    def clean_nombre(self):

        nombre = self.cleaned_data['nombre']

        if len(nombre) < 3:

            raise forms.ValidationError(
                "El nombre es muy corto"
            )

        return nombre