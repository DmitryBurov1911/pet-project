from distutils import archive_util
from django.urls import path, re_path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(MenHome.as_view()), name='home'),
    path('about', About.as_view(), name='about'),
    path('addpage', AddPage.as_view(), name='addpage'), 
    path('category/<slug:category_slug>/', MenCategory.as_view(), name='category'), 
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/',  logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'), 
    path('contact/', Contact.as_view(), name='contact')
]