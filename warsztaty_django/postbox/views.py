from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from postbox.models import Person, Adress, Telephone, Email
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')   
class GetOrPost(View):
    
    def get(self,request):
        response = HttpResponse()
        response.write('Wszedłeś przez GET')
        form = """<form method='POST'>
                   
                      <input type="submit" value="Wejdź przez POST">
                    </form> """
        response.write(form)
        return response
    def post(self,request):
        response = HttpResponse()
#         name = request.POST.get('name')
#         surname = request.POST.get('surname')
        response.write('Wszedłeś przez POST<br>\
        <a href="/get_or_post"><input type="submit" value="Wróć do GET"></a>')#.format(name,surname))
        return response