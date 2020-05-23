from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField(required = True, error_messages = {"required": "邮箱不能为空"})
	password = forms.CharField(required = True, min_length = 6, max_length = 20, error_messages={
		"min_length": "密码应该大于等于6个字符",
		 "max_length": "密码应该小于等于20个字符",
		 })

class RegisterForm(forms.Form):
	email = forms.EmailField(required = True, error_messages = {"required": "邮箱不能为空"})
	password = forms.CharField(required = True, min_length = 6, max_length = 20, error_messages={
		"min_length": "密码应该大于等于6个字符",
		 "max_length": "密码应该小于等于20个字符",
		 })