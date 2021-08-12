from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string

weekly_challenges={
    'monday':"Eat healthy ,Stay hydrated",
    'tuesday':"Walk fo 20 min",
    'wednesday':"Attend yoga class",
    'thrusday':"Start working out",
    'friday':"Get some rest and sleep",
    'saturday':"Hangout wih friends",
    'sunday': None 
}
def index(request):
    '''list_items=""'''
    weeks=list(weekly_challenges.keys())
    return render(request,"weekly_challenges/index.html",{"days":weeks})

    '''for week in weeks:
        captialized_week=week.capitalize()
        rediect_path=reverse("week-challenge",args=[week])
        list_items+=f"<li><a href=\"{rediect_path}\">{captialized_week}</a></li>"
    reponse_data=f"<ul><h1>{list_items}</h1></ul>"
    return HttpResponse(reponse_data)'''

def weekly_challenge(request,week):
    try:
        challenge_text=weekly_challenges[week]
        letter=week
        return render(request,"weekly_challenges/weekly_challenge.html",{"text":challenge_text,"title":letter})
        '''response_data=render_to_string("weekly_challenges/weekly_challenge.html") //longway of rendering html
        respone_data=f"<h1>{challenge_text}</h1>   //single and simple addition of html style
        return HttpResponse(response_data)'''
    except:
        return HttpResponseNotFound("<h1>sorry this was not valid</h1>")

def weekly_in_number(request,week):
    try:
        weeks=list(weekly_challenges.keys())
        redriect_week=weeks[week-1]
        rediect_path=reverse("week-challenge",args=[redriect_week])
        return HttpResponseRedirect(rediect_path)
    except:
        raise Http404()

