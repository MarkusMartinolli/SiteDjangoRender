from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Problema, PerfilOficina, Especialidade

class ClienteSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label='Primeiro Nome')
    last_name = forms.CharField(max_length=30, required=True, label='Sobrenome')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_cliente = True
        if commit:
            user.save()
        return user

class OficinaSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label='Nome do Responsável')
    nome_oficina = forms.CharField(max_length=200, required=True, label='Nome da Oficina')
    endereco = forms.CharField(max_length=255, required=True, label='Endereço')
    especialidades = forms.ModelMultipleChoiceField(
        queryset=Especialidade.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Especialidades'
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_oficina = True
        if commit:
            user.save()
            # Criar perfil da oficina
            perfil = PerfilOficina.objects.create(
                usuario=user,
                nome_oficina=self.cleaned_data['nome_oficina'],
                endereco=self.cleaned_data['endereco']
            )
            perfil.especialidades.set(self.cleaned_data['especialidades'])
        return user

class ProblemaForm(forms.ModelForm):
    class Meta:
        model = Problema
        fields = ['titulo', 'modelo_carro', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo_carro': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class OficinaPerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilOficina
        fields = ['nome_oficina', 'endereco', 'especialidades']
        widgets = {
            'nome_oficina': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidades': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }