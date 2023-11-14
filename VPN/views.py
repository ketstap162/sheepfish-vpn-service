from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.template import Template, Context

from .models import Site
from .forms import SiteForm

# Create your views here.
from .site_processing import get_original_site_url, get_site_data, replace_urls, post_site_data


@login_required
def home_page_view(request):
    context = {
        "sites": Site.objects.filter(user=request.user),
    }
    return render(request, "VPN/home.html", context)


@login_required
def site_create_view(request):
    if request.method == "POST":
        form = SiteForm(request.POST, initial={"user": request.user})
        if form.is_valid():
            form_data = form.cleaned_data
            Site.objects.create(
                url=form_data["url"],
                alias=form_data["alias"],
                user=request.user
            )
            return redirect("VPN:home")
    else:
        form = SiteForm()
    return render(request, "VPN/site-create.html", {"form": form})


@login_required
def site_delete_view(request, pk: int):
    site = get_object_or_404(Site, pk=pk)
    if site.user == request.user:
        if request.method == "POST":
            site.delete()
            return redirect("VPN:home")
        return render(request, "VPN/site_confirm_delete.html", {"site": site})
    raise PermissionDenied("You don't have access to edit this site.")


@login_required
def vpn_view(request, site_url: str, path: str):
    allowed_methods = ["GET", "POST"]
    if request.method not in allowed_methods:
        return HttpResponseNotAllowed(allowed_methods)

    original_url = get_original_site_url(request.user, site_url, path)

    if request.method == "GET":
        data = get_site_data(original_url)

    else:
        data = post_site_data(original_url, request.POST)

    text = replace_urls(original_url, site_url, data["content"])
    template = Template(text)
    context = Context(data["headers"])
    return HttpResponse(template.render(context))
