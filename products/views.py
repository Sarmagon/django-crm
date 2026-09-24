from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import ProductForm
from .models import Product


class ProductListView(PermissionRequiredMixin, ListView):
    model = Product
    permission_required = "products.view_product"
    context_object_name = "products"
    template_name = "products/products-list.html"


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = "products.add_product"
    template_name = "products/products-create.html"
    success_url = reverse_lazy("products:list")


class ProductDetailView(PermissionRequiredMixin, DetailView):
    model = Product
    permission_required = "products.view_product"
    template_name = "products/products-detail.html"


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = "products.change_product"
    template_name = "products/products-edit.html"

    def get_success_url(self):
        return reverse_lazy("products:detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = "products.delete_product"
    template_name = "products/products-delete.html"
    success_url = reverse_lazy("products:list")
