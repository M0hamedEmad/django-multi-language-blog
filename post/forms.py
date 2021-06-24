from django import  forms
from .models import Comment

class CommentForm(forms.ModelForm):
    # content = forms.ChoiceField(widget=forms.Textarea({'placeholder':"Write Your Comment Here"}), label='', )
    class Meta:
        model = Comment
        fields = ['content',]
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__()
        
    #     self.fields['content'].widget.attrs = {
    #         'placeholder':"Write Your Comment Here"
    #     }
    #     self.fields['content'].label = ''