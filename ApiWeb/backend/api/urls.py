from django.urls import path
from .views import autenticacion


urlpatterns = [
    path('AUT', autenticacion ),
 
]