import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from authentication.forms import UserLoginForm, UsuarioPerfilForm
from django.contrib.auth.models import auth
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.db.models.query_utils import Q
from authentication.models import Usuario
from authentication.forms import UserRegisterForm
from seguridad.settings import email_send

username = ''


class PagesLoginView(View):
    template_name = "authentication/pages-login.html"

    def get(self, request):
        if 'username' in request.session:
            return redirect('dashboard')
        else:
            return render(request, self.template_name, {'form': UserLoginForm})

    def post(self, request):
        if request.method == 'POST':
            user_name = request.POST['username']
            password = request.POST['password']
            if user_name == '':
                messages.error(request, 'Ingrese su usuario')
                return redirect('pages-login')
            elif password == '':
                messages.error(request, 'Ingrese su contraseña')
                return redirect('pages-login')
            else:
                user = auth.authenticate(username=user_name, password=password)
                if user is not None:
                    if user.usuario_activo:
                        request.session['username'] = user_name
                        request.session['isModulo'] = False
                        auth.login(request, user)
                        return redirect('dashboard')
                    else:
                        user = None
                        messages.error(request, 'Usuario inactivo')
                        return redirect('pages-login')
                else:
                    messages.error(request, 'Credenciales invalidas')
                    return redirect('pages-login')
        else:
            return render(request, self.template_name)


class PagesRecoverpwView(View):
    template_name = 'authentication/pages-recoverpw.html'

    def get(self, request):
        if 'username' in request.session:
            return redirect('dashboard')
        else:
            return render(request, self.template_name, {'form': PasswordResetForm})

    def post(self, request):
        if request.method == "POST":
            email = request.POST.get("email", "default value")
            if Usuario.objects.filter(email=email).exists():
                password_reset_form = PasswordResetForm(request.POST)
                if password_reset_form.is_valid():
                    data = password_reset_form.cleaned_data['email']
                    associated_users = Usuario.objects.filter(Q(email=data))
                    if associated_users.exists():
                        for user in associated_users:
                            subject = "RECUPERACIÓN DE CONTRASEÑA"
                            email_template_name = "authentication/email.txt"
                            c = {
                                "username": user.username,
                                "email": user.email,
                                'domain': '95.216.216.98:8086',
                                'site_name': 'Website',
                                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                                "user": user,
                                'token': default_token_generator.make_token(user),
                                'protocol': 'http',
                            }
                            email = render_to_string(email_template_name, c)
                            try:
                                send_mail(subject, email, 'sigocd@gmail.com',
                                          [user.email], fail_silently=False)
                            except BadHeaderError:
                                messages.info(request, "Email Doesn't Exists ")
                                return redirect('pages-recoverpw')
                            return redirect("password_reset_done")
                password_reset_form = PasswordResetForm()
                return render(request=request, template_name="authentication/pages-recoverpw.html",
                              context={"password_reset_form": password_reset_form})
            else:
                if email == "":
                    messages.info(request, 'Ingrese su email')
                    return redirect('pages-recoverpw')
                else:
                    messages.info(request, "Ingrese su email")
                    return redirect('pages-recoverpw')
        else:
            return render(request, 'authentication/pages-recoverpw.html')


class PagesLockscreenView(View):
    def get(self, request):
        return render(request, 'authentication/pages-lockscreen.html')


class PagesConfirmmailView(View):
    def get(self, request):
        return render(request, 'authentication/pages-confirmmail.html')


class PagesEmailVerificationView(View):
    def get(self, request):
        return render(request, 'authentication/pages-emailverificationmail.html')


class PagesTwoStepVerificationView(View):
    def get(self, request):
        return render(request, 'authentication/pages-twostepverificationmail.html')


def logout(request):
    auth.logout(request)
    return redirect('pages-login')


def verify(nro):
    l = len(nro)
    if l == 10 or l == 13:  # verificar la longitud correcta
        cp = int(nro[0:2])
        if 1 <= cp <= 24:  # verificar codigo de provincia
            tercer_dig = int(nro[2])
            if 0 <= tercer_dig < 6:  # numeros enter 0 y 6
                if l == 10:
                    return __validar_ced_ruc(nro, 0)
                elif l == 13:
                    return __validar_ced_ruc(nro, 0) and nro[
                                                         10:13] == '001'  # se verifica que los ultimos numeros sean 001
            elif tercer_dig == 6:
                return __validar_ced_ruc(nro, 1) and nro[10:13] == '001'  # sociedades publicas
            elif tercer_dig == 9:  # si es ruc
                return __validar_ced_ruc(nro, 2) and nro[10:13] == '001'  # sociedades privadas
            else:
                return False
        else:
            return False
    else:
        return False


