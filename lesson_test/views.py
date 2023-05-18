# -*- coding: utf8 -*-
from django.shortcuts import render
from django.views import View
from .models import Product, Category


# Create your views here.
class MainPage(View):

    def get(self, request):
        title = request.GET.get("title")
        if title:
            products = Product.objects.filter(title=title)
        else:
            products = Product.objects.all()
        return render(request, "index.html", context={
            "title": "MainPage",
            "products": products,
            "count_product": products.count()
        })

    def post(self, request):
        Product.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            price=request.POST.get("price"),
            quantity=request.POST.get("quantity"),
            category=Category.objects.get(title="Для уборки")
        )
        return render(request, "index.html", context={
            "title": "MainPage",
            "products": Product.objects.all(),
        })
