from django import forms
from countries.models import Country
from people.models import Person


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    nationality = forms.ModelMultipleChoiceField(queryset=Country.objects.all())
    father = forms.ModelChoiceField(required=False, queryset=Person.objects.all())


# Other more efficient
class RegisterFormModel(forms.ModelForm):

    def __init__(self, fathers, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['father'].queryset = fathers

    class Meta:
        model = Person
        # father can be null if declered in the model blank=True
        fields = ['first_name', 'nationality', 'father']
