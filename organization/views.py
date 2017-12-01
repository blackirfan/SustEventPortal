# from django.http import Http404
# from django.http import HttpResponse
#
#
# from django.shortcuts import render
#
# from .models import Organization
# from .models import Special_event
#
#
#
# def index(request):
#     all_organization = Organization.objects.all()
#     context = {
#         'all_organization': all_organization,
#     }
#
#
#     return render(request,'organization/index.html',context)
#
#
# def detail(request, organization_id):
#     try:
#         organization = Organization.objects.get(pk = organization_id)
#     except Organization.DoesNotExist:
#         raise Http404("Organization does not exist")
#     return render(request,'organization/index.html',{'organization': organization})
from django.http import HttpResponse
from django.template import loader
from .models import Organization

def index(request):
    all_organization = Organization.objects.all()

    template =loader.get_template('organization/index.html')
    context ={
        'all_organization':all_organization,
    }
    # html = ''
    # for organization  in all_organization:
    #     url = '/organization/' + str(organization.id) + '/'
    #     html += '<a href="' + url + '">' + organization.name + '</a><br>'
    return HttpResponse(template.render(context,request))
def detail(request , organization_id):
    return HttpResponse("<h2> SUST Organization id number :"+ str(organization_id)+"</h2>")

