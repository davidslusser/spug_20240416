import httpx
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpRequest, HttpResponse

from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import MyForm


class Index(TemplateView):
    template_name = "index.html"


class ExampleOne(TemplateView):
    template_name = "example_one.html"


class ExampleTwo(TemplateView):
    template_name = "example_two.html"


def ExampleThree(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            object = form.save()
            context = {"object": object}
            return render(request, "partials/form_success.htm", context)
    else:
        print("TEST: in submit_form()")
        form = MyForm()
    return render(request, "example_three.html", {"form": form})


def ExampleFour(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            object = form.save()
            context = {"object": object, "count": form.Meta.model.objects.count()}
            return render(request, "partials/form_success.htm", context)
    else:
        print("TEST: in submit_form()")
        form = MyForm()
        context = {"form": form, "count": form.Meta.model.objects.count()}
    return render(request, "example_four.html", context)


def get_time(request: HttpRequest) -> HttpResponse:
    print("TEST: in get_time()")
    context = {"timestamp": timezone.now().isoformat()}
    return render(request, "partials/get_time.htm", context=context)


def get_joke(request: HttpRequest) -> HttpResponse:
    print("TEST: in get_joke()")
    resp = httpx.get("https://api.chucknorris.io/jokes/random")
    text_content = resp.json()["value"]
    return HttpResponse(text_content, content_type="text/plain")
