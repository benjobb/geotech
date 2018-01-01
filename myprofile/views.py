from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.shortcuts import render

from .models import Profile, Layers, Project
from .forms import LayerFormSet

class Object(object):
    pass

class ProfileList(ListView):
    model = Profile
    def get_context_data(self, **kwargs):
        context = super(ProfileList,self).get_context_data(**kwargs)
        context['project_pk'] = self.kwargs['project_pk']

        project_pk = self.kwargs['project_pk']
        project = Project.objects.get(pk = project_pk)
        context['project']=project
        return context

    def get_queryset(self):
        project_pk = self.kwargs['project_pk']
        project = Project.objects.get(pk = project_pk)
        profiles = Profile.objects.filter(project=project)

        return profiles

def ProfileView(request,project_pk,profile_pk):
    try:
        profile=Profile.objects.get(pk=profile_pk)
        layers = Layers.objects.filter(profile=profile)
        cumulative = 0

        for layer in layers:
            cumulative += layer.depth
            layer.cumulative = cumulative

    except Profile.DoesNotExist:
        raise Http404("Profile does not exist")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'myprofile/view_profile.html',
        context={'profile':profile,'layers':layers}
    )

class ProfileLayerCreate(CreateView):
    model = Profile
    fields = ['name', 'water_table_depth']
    success_url = reverse_lazy('profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileLayerCreate, self).get_context_data(**kwargs)
        data['project_pk'] = self.kwargs['project_pk']
        project_pk = self.kwargs['project_pk']
        project = Project.objects.get(pk = project_pk)
        data['project']=project

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
    fields = ['name',  'water_table_depth']


class ProfileLayerUpdate(UpdateView):
    model = Profile
    fields = ['name', 'water_table_depth']
    success_url = reverse_lazy('profile-list')

    def get_context_data(self, **kwargs):
        data = super(ProfileLayerUpdate, self).get_context_data(**kwargs)
        data['project_pk'] = self.kwargs['project_pk']
        project_pk = self.kwargs['project_pk']
        project = Project.objects.get(pk = project_pk)
        data['project']=project

        if self.request.POST:
            data['layers'] = LayerFormSet(self.request.POST, instance=self.object)
            data['project_pk'] = self.kwargs['project_pk']


        else:
            data['layers'] = LayerFormSet(instance=self.object)
            data['project_pk'] = self.kwargs['project_pk']
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


# projects
class ProjectList(ListView):
    model = Project
    template_name= 'projects/project_list.html'

class ProjectCreate(CreateView):
    model = Project
    fields = ['name']
    template_name='projects/project_add.html'
    success_url = '/'


class ProjectUpdate(UpdateView):
    model = Project
    success_url = '/'
    fields = ['name']
    pk_url_kwarg = 'project_pk'
    template_name='projects/project_update.html'


class ProjectDelete(DeleteView):
    model = Project
    template_name='projects\project_confirm_delete.html'
    success_url = reverse_lazy('project-list')
    pk_url_kwarg = 'project_pk'

def ProjectView(request,project_pk):
    try:
        project=Project.objects.get(pk=project_pk)
        profiles = Profile.objects.filter(project=project)

    except Project.DoesNotExist:
        raise Http404("Profile does not exist")

    #book_id=get_object_or_404(Book, pk=pk)

    return render(
        request,
        'myprofile/profile_list.html',
        context={'profiles':profiles,'project':project,'project_pk':project_pk}
    )
