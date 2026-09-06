from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.urls import reverse


class RegisterView(View):

    def get(self, request):
        return render(request, "accounts/register.html")

    def post(self, request):
        username = request.POST.get("username")

        if not username:
            print("Registration failed: username is empty")
            return HttpResponse("Registration failed: username is required")

        registered_user = request.session.get("registered_user")

        if registered_user == username:
            print(f"Registration failed: {username} is already registered")
            return HttpResponse("User is already registered")

        request.session["registered_user"] = username

        print(f"User registered successfully: {username}")

        return HttpResponse(
            f"Registration successful for {username}. "
            f'<a href="{reverse("accounts:login")}">Go to Login</a>'
        )


class LoginView(View):

    def get(self, request):
        return render(request, "accounts/login.html")

    def post(self, request):
        username = request.POST.get("username")

        if not username:
            print("Login failed: username is empty")
            return HttpResponse("Login failed: username is required")

        registered_user = request.session.get("registered_user")

        if username != registered_user:
            print(f"Login failed: {username} is not registered")
            return HttpResponse("Login failed: user is not registered")

        request.session["logged_in_user"] = username

        print(f"Login successful: {username}")

        return redirect("accounts:profile")


class ProfileView(View):

    def get(self, request):
        username = request.session.get("logged_in_user")

        if not username:
            print("Profile denied: user is not logged in")
            return HttpResponse(
                'You must login first. '
                '<a href="/accounts/login/">Login</a>'
            )

        print(f"Profile opened by: {username}")

        return render(
            request,
            "accounts/profile.html",
            {"username": username},
        )


def status_view(request):
    username = request.session.get("logged_in_user")

    return JsonResponse({
        "status": "ok",
        "logged_in": username is not None,
        "username": username,
    })