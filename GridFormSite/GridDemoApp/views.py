from django.shortcuts import render
from .models import Enroll
from django.http import HttpResponse
from django.forms import modelformset_factory


def home(request):
    EnrollForm = modelformset_factory(
        Enroll, fields=('courseID', 'studentID', 'couesePractical', 'courseYearWork',  'finalExamScore', 'finalExamAbsent', 'finalExamScore', 'courseTotalScore'), extra=0)

    if request.method == 'POST':
        formset = EnrollForm(request.POST,  queryset=Enroll.objects.all())
        if formset.is_valid():
            print('vlaid')
            instanes = formset.save(commit=False)
            for ins in instanes:
                ins.save()
        else:
            print(formset.errors)

    formset = EnrollForm(queryset=Enroll.objects.all())
    return render(request, 'GridDemoApp/home.html', {'formset': formset})
