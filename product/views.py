from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductInquiryForm

def products(request):
    all_products = Product.objects.all() 
    context = {'products': all_products}
    return render(request, 'product/products.html', context)


def product(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == "POST":
        form = ProductInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.product = product
            inquiry.save()
            messages.success(request, f"پیام شما برای محصول «{product.title}» ثبت شد. به زودی با شما تماس می‌گیریم.")
            return redirect('product', pk=pk)
    else:
        form = ProductInquiryForm()

    context = {'product': product, 'form': form}
    return render(request, 'product/product.html', context)
