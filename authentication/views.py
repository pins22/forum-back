from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
import environ

env = environ.Env()


class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = env("GITHUB_CALLBACK_URL")
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        print(self.callback_url)
        return super().post(request, *args, **kwargs)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = env("GOOGLE_CALLBACK_URL")
    client_class = OAuth2Client
