from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plot', views.plot_scatter),
    path('upload', views.upload_file,name="upload")
]
