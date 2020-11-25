from django.urls import path

from idvalidator.views import IndexView

app_name = 'idvalidator'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
