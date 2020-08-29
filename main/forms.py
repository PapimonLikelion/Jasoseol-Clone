from django import forms
from .models import Jasoseol, Comment

class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol
        fields = {'title','content', 'location_si', 'location_gu'}

    def check(self):
        if(self.fields['location_si']=='seoul'):
            print("여기냐?")

    def __init__(self, *args, **kwargs):
        print("!!!!")
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class' : "jss_title",
            'placeholder' : "제목",
        })
        self.fields['content'].widget.attrs.update({
            'class' : "jss_content_js",
        })
        self.fields['location_si'].widget.attrs.update({
            'class' : "jss_location_si",
            'placeholder' : "시",
        })
        self.fields['location_gu'].widget.attrs.update({
            'class' : "jss_location_gu",
            'placeholder' : "구",
        })
        if True:
            print("Settings done")

        

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = {'content', }
