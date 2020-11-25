from django.urls import path
from . import views

urlpatterns = [
    path('state/', views.queryState, name='queryState'),
    path('state/<str:id>', views.queryState, name='queryState'),
    path('candidate/', views.queryCandidate, name='queryCandidate'),
    path('candidate/<str:id>', views.queryCandidate, name='queryCandidate'),
]
