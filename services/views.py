from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service
from .forms import ServiceInquiryForm

def services(request):
    all_services = Service.objects.all()  # fetch all services
    context = {'services': all_services}
    return render(request, 'services/services.html', context)


def service(request, pk):
    service = get_object_or_404(Service, id=pk)

    if request.method == "POST":
        form = ServiceInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.service = service
            inquiry.save()
            messages.success(request, f"پیام شما برای خدمت «{service.title}» ثبت شد. به زودی با شما تماس می‌گیریم.")
            return redirect('service', pk=pk)
    else:
        form = ServiceInquiryForm()

    context = {'service': service, 'form': form}
    return render(request, 'services/service.html', context)
