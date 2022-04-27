from django.shortcuts import render

def blgliste(requiste):
     return render(requiste,'blog/blogliste',{})
