
from django.urls import path
from login.views import LogarView, UserView, csrfGet

urlpatterns = [
    path('login/',LogarView.as_view(),name="login"),
    path('csrf/',csrfGet,name="csrfGet"),
    path('view/',UserView.as_view(),name="userView"),
]