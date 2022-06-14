from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from requests import request
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, FormView
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

class MenHome(DataMixin, ListView):
    model = Men
    template_name = 'men/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        def_import = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(def_import.items()))

    def get_queryset(self):
        return Men.objects.filter(is_published = True).select_related('category')

class About(DataMixin, ListView):
    model = Men
    template_name = 'men/about.html'

    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_user_context(**kwargs)
        def_import7 = self.get_user_context(title='О сайте')
        return dict(list(context.items()) + list(def_import7.items()))

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm 
    template_name = 'men/addpage.html'
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        def_import1 = self.get_user_context(title='Добавить статью')
        return dict(list(context.items()) + list(def_import1.items()))

def category(request, catid):
    print(request.POST)
    return HttpResponse(f"Категории<p>{catid}</p>")

def archive(request, year):
    if int(year) > 2022:
        return redirect('home') 

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class ShowPost(DataMixin, DetailView):
    model = Men
    template_name = 'men/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        def_import2 = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(def_import2.items()))

class MenCategory(DataMixin, ListView):
    model = Men 
    template_name = 'men/index.html'
    context_object_name = 'public'
    allow_empty = False
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['category_slug'])
        def_import3 = self.get_user_context(title='Категория - ' + str(c.name), category_selected=c.pk)
        return dict(list(context.items()) + list(def_import3.items()))
    
    def get_queryset(self):
        return Men.objects.filter(category__slug = self.kwargs['category_slug'], is_published=True).select_related('category')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'men/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_user_context(**kwargs)
        def_import4 = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(def_import4.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'men/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_user_context(**kwargs)
        def_import5 = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(def_import5.items()))

    def get_success_url(self): 
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

class Contact(DataMixin, ListView):
    model = Men
    template_name = 'men/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_user_context(**kwargs)
        def_import6 = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(def_import6.items()))
