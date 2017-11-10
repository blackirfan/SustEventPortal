from django.http import Http404
from django.http import HttpResponse

from django.shortcuts import render
from .models import Organization



def index(request):
    all_organization = Organization.objects.all()
    context = {
        'all_organization': all_organization}


    return render(request,'organization/index.html',context)


def detail(request, organization_id):
    try:
        organization = Organization.objects.get(pk = organization_id)
    except Organization.DoesNotExist:
        raise Http404("Organization does not exist")
    return render(request,'organization/detail.html',{'organization': organization})
