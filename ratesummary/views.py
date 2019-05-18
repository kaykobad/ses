from django.shortcuts import render
from . models import Document, Rating
from django.db.models import F


# Create your views here.
def ratesummary(request):
    if request.method == 'POST':
        aid = request.POST['aid']
        com = float(request.POST['com_score'])
        wr = float(request.POST['wr_score'])
        tr = float(request.POST['tr_score'])

        # update database and increment count
        status = Rating.objects.create(aid=aid, com_score=com, wr_score=wr, tr_score=tr)

        # update avg scores
        article = Document.objects.get(id=aid)
        av_com = float(article.avg_com)
        av_wr = float(article.avg_wr)
        av_tr = float(article.avg_tr)
        count = float(article.num_rating)

        av_com = ((av_com*count) + com )/(count+1)
        av_wr = ((av_wr*count) + wr )/(count+1)
        av_tr = ((av_tr*count) + tr )/(count+1)

        count = count + 1

        Document.objects.filter(id = aid).update(avg_com=av_com, avg_wr=av_wr, avg_tr=av_tr, num_rating=count)

        #counter, created = Document.objects.get_or_create(id = aid)
        #counter.num_rating = F('num_rating') + 1
        #counter.save()

        return render(request, 'ratesummary/ratesummary.html', {'info': 'thanks'})
    else:
        # get a non rated article
        articles = Document.objects.order_by('?')

        if not articles:
            return render(request, 'ratesummary/ratesummary.html', {'info': 'none'})
        else:
            article = articles.first()
            return render(request, 'ratesummary/ratesummary.html', {'article': article, 'info': 'fresh'})
