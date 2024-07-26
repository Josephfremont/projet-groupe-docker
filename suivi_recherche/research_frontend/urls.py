from django.urls import path
from . import views

app_name = 'research_frontend'

urlpatterns = [
    path('', views.index, name='home'),
    path('researches/', views.researches, name='researches'),
    path('researchers/', views.researchers, name='researchers'),
    path('publications/', views.publications, name='publications'),
    path('research/<int:id>/', views.research, name='research'),
    path('researcher/<int:id>/', views.researcher, name='researcher'),
    path('publication/<int:id>/', views.publication, name='publication'),
    path('delete_research/<int:id>/', views.delete_research, name='delete_research'),
    path('delete_researcher/<int:id>/', views.delete_researcher, name='delete_researcher'),
    path('delete_publication/<int:id>/', views.delete_publication, name='delete_publication'),
    path('create_research/', views.create_research, name='create_research'),
    path('create_researcher/', views.create_researcher, name='create_researcher'),
    path('create_publication/', views.create_publication, name='create_publication'),
    path('update_research/<int:id>/', views.update_research, name='update_research'),
    path('update_researcher/<int:id>/', views.update_researcher, name='update_researcher'),
    path('update_publication/<int:id>/', views.update_publication, name='update_publication'),
    path('filter/', views.filter, name='filter'),
    path('visualization/', views.visualization, name='visualization'),
    path('chatbot/', views.chatbot, name='chatbot'),
]
