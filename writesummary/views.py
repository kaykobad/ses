from django.shortcuts import render
from .models import NewSummary


# Create your views here.
def writesummary(request):
    if request.method == 'POST':
        aid = request.POST['aid']
        summary = request.POST['summary']

        # update database
        NewSummary.objects.filter(id = aid).update(summary=summary, is_summarized=1)

        return render(request, 'writesummary/writesummary.html', {'info': 'thanks'})
    else:
        # get a non summarized article
        articles = NewSummary.objects.filter(is_summarized=0).order_by('?')

        if not articles:
            return render(request, 'writesummary/writesummary.html', {'info': 'none'})
        else:
            article = articles.first()
            return render(request, 'writesummary/writesummary.html', {'article': article, 'info': 'fresh'})