def __validar_ced_ruc(nro, tipo):
    total = 0
    if tipo == 0:  # cedula y r.u.c persona natural
        base = 10
        d_ver = int(nro[9])  # digito verificador
        multip = (2, 1, 2, 1, 2, 1, 2, 1, 2)
    elif tipo == 1:  # r.u.c. publicos
        base = 11
        d_ver = int(nro[8])
        multip = (3, 2, 7, 6, 5, 4, 3, 2)
    elif tipo == 2:  # r.u.c. juridicos y extranjeros sin cedula
        base = 11
        d_ver = int(nro[9])
        multip = (4, 3, 2, 7, 6, 5, 4, 3, 2)
    for i in range(0, len(multip)):
        p = int(nro[i]) * multip[i]
        if tipo == 0:
            total += p if p < 10 else int(str(p)[0]) + int(str(p)[1])
        else:
            total += p
    mod = total % base
    val = base - mod if mod != 0 else 0
    return val == d_ver


def send_email_registro(email, name, last_name, identify, password):
    subject = "USUARIO DE INGRESO PARA EL SIGOCD"
    email_template_name = "authentication/register-email.txt"
    email_user = email
    c = {
        'username': identify,
        'password': password,
        'nombres': name,
        'apellidos': last_name,
    }
    email_1 = render_to_string(email_template_name, c)
    send_mail(subject, email_1, 'sigocd@gmail.com',
              [email_user], fail_silently=False)


class UserView(View):
    def get(self, request):
        usuario = Usuario.objects.filter(usuario_activo=True).order_by('apellidos')
        greeting = {'heading': "Usuario", 'pageview': "Administración", 'usuarioview': usuario}
        return render(request, 'authentication/usuario.html', greeting)

    def register(request):
        if request.method == 'POST':
            user_form = UserRegisterForm(request.POST)
            identification = request.POST['identificacion']
            if not verify(identification):
                messages.warning(request, "El numero de identificación es invalida", "warning")
                return redirect('usuario')
            # split = request.POST['nombres'].split(' ')
            # split1 = request.POST['apellidos'].split(' ')
            # pswd = split[0][0].upper() + split1[0][0].lower() + "-" + request.POST['identificacion']
            pswd = request.POST['identificacion']

            if user_form.is_valid():
                if email_send:
                    email_user = request.POST['email']
                    name = request.POST['nombres']
                    last_name = request.POST['apellidos']
                    dni = request.POST['identificacion']
                    send_email_registro(email_user, name, last_name, dni, pswd)
                else:
                    user_form.save()
                messages.success(request, "Se registro correctamente", "success")
            else:
                aux = Usuario.objects.filter(email=request.POST['email'])
                if aux:
                    messages.warning(request, "Ya exite ese correo", "warning")
                aux = Usuario.objects.filter(identificacion=request.POST['identificacion'])
                if aux:
                    messages.warning(request, "Ya exite un usuario con esta identificación", "warning")
            return redirect('usuario')
        else:
            user_form = UserRegisterForm()
            user = Usuario()
            view = False
            context = {'usuarioFormView': user_form, 'usuario': user, 'view': view}
        return render(request, 'authentication/usuarioForm.html', context)

    def view_user(request, pk):
        user = get_object_or_404(Usuario, pk=pk)
        user_form = UserRegisterForm(instance=user)
        view = True
        context = {'usuarioFormView': user_form, 'usuario': user, 'view': view}
        return render(request, 'authentication/usuarioForm.html', context)

    def update(request, pk):
        obj = get_object_or_404(Usuario, pk=pk)
        context = {}
        if request.method == 'POST':
            identification = request.POST['identificacion']
            if not verify(identification):
                messages.warning(request, "El número de identificación es invalida", "warning")
                return redirect('usuario')
            form = UserRegisterForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, "Se edito correctamente", "success")
                return redirect('usuario')
        else:
            user_form = UserRegisterForm(instance=obj)
            view = False
            context = {'usuarioFormView': user_form, 'usuario': obj, 'view': view}
        return render(request, 'authentication/usuarioForm.html', context)

    def delete(request, pk):
        user = get_object_or_404(Usuario, pk=pk)
        if user:
            user.delete()
            messages.success(request, "Se ha eliminado correctamente", "success")
        return redirect('usuario')


class UsuarioPerfilView(View):
    template_name = 'authentication/usuarioPerfil.html'

    def get(self, request):
        user = get_object_or_404(Usuario, pk=request.user.id)
        user_perf_form = UsuarioPerfilForm(instance=user)
        greeting = {'heading': "Perfil", 'pageview': "Perfil", "form": user_perf_form, "usuario": user}
        return render(request, self.template_name, greeting)

    def update(self, request, pk):
        user = get_object_or_404(Usuario, pk=pk)
        if request.method == 'POST':
            user_perf_form = UsuarioPerfilForm(data=request.POST, instance=user, files=request.FILES)
            print(user_perf_form)
            if user_perf_form.is_valid():
                user_perf_form.save()
                messages.success(request, "Se edito correctamente", "success")
                return redirect('user')
            else:
                messages.success(request, "No se puede editar", "error")
                return redirect('user')
        else:
            user_perf_form = UsuarioPerfilForm(instance=user)
            view = False
            context = {'usuarioPerfilForm': user_perf_form, 'usuario': user, 'view': view}
        return render(request, 'authentication/usuario-perfil.html', context)
