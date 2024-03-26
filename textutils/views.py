from django.shortcuts import render
from django.http import HttpResponse
import string


def index(request):
    return render(request,'index.html')

# def removepunc(request):
#     return HttpResponse("Hello")

# def capall(request):
#     return HttpResponse("YELLOW")

def analyse(request):
# Take Text Input
    text=request.GET.get('textbox','default')

# Get Button Value
    removepunc=request.GET.get('Remove','off')
    newline=request.GET.get('NewLineRemove','off')
    uppercase=request.GET.get('UpperCase','off')
    spaceremover=request.GET.get('SpaceRemover','off')

# Remove Puncation If button is on
    if removepunc=="on":
        punctuations=string.punctuation
        analyzed=''
        for char in text:
            if char not in punctuations:
                analyzed+=char    

    # NewLine Remover
    elif newline=="on":
        analyzed=""
        for char in text:
            if char !="\n":
                analyzed+=char

    # UpperCase
    elif uppercase=="on":
        analyzed=""
        for char in text:
            analyzed+=char.upper()

    # SpaceRemover
    elif spaceremover=="on":
        analyzed=""
        for index,char in enumerate(text):
            # if text[index]==" " and text[index+1]==" ":
            #     pass
            # else:
            if text[index]==" ":
                analyzed+=char
    
            

    else:        
        text=analyzed="N/A"
    
    data={"removed":removepunc,"newline":newline,'uppercase':uppercase,'spaceremover':spaceremover, 'input':text,'output':analyzed}

    # removepuncation=request.GET.get('Remove','off')
    # return HttpResponse("YELLOW","removepuncation")


# Parameters and Variables
# Render the output website
    # print(data)
    return render(request,'analyze.html',data)