from django.shortcuts import redirect
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views 
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import *
from users.forms import SignupForm
from users.forms import UserLoginForm
from users.models import UserLogin
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def imagenes(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = request.POST.get('user','')
            password = request.POST.get('password','')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('/cargarImagen')
            else:
                error = 'Invalid username or password.'

class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:registerok')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'

    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     print(context)
    #     return context


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logged_out.html'