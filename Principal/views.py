from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Hosts.models import Host

import json

@login_required
def principal(request):
    hosts = Host.objects.all()
    return render(request, 'principal.html', {'hosts': hosts})