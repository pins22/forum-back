from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.response import Response
import environ

env = environ.Env()


class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = env("GITHUB_CALLBACK_URL")
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        response: Response = super().post(request, *args, **kwargs)
        print(response.data)
        return response


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = env("GOOGLE_CALLBACK_URL")
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)
        self.login()
        return self.get_response()
