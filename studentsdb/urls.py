"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
# Students urls
url(r'^$', 'students.custom_views.student_list.students_list', name='home'),
url(r'^students/add/$', 'students.custom_views.student_list.students_add',
   name='students_add'),
url(r'^students/(?P<sid>\d+)/edit/$', 'students.custom_views.student_list.students_edit', name='students_edit'),
url(r'^students/(?P<sid>\d+)/delete/$',         'students.custom_views.student_list.students_delete', name='students_delete'),
url(r'^groups/$', 'students.custom_views.groups.groups_list', name='groups'),
url(r'^groups/add/$', 'students.custom_views.groups.groups_add',
   name='groups_add'),
url(r'^groups/(?P<gid>\d+)/edit/$',
   'students.custom_views.groups.groups_edit', name='groups_edit'),
url(r'^groups/(?P<gid>\d+)/delete/$',
   'students.custom_views.groups.groups_delete',
   name='groups_delete'),
url(r'^journal/', 'students.custom_views.journal.journal', name = 'journal'),
url(r'^admin/', include(admin.site.urls)),
)
