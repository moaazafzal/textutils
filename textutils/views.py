from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    djtext=request.GET.get('text','default')
    isremove_pun=request.GET.get('removepunc','off')
    uppercase=request.GET.get('capitilze','off')
    removespace = request.GET.get('removespace', 'off')
    countwords = request.GET.get('countwords', 'off')
    print(djtext)
    print(isremove_pun)
    analyzed=''
    if isremove_pun=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}


        return render(request,'analyze.html',params)
    elif(uppercase=='on'):
        analyzed=''
        for char in djtext:
          analyzed=analyzed+char.upper()
        params={'purpose':'Capitalized ','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(removespace=="on"):
        analyzed=''
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext [index+1]==" "):
                analyzed+=char
        params={'purpose':'removespace','analyzed_text':analyzed}
        return  render(request,'analyze.html',params)
    elif(countwords=="on"):
     # print(str(len(djtext)) +'aaa')
     params={'purpose':'No of char are :','analyzed_text':len(djtext)}
     return  render(request,'analyze.html',params)





    else:
        return HttpResponse("error")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newline remove first")


def spaceremove(request):
    return HttpResponse("space remover back")

def charcount(request):
    return HttpResponse("charcount ")