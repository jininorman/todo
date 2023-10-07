from django.urls import path
from . import views


urlpatterns=[
path("",views.add,name='add'),
path("update/<int:id>/",views.update,name='update'),
path("delete/<int:taskid>/", views.delete, name='delete'),
path("searchdata", views.searchdata, name='searchdata'),

]