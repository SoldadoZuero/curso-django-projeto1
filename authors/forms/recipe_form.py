from django import forms
from recipes.models import Recipe
from utils.django_forms import add_attr


class AuthorRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_attr(self.fields.get('preparation_steps'), 'class', 'span-2')

    class Meta:
        model = Recipe
        fields = 'title', 'description', 'category', 'preparation_time', \
            'preparation_time_unit', 'servings', 'servings_unit', \
            'preparation_steps', 'cover', 'slug',

        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'class': 'span-2'
                },
            ),
            'servings_unit': forms.Select(
                choices=(
                    ('Porções', 'Porções',),
                    ('Pessoas', 'Pessoas',),
                ),
            ),
            'preparation_time_unit': forms.Select(
                choices=(
                    ('Minutos', 'Minutos',),
                    ('Horas', 'Horas',),
                ),
            ),
            'slug': forms.SlugField(),
        }
