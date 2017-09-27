from django.shortcuts import render
from django.views import View

from excel_upload.forms import ExcelForm
from .loading_excel import load_excel


class ExcelUpload(View):
    def get(self, request):
        form = ExcelForm()
        return render(request, 'excel.html', {'form': form})

    def post(self, request):
        load_excel(request.FILES['excel'])
        return render(request, 'excel.html',)
