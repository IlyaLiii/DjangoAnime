from django.contrib.auth.models import User
from django.core import validators
from django.forms import ModelForm, Select, forms, DecimalField, ModelChoiceField, CharField, NumberInput, IntegerField, \
    SlugField, ModelMultipleChoiceField, ImageField, widgets
from .models import Anime_title, Genres, Img
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class Anime_title_form_for_user(ModelForm):
    class Meta:
        model = Anime_title
        fields = ('name_ru',)
        labels = {'name_ru': 'Имя тайтла'}
        help_texts = {'name_ru': ' - Укажи имя тайтла'}
        # widgets = {'name_ru': Select(attrs={'size': 100, 'color': 'yellow'})}

# несрочное TODO: Сделать красивую форму, а то жанры через CTRL жать - такое себе
class Add_Anime_title(ModelForm):
    name_ru = CharField(label='Имя на русском', max_length=250)
    rating = IntegerField(label='Рейтинг', min_value=1, max_value=10)
    genres = ModelMultipleChoiceField(queryset=Genres.objects.all(),
                                      label='Жанры',
                                      help_text='Укажите жанры через CTRL',
                                      required=False)
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(
            attrs={
                'data-theme': 'dark',
                # 'data-size': 'compact',
            }
        )
    )

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


class ImgForm(ModelForm):
    img = ImageField(label='Изображение',
                     validators=[validators.FileExtensionValidator(
                         allowed_extensions=('gif', 'jpg', 'png'))],
                     error_messages={
                         'invalid': 'Ошибка сервера',
                         'invalid_extension': 'Этот формат не поддерживается',
                         'missing': 'Файл не заружен по какой-то причине',
                         'invalid_image': 'Файл поврежден',
                         'empty': 'Загружен пустой файл'
                     })
    desc = CharField(label='Описание',
                     widget=widgets.Textarea())

    class Meta:
        model = Img
        fields = '__all__'
