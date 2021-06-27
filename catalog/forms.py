from django.contrib.auth.models import User
from django.forms import ModelForm, Select, forms, DecimalField, ModelChoiceField, CharField
from .models import Anime_title, Genres


class Anime_title_form_for_user(ModelForm):
    class Meta:
        model = Anime_title
        fields = ('name_ru',)
        labels = {'name_ru': 'Имя тайтла'}
        help_texts = {'name_ru': ' - Укажи имя тайтла'}
        # widgets = {'name_ru': Select(attrs={'size': 100, 'color': 'yellow'})}


class AddAnime_title(ModelForm):
    name_ru = CharField(label='Имя на русском', max_length=250)
    rating = DecimalField(label='Рейтинг', decimal_places=2)
    genres = ModelChoiceField(queryset=Genres.objects.all(),
                              label='Жанры',
                              help_text='Укажите жанры',
                              required=False)

    class Meta:
        model = Anime_title
        fields = ('name_ru', 'rating', 'genres')


class RegisterUserForm(ModelForm):
    password1 = CharField(label='Пароль')
    password2 = CharField(label='Пароль (повторно)')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password1', 'first_name', 'last_name')
