from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
monthly_challenges = {
    "january" : "You have to follow January rules",
    "february" : "You have to follow February rules",
    "march" : "You have to follow March rules",
    "april" : "You have to follow april rules",
    "may" : "You have to follow may rules",
    "june" : None,
    "july" : "You have to follow july rules",
    "august" : "You have to follow august rules",
    "september" : "You have to follow september rules",
    "october" : "You have to follow october rules",
    "november" : "You have to follow november rules",
    "december" : None
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html",{
        "months" :months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month!")
    else:
        redirect_month = months[month -1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    

def monthly_challenge(request, month):
    try:
        challenge_text  = monthly_challenges[month]
        return render(request, "challenges/challenge.html",{
                "text": challenge_text,
                "month_name" : month
        })
    except:
        render_data = render_to_string("404.html")
        return HttpResponseNotFound(render_data)
        # raise Http404()