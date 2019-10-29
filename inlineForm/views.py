from django.shortcuts import render
from .models import CourseScore
from django.http import HttpResponse
from django.forms import modelformset_factory


def home(request):
    courseForm = modelformset_factory(
        CourseScore, fields=('name', 'studentName',  'score', ), extra=1)

    if request.method == 'POST':
        formset = courseForm(request.POST,  queryset=CourseScore.objects.all())
        if formset.is_valid():
            print('vlaid')
            instanes = formset.save(commit=False)
            for ins in instanes:
                ins.save()
        else:
            print(formset.errors)

    formset = courseForm(queryset=CourseScore.objects.all())
    return render(request, 'inlineForm/home.html', {'formset': formset})
