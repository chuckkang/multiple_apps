
from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
# url(r'^$', views.index), # This line has changed!
url(r'^$', views.index), # This line has changed!
url(r'^/$', views.index), # This line has changed!
url(r'^/new$', views.new), #httpresponse
url(r'^/create$', views.create), #Have this be handled by a method named 'create'.For now, have this url redirect to /blogs.
url(r'/(?P<number>\d+)$', views.show), #display 'placeholder to display blog {{number}}Have this be handled by a method named 'show'.
url(r'/(?P<number>\d+)/edit$', views.edit), #display 'placeholder to edit blog {{number}}. Have this be handled by a method named 'edit'.
url(r'/(?P<number>\d+)/delete$', views.destroy) # Have this be handled by a method named 'destroy' redirect to /blogs
]