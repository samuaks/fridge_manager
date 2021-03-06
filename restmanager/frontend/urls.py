from . import views
from django.urls import path


# Defining URL endpoints and what views they use.
urlpatterns = [
    path('', views.floors, name="home"),
    path('floors', views.floors),
    path('floors/', views.floors),
    path('fridges', views.fridges),
    path('fridges/', views.fridges),
    path('api/json/', views.json_view),
    path('api/change_state/', views.change_state),
]
