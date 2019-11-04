from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    worldlist = fulltext.split()

    word_dic = {}

    for word in worldlist:
        if word in word_dic:
            #Increase Here
            word_dic[word] +=1
        else:
            # Add to dictionary
            word_dic[word] = 1

    sorted_words = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(worldlist), 'sorted_words':sorted_words})

def about(request):
    return render(request, 'about.html')
