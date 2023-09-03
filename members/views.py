from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from members.models import Member
from members.forms import Memberform



def index(request):
    #   context : data to view in frontend (dictionary) ..#or html page content
    template = loader.get_template('index.html')
    return HttpResponse(template.render())



def members(request):
    mymembers = Member.objects.all().values() #البيانات الجاية من db
    template = loader.get_template('all_membrs.html')
    context = {
    'mymembers': mymembers, #dictionary #البيانات بحد ذاتها
    }
    return HttpResponse(template.render(context, request)) 


def details(request, id): #أي متحولات بتنزل بعد ال request
    mymember = Member.objects.get(id=id) #get: select * from members where id = id
    template = loader.get_template('details.html')
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))



    
def add_member(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Memberform(request.POST)
        # check whether it's valid:
        if form.is_valid(): #بداية المعالجة 
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            new_member=Member(firstname=first_name , lastname=last_name)
            new_member.save()

            
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/members/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Memberform()
        template= loader.get_template('add_member.html')
        context={
            'form' : form,
        }

    return HttpResponse(template.render(context , request))