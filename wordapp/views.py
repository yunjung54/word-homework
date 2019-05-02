from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")
    
def about(request):
    return render(request,"about.html")
def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary={}
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
            
        else:
            word_dictionary[word] = 1

    return render(request,"count.html",{"fulltext":full_text, 'total':len(word_list),'dictionary':word_dictionary.items()})#키와 벨류값 변수와 데이터 라는뜻 큰따음표랑 짝은땀표랑 상관없덩 len도 파이썬함수 길이를 뜻함