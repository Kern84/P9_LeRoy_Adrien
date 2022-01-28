"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path
import authentication.views
import publication.views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        LoginView.as_view(
            template_name="authentication/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("home/", publication.views.home, name="home"),
    path("post/", publication.views.post, name="post"),
    path("subscription/", authentication.views.subscriptions, name="subscription"),
    path(
        "change-password/",
        PasswordChangeView.as_view(
            template_name="authentication/password_change_form.html"
        ),
        name="password_change",
    ),
    path(
        "change-password-done/",
        PasswordChangeDoneView.as_view(
            template_name="authentication/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path("signup/", authentication.views.signup_page, name="signup"),
    path(
        "publication/create-ticket/",
        publication.views.create_ticket,
        name="create_ticket",
    ),
    path(
        "publication/ticket/<int:ticket_id>",
        publication.views.view_ticket,
        name="view_ticket",
    ),
    path(
        "publication/ticket/<int:ticket_id>/edit",
        publication.views.edit_ticket,
        name="edit_ticket",
    ),
    path(
        "publication/create-review/",
        publication.views.create_review,
        name="create_review",
    ),
    path(
        "publication/review/<int:review_id>",
        publication.views.view_review,
        name="view_review",
    ),
    path(
        "publication/review/<int:review_id>/edit",
        publication.views.edit_review,
        name="edit_review",
    ),
    path(
        "publication/ticket/<int:ticket_id>/answer/",
        publication.views.answer_ticket,
        name="answer_ticket",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
