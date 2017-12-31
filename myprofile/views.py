from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import Profile
from .forms import LayerFormSet


class ProfileList(ListView):
    model = Profile


class ProfileCreate(CreateView):
    model = Profile
    fields = ['name']


class ProfileLayerCreate(CreateView):
    model = Profile
    fields = ['name']
    success_url = reverse_lazy('profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileLayerCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['layers'] = LayerFormSet(self.request.POST)
        else:
            data['layers'] = LayerFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        layers = context['layers']
        with transaction.atomic():
            self.object = form.save()

            if layers.is_valid():
                layers.instance = self.object
                layers.save()
        return super(ProfileLayerCreate, self).form_valid(form)


class ProfileUpdate(UpdateView):
    model = Profile
    success_url = '/'
    fields = ['name']


class ProfileLayerUpdate(UpdateView):
    model = Profile
    fields = ['name']
    success_url = reverse_lazy('profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileLayerUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['layers'] = LayerFormSet(self.request.POST, instance=self.object)
        else:
            data['layers'] = LayerFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        layers = context['layers']
        with transaction.atomic():
            self.object = form.save()

            if layers.is_valid():
                layers.instance = self.object
                layers.save()
        return super(ProfileLayerUpdate, self).form_valid(form)


class ProfileDelete(DeleteView):
    model = Profile
    success_url = reverse_lazy('profile-list')
