from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^left', views.left),
    url(r'^right', views.right),
    url(r'^forward', views.forward),
    url(r'^backward', views.backward),
    url(r'^stop', views.stop),
    url(r'^scenario1', views.scenario1),
    url(r'^scenario2/sectionA', views.scenario2),
    url(r'^scenario2/sectionB', views.scenario2)
]
