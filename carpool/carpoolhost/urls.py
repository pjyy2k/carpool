from django.urls import path
from carpoolhost import views


urlpatterns = [
    path('',views.index,name='index'),
    path('lists/', views.HostListView.as_view(),name='lists'),
]