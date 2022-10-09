from django.shortcuts import render,redirect
from App.models import Contact
from django.views.generic.detail import DetailView

# Create your views here.


def contactlist(request):
    contactlist=Contact.objects.all()
    return render(request,'contactlist.html',{'contactlist':contactlist})

def addcontact(request):
    if request.method =='POST':
        contact=Contact(Name=request.POST['Name'],
                        PhnNo = request.POST['PhnNo'])  
        contact.save()
    return render(request,'newcontact.html')

class ContactDetail(DetailView):
    model = Contact
    template_name = 'ContactModel_detail.html'
    
def edit(request,id):
    contact=Contact.objects.get(id=id)
    return render(request,'edit.html',{'contact':contact})

def update(request,id):
    cont=Contact.objects.get(pk=id)
    cont.Name=request.POST.get('Name')
    cont.PhnNo=request.POST.get('PhnNo')
    cont.save()
    return redirect('/')

def delete(request,id):
    cont = Contact.objects.get(id=id)
    cont.delete()
    return redirect('/')