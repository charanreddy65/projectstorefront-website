from django import forms
class mangoForm(forms.ModelForm):
    #other fields…. 
    OPTIONS = (
        ('alphonse mangoes’,’Alphonse mangoess’),
        ('banginapalli mangoes’,’Banginapalli mangoes’),
        ('aparanji mangoes’,’Aparanji mangoes’),
        )
    items = forms.ChoiceField(required=True, choices=OPTIONS)

class kiloForm(forms.ModelForm):
    OPTIONS = (
        ('5','5'),
        ('10','10'),
        ('20','20'),
        ('30','30'),
        ('40','40'),
        ('50','50'),
        )
    weigh = forms.ChoiceField(required=True, choices=OPTIONS)