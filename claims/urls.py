from django.urls import path

from . import views

app_name='claims'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>',views.details , name='claim_detail'),
    path('add/', views.newclaim, name='add'),
    
]
