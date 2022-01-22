from django.urls import path

from hackapp.views import*

urlpatterns=[
    path('',index,name='main page'),
    path('list/',liste,name='list'),
    path('anketa/<int:userid>',pageofuser,name='pageofuser')
    # path('device/<int:assetid>/',checker)
]