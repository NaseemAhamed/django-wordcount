from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter

def homepage(request):
    return render(request,'home.html',{'hithere':'its me'})

def count(request):
    fulltext=request.GET['fulltext']
    words=fulltext.split(' ')
    wordDictionary={}
    for word in words:
        if word in wordDictionary:
            wordDictionary[word]+=1
        else:
            wordDictionary[word]=1

    sortedDictionary=sorted(wordDictionary.items(),key=itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'totalcount':len(words),'sortedDictionary':sortedDictionary,'words':words})

def about(request):
    return render(request,'about.html')
