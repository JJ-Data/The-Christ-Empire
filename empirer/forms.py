from django.forms import ModelForm
from .models import Weekly, Live


class WeeKlyForm(ModelForm):
    class Meta:
        model = Weekly
        fields = ['title', 'url']

    def __init__(self, *args, **kwargs):
        super(WeeKlyForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'textbox'})


class LiveForm(ModelForm):
    class Meta:
        model = Live
        fields = ['title', 'url']

    def __init__(self, *args, **kwargs):
        super(LiveForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'textbox'})