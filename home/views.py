import xlrd
from django.http import HttpResponse
from django.shortcuts import render
from .form import FileUploadForm
from .models import Student, Grade, Unit


# Create your views here.

# 挂在Home界面
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# 查询所有的grade,画图
def plot_scatter(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def upload_file(request):
    if request.method == 'POST':
        my_form = FileUploadForm(request.POST, request.FILES)
        if my_form.is_valid():
            # 开始解析上传的excel表格
            f = request.FILES["excel"]
            wb = xlrd.open_workbook(filename=None, file_contents=f.read())  # 关键点在于这里
            table = wb.sheets()[0]
            nrows = table.nrows  # 行数
            ncole = table.ncols  # 列数
            print("row :%s, cole: %s" % (nrows, ncole))

            for i in range(1, nrows):
                row = table.row_values(i)  # 一行的数据
                student = Student(
                    sid=row[0],
                    first_name=row[1],
                    last_name=row[2],

                )
                unit = Unit(
                    code=row[3],
                )
                grade = Grade(
                    grade=int(row[4])
                )
                student.save()
                unit.save()
                grade.save()

            # 这种方法是利用Form手动存储
            # f = my_form.cleaned_data['my_file']
            return HttpResponse(f.name)

    else:
        my_form = FileUploadForm()
    return render(request, 'home/uploadfile.html', {'form': my_form})

# def handle_uploaded_file(f):
#     with open(f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
