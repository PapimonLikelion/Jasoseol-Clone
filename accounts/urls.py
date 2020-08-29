from django.urls import path
from .views import signup, myLoginView
from django.contrib.auth.views import LogoutView
# from .views import

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', myLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]