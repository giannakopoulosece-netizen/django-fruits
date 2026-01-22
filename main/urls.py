from django.urls import path
from .views import home, page, fruit_detail

urlpatterns = [
    path('', home, name='home'),
    path('page/', page, name='page'),
    path('fruit/<str:name>/', fruit_detail, name='fruit_detail'),
]
