from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic import View

from .models import CbtcatUser, Login
from .register_forms import UserRegisterForm


class UserRegisterFormView(View):
    form_class = UserRegisterForm
    template_name = 'registration.html'

    def get(self, request):
        user = request.user
        if CbtcatUser.objects.filter(username=user.username).exists():
            cbtcat_user = CbtcatUser.objects.get(username=user.username)
            return render(request, 'index.html', {'level': cbtcat_user.current_level})
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST or None)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            consent = form.cleaned_data['consent']

            if password1 and password2 and password1 != password2:
                return render(request, 'registration.html', {'error': 'Passwords do not match'})
            user.set_password(form.check_password_match(password1, password2))
            user.save()
            cbtcat_user, created = CbtcatUser.objects.get_or_create(user=user, username=username)

            user = authenticate(username=username, password=password1)
            if user is not None:
                if user.is_active:
                    user_log = Login.objects.create(username=username)
                    login(request, user)
                    return render(request, 'registration.html', {'error': 'sign up successful!'})
            else:
                user_log = Login.objects.create(username=username)
                return render(request, 'registration.html', {'error': 'signed up'})
        return render(request, 'registration.html', {'error': 'error logging in, try a different username'})


def user_login(request):
    user = request.user
    if CbtcatUser.objects.filter(username=user.username).exists():
        cbtcat_user = CbtcatUser.objects.get(username=user.username)
        return render(request, 'index.html', {'level': cbtcat_user.current_level})

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                cbtcat_user = CbtcatUser.objects.get(username=username)
                update = cbtcat_user.num_times_login
                cbtcat_user.num_times_login = update+1
                cbtcat_user.save()
                user_log = Login.objects.create(username=username)

                return render(request, 'index.html', {'level': cbtcat_user.current_level})
            else:
                return render(request, 'login.html', {'error': '!!!'})
        else:
            return render(request, 'login.html', {'error': 'Invalid login'})
    return render(request, 'login.html', {})


def links(request):
    return render(request, 'links.html', {})


def index(request):
    user = request.user
    if CbtcatUser.objects.filter(username=user.username).exists():
        cbtcat_user = CbtcatUser.objects.get(username=user.username)
        return render(request, 'index.html', {'level': cbtcat_user.current_level})
    else:
        return render(request, 'login.html', {})


def tohome(request):
    user = request.user
    if CbtcatUser.objects.filter(username=user.username).exists():
        cbtcat_user = CbtcatUser.objects.get(username=user.username)
        return render(request, 'index.html', {'level': cbtcat_user.current_level})
    return render(request, 'login.html', {})
