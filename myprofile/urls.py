from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProjectList.as_view(), name='project-list'),
    url(r'^projects/add/$', views.ProjectCreate.as_view(), name='project-create'),
    url(r'^projects/(?P<project_pk>[0-9]+)/delete/$', views.ProjectDelete.as_view(), name='project-delete'),
    url(r'^projects/(?P<project_pk>[0-9]+)/update/$', views.ProjectUpdate.as_view(), name='project-update'),
    url(r'^projects/(?P<project_pk>[0-9]+)/view/$', views.ProjectView, name='project-view'),


    url(r'^projects/(?P<project_pk>[0-9]+)/profile/$', views.ProfileList.as_view(), name='profile-list'),
    url(r'^projects/(?P<project_pk>[0-9]+)/profile/add/$', views.ProfileLayerCreate.as_view(), name='profile-add'),
    url(r'^projects/(?P<project_pk>[0-9]+)/profile/(?P<profile_pk>[0-9]+)/update/$', views.ProfileLayerUpdate.as_view(), name='profile-update'),
    url(r'^projects/(?P<project_pk>[0-9]+)/profile/(?P<profile_pk>[0-9]+)/delete/$', views.ProfileDelete.as_view(), name='profile-delete'),
    url(r'^projects/(?P<project_pk>[0-9]+)/profile/(?P<profile_pk>\d+)/view/$', views.ProfileView, name='profile-view'),

]
