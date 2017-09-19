from django.shortcuts import render_to_response
import feedparser, datetime, time


def reconstruction(request):
    return render_to_response("reconstruction.html")


def index(request):
    c = {}
    d = feedparser.parse('https://www.facebook.com/feeds/page.php?id=316951838354717&format=rss20')
    entries = []
    months = 2
    # for entry in d.entries:
    #     if(datetime.datetime.fromtimestamp(time.mktime(entry.published_parsed)).month >= datetime.datetime.today().month - months):
    #         entries.append(entry.summary)
    c["entries"] = entries
    return render_to_response("index.html", c)


def about(request):
    return render_to_response("about.html")


def groups(request):
    return render_to_response("groups.html")


def events(request):
    return render_to_response("events.html")


def calendar(request):
    return render_to_response("calendar.html")


def contact(request):
    return render_to_response("contact.html")
