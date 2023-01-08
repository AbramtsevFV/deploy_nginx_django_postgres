from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from loader.form import ImageForm


class Index(View):
    template_name = "loader/index.html"

    def get(self, request):
        form = ImageForm()
        return render(request, self.template_name, {'form': form})




class Upload(View):
    template_name = "loader/upload.html"

    def get(self, request):

        return render(request, self.template_name,)


    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Вместо form.instance должно быть фото результата
            img_obj = form.instance
            # Результат обработки
            result = 'На фото поза собаки'
            return render(request, self.template_name, {'form': form, 'img_obj': img_obj, 'result': result})