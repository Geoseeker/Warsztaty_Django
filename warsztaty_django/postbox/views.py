from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from postbox.models import Person, Adress, Telephone, Email
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')  
class AddPerson(View):    
    def get(self,request):
#         context = {'person': Person.objects.get(pk=1)}
#     <!--  {{person.name}}, {{person.surname}}
#         {% for telephone in person.telephone%}-->    
        return render(request, 'postbox/form.html')    #,  context)

#         response = HttpResponse()
#     
#         html = """<form method='GET'>
#              Wprowadź ID osoby:<br>
#              <input type="text" name="id"><br>
#              <input type="submit" value="Modyfikuj osobę">
#              </form> """
#         response.write(html)
#         return response

    def post(self,request):
        response = HttpResponse()
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        description = request.POST.get('description')
        city = request.POST.get('city')
        street = request.POST.get('street')
        home_number = request.POST.get('home_number')
        flat_numer = request.POST.get('flat_number')
        tele_number = request.POST.get('tele_number')
        tele_type = request.POST.get('tele_type')
        email_address = request.POST.get('email_address')
        email_type = request.POST.get('email_type')
         
        person = Person.objects.create(name=name,surname=surname, description=description)
        Adress.objects.create(city=city,street=street, home_number=home_number, flat_number=flat_numer, person=person)
        Telephone.objects.create(tele_number=tele_number,tele_type=tele_type,person=person)
        Email.objects.create(email_address=email_address,email_type=email_type,person=person)               
         
        response.write('Nowa osoba została dodana')
        response.write('<br /><a href="/new"><input type="submit" value="Wróc do strony głównej"></a>')
         
        return response
     
 
def modif(request):
        if request.method == 'GET':
            response = HttpResponse()
            person = Person.objects.all()
            for i in person:
                response.write('Przejdź do edycji osoby o <a href="modify/{}">id={}</a> lub kliknij by usunąć <a href="delete/{}">id={}</a><br />'.format(i.id, i.id, i.id, i.id))
                
        
        return response

def delete(request,id):
    if request.method == 'GET':
        response = HttpResponse()
        p = Person.objects.get(pk = id)
        response.write('Osoba o id={} została usunięta z bazy'.format(p.id))
        p.delete()
        return response  
     
@method_decorator(csrf_exempt, name='dispatch')       
class ModifyPerson(View):
    def get(self,request,id):
        person = Person.objects.get(pk = id)
        peradd = Adress.objects.get(pk = id)
        pertel = Telephone.objects.get(pk = id)
        perema =  Email.objects.get(pk = id)    
        
        response = HttpResponse()
        response.write('<h3>Aktualne dane osoby o nr. id={}:</h3><br />'.format(person.id))
        response.write('Imię: <b>{}</b> Nazwisko: <b>{}</b> Opis:<b>{}</b><br />'.format(person.name, person.surname, person.description))
        response.write('<u>ADRES:</u><br><u>miasto</u>:<b>{}</b><u>ulica:</u><b>{}</b><u>nr.domu:</u><b>{}</b><u>nr.mieszkania:</u><b>{}</b><br />'
                       .format(peradd.city, peradd.street, peradd.home_number,peradd.flat_number))
        response.write('<u>nr.telefonu:</u><b>{}</b><b>{}</b><u>email</u><b>{}</b><b>{}</b></b><br />'
                       .format(pertel.tele_number, pertel.tele_type, perema.email_address, perema.email_type))
        
        response.write('<br /><b>Skorzystaj z formularza poniżej aby edytować dane</b><br />')
        
        html = """<form method='POST'>
             Podaj imię:<input type="text" name="name"><br>
             Podaj nazwisko:<input type="text" name="surname"><br>
             Podaj opis:<input type="text" name="description"><br>
             Podaj miasto:<input type="text" name="city"><br>
             Podaj ulicę:<input type="text" name="street"><br>
             Podaj nr.domu:<input type="text" name="home_number"><br>
             Podaj nr.mieszkania:<input type="text" name="flat_number"><br>
             Podaj numer telefonu:<input type="text" name="tele_number"><br>
             Podaj typ numeru:<select name="tele_type">
                              <option value="0">domowy</option>
                              <option value="1">business</option>
                              <option value="2">private</option>
                              </select>
                              <br>
             Podaj adres email:<input type="text" name="email_address"><br>                 
             Podaj typ adresu email:<select name="email_type">
                              <option value="0">domowy</option>
                              <option value="1">business</option>
                              <option value="2">private</option>
                              </select>
                              <br>
                              <input type="submit" value="Edytuj dane">
                              </form>"""
        
        response.write(html)
        return response
    
    def post(self,request,id):
        response = HttpResponse()
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        description = request.POST.get('description')
        city = request.POST.get('city')
        street = request.POST.get('street')
        home_number = request.POST.get('home_number')
        flat_numer = request.POST.get('flat_number')
        tele_number = request.POST.get('tele_number')
        tele_type = request.POST.get('tele_type')
        email_address = request.POST.get('email_address')
        email_type = request.POST.get('email_type')
         
        person = Person.objects.update(name=name,surname=surname, description=description)
        Adress.objects.update(city=city,street=street, home_number=home_number, flat_number=flat_numer, person=person)
        Telephone.objects.update(tele_number=tele_number,tele_type=tele_type,person=person)
        Email.objects.update(email_address=email_address,email_type=email_type,person=person)               
         
        response.write('Dziękuje - Dane osoby zostały zaktualizowane')
        response.write('<a href="/new"><input type="submit" name="Wróc do strony głównej"></a>')
        
        return response
        
     

      
        
        
        
        
        
        
        
        
        
        
        