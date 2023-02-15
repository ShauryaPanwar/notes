from django.urls import path
from . import views

urlpatterns=[
    path('',views.getRoutes),
    path('notes/',views.getNotes),
    path('notes/create/',views.createnotes),
    path('notes/<str:pk>/',views.singleNotes),
    path('notes/<str:pk>/update/',views.updatenotes),
    path('notes/<str:pk>/delete/',views.deletenotes),
]