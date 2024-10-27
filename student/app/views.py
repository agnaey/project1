from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
std=[{'roll':'1','name':'agni','age':'21','place':'knr','email':'ag@ag.com','phone':'9887676564'}]
# Create your views here.
def index_page(request):
    return render(request, 'index.html')


def add_std(request):
    if request.method == 'POST':
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        age = request.POST.get('age')
        place = request.POST.get('place')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        std.append({'roll': roll, 'name': name, 'age': age, 'place': place,'email':email,'phone':phone})
        print(std)
        return redirect(index_page)
    return render(request, 'add.html',)

def view_std(req):
    data=std
    return render(req,'view.html',{'data':data})

def update_std(req):
    data=std
    return render(req,'update.html',{'data':data})

def edit_std(request,roll):
    for i in std:
        if i['roll']==roll:
            std=i
            
            if request.method=='POST':
                roll = request.POST('roll')
                name = request.POST('name')
                age = request.POST('age')
                place = request.POST('place')
                email = request.POST('email')
                phone = request.POST('phone')
                std['roll']=roll
                std['name']=name
                std['age']=age
                std['place']=place
                std['email']=email
                std['phone']=phone
                return redirect(update_std)
    return render(request,'edit.html',{'std':std})

def delete_std(request,roll):
    for i in std:
        if i['roll']==roll:
            std.remove(i)
    return redirect(update_std)

# def search_std(request,roll):
#     for i in std:
#         if i['roll']==roll:
#             std=i
#             return render(request,'search.html',{'std':std})


                                                                                                                           

