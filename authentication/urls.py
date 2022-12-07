# implement acording to ../forum_back/urls.py

# Compare this snippet from auth/urls.py:
from django.urls import path
from .views import GithubLogin, GoogleLogin
from django.conf.urls import include

urlpatterns = [
    path('github/', GithubLogin.as_view(), name='github_login'),
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls'))
]
