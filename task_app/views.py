from django.shortcuts import render, HttpResponse, redirect
from .forms import NewUserForm
from django.contrib.auth import login, logout
from .forms import AddGroupDonationForm
from django.views.generic import CreateView, DetailView, UpdateView
from .models import Collect, Payment
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


