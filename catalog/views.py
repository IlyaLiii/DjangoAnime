from django.http import HttpResponse, Http404, HttpResponseRedirect, \
    StreamingHttpResponse, FileResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views.generic.list import ListView
# from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from catalog.models import Anime_title, Genres, Img
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
from .forms import Anime_title_form_for_user, SearchForm, Add_Anime_title, ImgForm
from django.urls import reverse_lazy, resolve
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from random import randint

from .serializers import GenresSerializer


class IndexView(generic.ListView):
    template_name = 'catalog/index.html'
    context_object_name = 'latest_anime_title_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Anime_title.objects.order_by('-pub_date')[:10]
    # TODO: это метод должен по идее возвращать в 'current_title' аниме по айди, но как я понял это метод для функции detail
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     print(**kwargs)
    #     context = super().get_context_data(**kwargs)
    #     # context['rubrics'] = Rubric.objects.all()
    #     context['current_title'] = Anime_title.objects.get(pk=self.kwargs['anime_id'])
    #     return context


class Genre_search(ListView):
    template_name = 'catalog/genre_search.html'
    context_object_name = 'genres'

    def get_queryset(self):
        return Anime_title.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genres.objects.all()
        return context


# Переопределение функции в класс, чтобы было круче
@require_http_methods(['GET'])
def detail(request, anime_id):
    # print(request.GET)
    data = get_object_or_404(Anime_title, pk=anime_id)
    return render(request, 'catalog/detail.html', {'data': data})


# TODO: у меня нихуя не получается , я тупой нахуй как пробка
# #
# class Anime_title_detailView(SingleObjectMixin, ListView):
#     template_name = 'catalog/index.html'
#     pk_url_kwarg = 'anime_id'
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=Anime_title.objects.all())
#         return super().get(request, *args, **kwargs)
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['current_title'] = self.object
#         context['data'] = context['object_list']
#         return context
#     def get_queryset(self):
#           return Anime_title.objects.all()
def genre_titles(request, genre_id):
    data = Anime_title.objects.filter(genre=genre_id)
    return render(request, 'catalog/genre_titles.html', {'data': data})


@login_required
def top(request, ):
    data = Anime_title.objects.order_by('-rating')[:100]
    return render(request, 'catalog/top.html', {'data': data})


def index2(request):
    response = HttpResponse('Здвесь будет',
                            content_type='text/plain; charset=utf-8')
    response.write(' главная')
    response.writelines((' страница', ' сайта'))
    # response['keywords'] = 'Python, Django'
    response.write(' Python Django')
    return response


def tryindex(request):
    filename = r'E:\photo\pPKmQED_mb8.jpg'
    return FileResponse(open(filename, 'rb'))  # as_attachment=True чтоб сохранить файл)


def tryindex2(request):
    data = {'foo': 'bar'}
    return JsonResponse(data)


def random_title(request):
    data = Anime_title.objects.all()
    title = randint(0, len(data))
    context = Anime_title.objects.get(pk=title)
    return redirect('/catalog/' + str(title), {'data': context})


# Todo: Добавить корректные декораторы к этой функции, изменить форму, а то она некрасивая) и по возможности через bootstrap. Пофиксиить формы, есть форма Anime_title_form_for_user, а есть Add_Anime_title (понять какая лучше и чо зачем и почему)
class Anime_t_create_view(CreateView):
    template_name = 'catalog/create.html'
    form_class = Anime_title_form_for_user
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Anime_title'] = Anime_title.objects.all()
        return context


# TODO: Аналог нормальной формы, нужно потесить
def Anime_t_create(request):
    if request.method == 'POST':
        anime_form = Add_Anime_title(request.POST)
        if anime_form.is_valid():
            anime_form.save()
            return HttpResponseRedirect(reverse('catalog:index'))
        else:
            context = {'form': anime_form}
            return render(request, 'catalog/create.html', context)
    else:
        anime_form = Add_Anime_title()
        context = {'form': anime_form}
        return render(request, 'catalog/create.html', context)


def title_search(request):
    if request.method == 'POST':
        sf = SearchForm(request.POST)
        if sf.is_valid():
            keyword = sf.cleaned_data['keyword'].capitalize()
            # genre_id = sf.cleaned_data['genre'].pk
            anime_titles = Anime_title.objects.filter(name_ru__icontains=keyword, )
            # genre=genre_id)
            data = {'data': anime_titles}
            return render(request, 'catalog/search_results.html', data)
    else:
        sf = SearchForm()
        context = {'form': sf}
        return render(request, 'catalog/search.html', context)


def add_img(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:index')
        else:
            context = {'form': form}
            return render(request, 'catalog/add_img.html', context)
    else:
        form = ImgForm()
        context = {'form': form}
        return render(request, 'catalog/add_img.html', context)


# api_restwramework

@api_view(['GET', 'POST'])
def api_genres(request):
    if request.method == 'GET':
        genres = Genres.objects.all()
        serializer = GenresSerializer(genres, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GenresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_genres_detail(request, pk):
    genre = Genres.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = GenresSerializer(genre)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = GenresSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
