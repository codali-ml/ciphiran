from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactForm ,CareerForm

def home(request):
    context = {'home':home}
    return render(request,'home/home-page.html',context)

def aboutUs(request):
    context = {'aboutUs':aboutUs}
    return render(request,'home/about-us.html',context)

def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما با موفقیت ثبت شد. تیم ما در اسرع وقت با شما تماس خواهد گرفت")
            return redirect('contact')

    context = {'form': form}
    return render(request, 'home/contact-us.html', context)

def career(request):
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "درخواست شما با موفقیت ثبت شد. تیم ما به زودی با شما تماس خواهد گرفت.")
            return redirect('careers')
    else:
        form = CareerForm()

    context = {'form': form}
    return render(request, 'home/careers.html', context)