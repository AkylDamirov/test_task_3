from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import NewUserForm
from django.contrib.auth import login, logout
from .forms import AddGroupDonationForm, AddAmountForm
from django.views.generic import CreateView, DetailView, UpdateView
from .models import Collect, Payment
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
    events = Collect.objects.all()
    return render(request, 'task_app/index.html', {'events':events[::-1]})

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')

    form = NewUserForm
    return render(request, 'registration/register.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')


class AddGroupDonation(CreateView):
    model = Collect
    form_class = AddGroupDonationForm
    template_name = 'task_app/AddGroupDonation.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user

        subject = 'Group donation created successfully'
        message = 'Your group donation has been created successfully.'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [self.request.user.email]
        send_mail(subject,message,from_email,to_email)

        return super().form_valid(form)

class about(DetailView):
    model = Collect
    template_name = 'task_app/about.html'
    context_object_name = 'events'

class UpdateGroupDonation(UpdateView):
    model = Collect
    form_class = AddGroupDonationForm
    template_name = 'task_app/change.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)

def delete1(request, id=None):
    group = Collect.objects.get(id=id)
    group.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def profile(request):
    user = request.user
    if user.is_authenticated:
        events = Collect.objects.filter(author=user)
        context = {'events':events[::-1]}
        return render(request, 'task_app/profile.html', context)
    else:
        return redirect('login')

def add_amount(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    payments = Payment.objects.filter(pk=pk)
    form = AddAmountForm()
    collect_instance = Collect.objects.get(pk=pk)
    if request.method=='POST':
        form = AddAmountForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            FIO = form.cleaned_data['FIO']

            payment = Payment.objects.create(
                amount=amount,
                user=request.user,
                collect=collect_instance,
                FIO = FIO
            )
            instance = Collect.objects.get(pk=pk)
            instance.current_amount += amount
            instance.save()
            subject = 'Payment sent successfully'
            message = 'Your payment has been sent successfully.'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [request.user.email]
            send_mail(subject, message, from_email, to_email)

            return redirect('home')


    return render(request, 'task_app/add_amount.html', {'form': form, 'collect':collect_instance, 'payments':payments})

