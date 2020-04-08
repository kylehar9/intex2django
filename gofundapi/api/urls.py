from django.urls import path
from django.conf.urls import url
# from api.views import resultsView
from api import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.testInputView, name='testInputView'),
    path('results', views.AzureCall.as_view()),
    path('search', views.CampaignSearch.as_view()),
    # url(r'results/', resultsView, name='resultsView'),
]

# Comment