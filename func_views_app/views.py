from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
"""
1. Funkcija koja prima GET i POST metodi. Vo body vo POST metodod da se praka ime / string. Funkcijata da vraka json so slednive podatoci
Imeto koe e prateno
Dolzinata na Imeto
Imeto so site golemi bukvi
Imeto so site malite bukvi golemi, a golemite malite
"""
@api_view(["GET","POST"])
def korisnikime(request):
    ime=request.data.get("ime",None)
    return Response ({
        "Ime" : ime,
        "Dolzina" : len(ime),
        "GolemiBukvi": ime.upper (),
        "PromeniBukvi": ime.swapcase () 
        })

""" 
2. Funkcija koja ke prima POST metod. Funkcijata da moze da presmetuva plostina i perimetar na pravoagolnik. Vo body da se prakjaat stranite i 
sto da se presmeta plostina ili perimetar. Funkcijata da vraka JSON so slednive podatoci
strana a
strana b
plostina / perimetar(rezultatot)
"""
@api_view (["POST"])
def pravoagolnik (request):
    str1= int (request.data.get("str1",0))
    str2= int (request.data.get("str2",0))
    izbor =request.data.get ("izbor", None)
    if (izbor=="plostina"):
        plostina = str1*str2
        return Response({"str1":str1,
                        "str2":str2,
            "info":"Plostina na pravoagolnik iznesuva {}".format(plostina)})
    elif  (izbor=="perimetar"):
        perimetar= 2*str1+2*str2
        return Response({"str1":str1,
                        "str2":str2,
            "Info":"Perimetar na pravoagolnik iznesuva {}".format (perimetar)})

"""
3. Funkcija koja ke prima GET metod. Funkcijata da prima get parametar koj e broj i da se proveri dali toj broj e paren ili neparen. 
Da se vraka JSON so klucen zbor paren i true / false vrednost"""

@api_view (["GET"])
def proverka (request):
    broj=int(request.GET.get("broj",""))
    if (broj %2==0):
        return Response({"True":"Brojot {} e paren".format(broj)})
    else:
        return Response({"False":"Brojot {} e neparen".format(broj)})