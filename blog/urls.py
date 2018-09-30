from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]

### learning, my initial typo was '<int:blog_id/', just missed ">"

#urlpatterns = [
#    path('', views.allblogs, name='allblogs'),
#    path('<int:blog_id/', views.detail, name='detail'),
#]