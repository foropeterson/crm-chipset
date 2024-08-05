from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lead.models import Lead
from client.models import Client
from products.models import Product
from team.models import Team
from .models import *
@login_required


def dashboard(request):
    total_products = Product.objects.count()
    in_stock_count = Product.objects.filter(in_stock=True).count()
    out_of_stock_count = Product.objects.filter(in_stock=False).count()
    leads = Lead.objects.all()[:5]
    clients = Client.objects.all()[:5]

    context = {
        'total_products': total_products,
        'in_stock_count': in_stock_count,
        'out_of_stock_count': out_of_stock_count,
        'leads': leads,
        'clients': clients,
    }
    return render(request, 'dashboard/dashboard.html', context)