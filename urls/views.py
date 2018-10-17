from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Shortens

def decrypt(request, hash):
    sha = get_object_or_404(Shortens, hash=hash)
    return HttpResponseRedirect(sha.origin)
