from django import forms

class New_page_form(forms.Form):
	title = forms.CharField(required = True, min_length = 1, max_length = 30, error_messages = {"required": "名字不能为空或者超过30个字"})
	area = forms.CharField(required = True, min_length = 0, max_length = 2000, error_messages={
        "required": "内容不能为空",
		"min_length": "内容不能为空",
		 "max_length": "内容不能超过2000个字",
		 })
