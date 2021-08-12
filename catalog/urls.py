from django.urls import path
from .views import *
# from anime.settings import DEBUG
# from django.contrib.staticfiles.views import serve
# from django.views.decorators.cache import never_cache

app_name = 'catalog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:anime_id>/', detail, name='detail'),
    path('random_title/', random_title, name='random_title'),
    path('genre_search/', Genre_search.as_view(), name='genre_search'),
    path('title_search/', title_search, name='title_search'),
    path('genre_search/<int:genre_id>/', genre_titles, name='genre_titles'),
    path('top/', top, name='top'),
    # path('add/', Anime_t_create_view.as_view(), name='add'),
    path('index2/', index2, name='index2'),
    path('tryindex/', tryindex, name='tryindex'),
    path('tryindex2/', tryindex2, name='tryindex2'),
    # path('<int:anime_id>/', Anime_title_detailView.as_view(), name='detail'),
    path('add/', Anime_t_create, name='add'),
    path('add_img/', add_img, name='add_img'),
]
# if DEBUG:
#     urlpatterns.append(path('static/<path:path>', never_cache(serve)))
