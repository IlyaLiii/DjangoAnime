from django.contrib.auth.models import User
from django.forms import ModelForm, Select, forms, DecimalField, ModelChoiceField, CharField, NumberInput, IntegerField, \
    SlugField, ModelMultipleChoiceField
from .models import Anime_title, Genres
from captcha.fields import CaptchaField


class Anime_title_form_for_user(ModelForm):
    class Meta:
        model = Anime_title
        fields = ('name_ru',)
        labels = {'name_ru': 'Имя тайтла'}
        help_texts = {'name_ru': ' - Укажи имя тайтла'}
        # widgets = {'name_ru': Select(attrs={'size': 100, 'color': 'yellow'})}




class AddAnime_title(ModelForm):
    name_ru = CharField(label='Имя на русском', max_length=250)
    rating = IntegerField(label='Рейтинг', min_value=1, max_value=10)
    genres = ModelMultipleChoiceField(queryset=Genres.objects.all(),
                                      label='Жанры',
                                      help_text='Укажите жанры',
                                      required=False)
    captcha = CaptchaField(label='Введите текст с картинки:',
                                   error_messages={'invalid': 'Неправильный текст'})

    class Meta:
        model = Anime_title
        fields = ('name_ru', 'rating', 'genres')


class RegisterUserForm(ModelForm):
    password1 = CharField(label='Пароль')
    password2 = CharField(label='Пароль (повторно)')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password1', 'first_name', 'last_name')


class SearchForm(forms.Form):
    keyword = CharField(max_length=30, label='Искомое слово')
    # genres = ModelChoiceField(queryset=Genres.objects.all(),
    #                           label='Жанры')
