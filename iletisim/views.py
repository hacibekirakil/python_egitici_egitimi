from django.shortcuts import render

def iletisimlist(requiste):
     return render(requiste,'iletisim/iletisimlist.html',{})
