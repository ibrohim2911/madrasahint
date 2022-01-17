from django.urls import path
from .views import usersview, ModelListView, UserListView
urlpatterns = [
    path('register/', usersview.as_view(), name='register' ),
    path("", UserListView.as_view(), name="home"),
    path('done/', ModelListView.as_view(), name="done")
]
