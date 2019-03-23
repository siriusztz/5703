from django.forms import forms

# from django.core.exceptions import ValidationError
# def validate_excel(value):
#  if value.name.split('.')[-1] not in ['xls','xlsx']:
#  raise ValidationError(_('Invalid File Type: %(value)s'),params={'value': value},)


# 要从发过来的form里面接受文件需要建立一个表单类
class FileUploadForm(forms.Form):
    excel = forms.FileField()  #(validators=[validate_excel]) #这里使用自定义的验证
