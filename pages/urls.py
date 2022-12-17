from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('projects/', views.projects_page, name='projects'),
    path('projects/<int:pk>/', views.project),
    path('cv/', views.cv_page, name='cv'),
    path('contacts/', views.contacts_page, name='contacts')
]
