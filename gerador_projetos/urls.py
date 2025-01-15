from django.contrib import admin
from django.urls import path
from preenchimento import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dispensa/', views.dispensa_form, name='dispensa_form'),
]
