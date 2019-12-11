from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^left', views.left),
    url(r'^right', views.right),
    url(r'^forward', views.forward),
    url(r'^backward', views.backward),
    url(r'^stop', views.stop),
    url(r'^scenario3/sectionA', views.scenario3),
    url(r'^scenario3/sectionB', views.scenario3)
]
