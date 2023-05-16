# this code use to styleing form django using boostrep

from django import forms #for gets django form
from .models import Post,Category,Comment #for get the post form methode code

#choise = [('codeing','codeing'),('romance','romance'),('sport','sport'),] # this have function for thge select in views category just have this for the choice
choise = Category.objects.all().values_list('name','name')

choice_list = []
for item in choise:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippets','header_image' ) #<-- for get data from database
        
        # used widgets for stayling this forms
        widgets = { 
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value' : '', 'id':'elder', 'type':'hidden'}), #<-- send author unser name from html useing javascript code
            # we don't want the uaer to change the author, so we don't use the code below
            #'author': forms.Select(attrs={'class':'form-control'}),
            #new add category for choises
            'category' : forms.Select(choices=choice_list ,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippets': forms.Textarea(attrs={'class':'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category','body','snippets')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choice_list ,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippets': forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}), 
            'body' : forms.Textarea(attrs={'class':'form-control'}) 
        }