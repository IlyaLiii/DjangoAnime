from django.contrib import admin
from .models import Anime_title, Genres


class Anime_title_admin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_eng', 'rating', 'status', 'num_of_episodes')
    list_display_links = ('name_ru', 'status', 'num_of_episodes')
    search_fields = ('name_ru', 'rating', 'status')


admin.site.register(
    Anime_title, Anime_title_admin,
)
admin.site.register(
    Genres,
)
