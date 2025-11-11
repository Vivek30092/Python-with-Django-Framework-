from django.shortcuts import render

def home(request):
    return render(request,"index.html",{"c":c})

def entry1(request):
    return render(request,"entry1.html")

def entry2(request):
    list1 = [10,20,30]
    print(list1)
    list1.append(40)
    print(list1)
    list1.append(50)
    print(list1)
    return render(request,"entry2.html",{"list1":list1})

def entry3(request):
    if request.method == "GET":
        return render(request,"entry3.html")
    
    else:
        x = request.POST.get("n")
        print("x=",x)
        return render(request,"entry3.html")
    
def entry4(request):
    if request.method=="POST":
        a = request.POST.get("a")
        
