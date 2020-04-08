from django.urls import path
from django.conf.urls import url
from api.views import resultsView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.testInputView, name='testInputView'),
    url(r'results/', resultsView, name='resultsView'),
]

# Comment