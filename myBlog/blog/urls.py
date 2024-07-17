from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wood/', views.wood, name='wood'),
    path('printing/', views.printing, name='printing'),
    path('electronics/', views.electronics, name='electronics'),
    # path('programming/', views.programming, name='programming'),
    path('others/', views.others, name='others'),
    # path('about/', views.about, name='about'),
]
