# from django.contrib.auth.forms import UserCreationForm
# from .models import User

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'name', 'password1', 'password2']

#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
#         for fieldname in ['username', 'password1', 'password2']:
#             self.fields[fieldname].help_text = None
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['username', 'password1', 'password2','name','email']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control', 'style': 'margin-bottom: 10px;'})
