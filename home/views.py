from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def display_form(req):
    if req.method=='POST':
        fam=int(req.POST.get('fam'))
        electricity=int(req.POST.get('electricity'))
        plastic=int(req.POST.get('plastic'))
        two_wheeler_no=int(req.POST.get('two_wheeler_no'))
        two_wheeler_mlg=int(req.POST.get('two_wheeler_mlg'))
        dist_2=int(req.POST.get('dist_2'))
        four_wheeler_no=int(req.POST.get('four_wheeler_no'))
        four_wheeler_mlg=int(req.POST.get('four_wheeler_mlg'))
        dist_4=int(req.POST.get('dist_4'))
        dist_train=int(req.POST.get('dist_train'))
        dist_bus=int(req.POST.get('dist_bus'))
        trees=int(req.POST.get('trees'))
        emission=calculate_footprint(fam,electricity,plastic,two_wheeler_no,two_wheeler_mlg,dist_2,four_wheeler_no,four_wheeler_mlg,dist_4,dist_train,dist_bus,trees)
        e=Emission.objects.order_by('id')[0]
        d={'Electricity Emission':e.electricity_emission,'Plastic Emission':e.plastic_emission,'Two Wheeler Emission':e.two_wheeler_emission,'Four Wheeler Emission':e.four_wheeler_emission,'Train Emission':e.train_emission,'Bus Emission':e.bus_emission}
        return render(req,"home/output.html",{'emission':emission,'d':d})
    else:
        return render(req,"home/form.html")

def calculate_footprint(fam,electricity,plastic,two_wheeler_no,two_wheeler_mlg,dist_2,four_wheeler_no,four_wheeler_mlg,dist_4,dist_train,dist_bus,trees):
    electricity_emission= 0.83 * electricity * (12/1000)/fam
    plastic_emission=6*plastic*(12/1000)
    two_wheeler_emission=(dist_2/two_wheeler_mlg)*two_wheeler_no*2.296* (12/1000)
    four_wheeler_emission=(dist_4/four_wheeler_mlg)*two_wheeler_no*2.4745*(12/1000)
    dist_train_emission= 0.018 * dist_train*(12/1000)
    bus_ef = 0.02353 * (dist_bus/100) + 0.029 * (dist_bus/100)
    dist_bus_emission= bus_ef * dist_bus * (365/1000)
    trees_emission=21.7724*trees/1000
    e=Emission()
    e.electricity_emission=electricity_emission
    e.plastic_emission=plastic_emission
    e.two_wheeler_emission=two_wheeler_emission
    e.four_wheeler_emission=four_wheeler_emission
    e.train_emission=dist_train_emission
    e.bus_emission=dist_bus_emission
    e.trees_absorption=trees_emission
    e.save()
    return (electricity_emission+plastic_emission+two_wheeler_emission+four_wheeler_emission+dist_train_emission+dist_bus_emission-trees_emission)

def index(req):
    return render(req,"home/index.html")