# -*- coding: utf-8 -*-
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator

from oauth2_provider.views.application import (
    ApplicationList as OAuthApplicationList,
    ApplicationRegistration as OAuthApplicationRegistration,
    ApplicationDetail as OAuthApplicationDetail,
    ApplicationDelete as OAuthApplicationDelete,
    ApplicationUpdate as OAuthApplicationUpdate,
)

from meta_id.authentication.models import User
from meta_id.authentication.forms import RegisterForm


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm


class DeveloperRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = "registration/user_form_developer.html"

    def form_valid(self, form):
        self.object = form.save()

        # Selecionando permissoes para associar ao usuario registrado
        permissions = Permission.objects.filter(name__icontains="application")
        self.object.user_permissions = permissions
        self.object.save()
        return super(DeveloperRegisterView, self).form_valid(form)


class ApplicationList(OAuthApplicationList):
    @method_decorator(permission_required('oauth2_provider.add_application'))
    @method_decorator(permission_required('oauth2_provider.change_application'))
    @method_decorator(permission_required('oauth2_provider.delete_application'))
    def dispatch(self, *args, **kwargs):
        return super(ApplicationList, self).dispatch(*args, **kwargs)


class ApplicationNew(OAuthApplicationRegistration):
    @method_decorator(permission_required('oauth2_provider.add_application'))
    def dispatch(self, *args, **kwargs):
        return super(ApplicationNew, self).dispatch(*args, **kwargs)


class ApplicationUpdate(OAuthApplicationUpdate):
    @method_decorator(permission_required('oauth2_provider.change_application'))
    def dispatch(self, *args, **kwargs):
        return super(ApplicationUpdate, self).dispatch(*args, **kwargs)


class ApplicationDetail(OAuthApplicationDetail):
    @method_decorator(permission_required('oauth2_provider.add_application'))
    @method_decorator(permission_required('oauth2_provider.change_application'))
    @method_decorator(permission_required('oauth2_provider.delete_application'))
    def dispatch(self, *args, **kwargs):
        return super(ApplicationDetail, self).dispatch(*args, **kwargs)


class ApplicationDelete(OAuthApplicationDelete):
    @method_decorator(permission_required('oauth2_provider.delete_application'))
    def dispatch(self, *args, **kwargs):
        return super(ApplicationDelete, self).dispatch(*args, **kwargs)
