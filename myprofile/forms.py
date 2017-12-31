from django.forms import ModelForm, inlineformset_factory

from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ()


class LayerForm(ModelForm):
    class Meta:
        model = Layers
        exclude = ()


LayerFormSet = inlineformset_factory(Profile, Layers,
                                            form=LayerForm, extra=1)
