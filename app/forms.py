# from unittest.util import _MAX_LENGTH
from django import forms
from .models import Interview

class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=50)

class UserForm(forms.ModelForm):
    
    # address = forms.CharField(label='You Address', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Your Address Here', 'rows':3, 'cols': 50}), error_messages={'required':'Must Enter a Correct Address'})
    class Meta:
        model = Interview
        fields = '__all__'
        candidate_name = forms.CharField(label='Candidate Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':' Candidate Name Here'}), required=True, error_messages={'required':'Must Enter a Correct Name'}, max_length=50)
    # int_name= forms.CharField(label='Interviewer Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Interviewer Name Here'}), required=True, error_messages={'required':'Must Enter a Correct Name'}, min_length=4),
        mobile = forms.CharField(label='Mobile Number', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mobile Number Here'}), required=True, error_messages={'required':'Must Enter a Correct Mobile Number'}, min_length=10,max_length = 10),
        overall_feedback: forms.CharField(label='Feedback',widget=forms.Textarea(attrs={"rows":2, "cols":1, 'placeholder':'Type Feedback Here'}))
        widgets = {
            
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email Here'}),
            'position': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'overall_performance' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            
            # 'language': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),

            'programming_fundamentals' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'oops_concepts' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'framework_concepts' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'restful_concepts' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'databases' : forms.RadioSelect(attrs={'class': 'form-check-input'}),
            
        }   

        error_messages = {
            'candidate_name' :{'required' : 'Must Select a Gender'},
            'gender' : { 'required' : 'Must Select a Gender'},
            'email' : { 'required' : 'Enter Correct Email'},
            'mobile' : {'required' : 'Enter a Valid Contact'},
            'position' :{'required' : 'Must selcet position'},
            'overall_performance' :{'required' : 'Must selcet Overall Performance'},
            'overall_performance' :{'required' : 'Must selcet Programming Fundamentals'},
            'oops_concepts' :{'required' : 'Must selcet Opps Concepts'},
            'framework_concepts' :{'required' : 'Must selcet Framework Concepts'},
            'restful_concepts' :{'required' : 'Must selcet Restful_Concepts'},
            'databases' :{'required' : 'Must selcet Databases'},
            

            
            
            # 'language' : { 'required' : 'Select Language You Know'},
        }

