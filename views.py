from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenges = {
    "january": "January url works !",
    "february": "February url works !",
    "march": "March url works !",
    "april": "April url works !",
    "may": "May url works !",
    "june": "June url works !",
    "july": "July url works !",
    "august": "August url works !",
    "september": "September url works !",
    "october": "October url works !",
    "december": "November url works !",
    "november": "December url works !",
}


# Create your views here.
def index(request):
    list_items = ""
    months = list(challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-challenges", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    return HttpResponse(list_items)


def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("This month doesn't exist !")

    forward_month = months[month - 1]
    return HttpResponseRedirect("/challenges_app" + forward_month)


def all_months(request, month):
    try:
        text = challenges[month]
        response_data = f"<h1>{text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported !</h1>")
