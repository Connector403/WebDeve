import logging
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, render
from main import forms
from main import models


from django import forms as django_forms
from django.db import models as django_models


class ContactUsView(FormView):
    template_name = "contact_form.html"
    form_class = forms.ContactForm
    succes_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


class ProductListView(ListView):
    template_name = "main/product_list.html"
    paginate_by = 4

    def get_queryset(self):
        tag = self.kwargs['tag']
        self.tag = None
        if tag != "all":
            self.tag = get_object_or_404(
                models.ProductTag, slug=tag
            )
        if self.tag:
            products = models.Product.objects.active().filter(
                tags=self.tag
            )
        else:
            products = models.Product.objects.active()
        return products.order_by("name")
