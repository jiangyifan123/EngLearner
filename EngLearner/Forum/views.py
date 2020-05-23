from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from .forms import *
from django.http import JsonResponse
from users.models import UserProfile
import json
# Create your views here.

class forumView(View):
    def get(self, request):
        pages = Pages.objects.all()[:20]
        return render(request, 'Forum/forum.html', {"pages": pages})
    
    def post(self, request):
        return render(request, 'Forum/forum.html')

class detailView(View):
    def get(self, request, page_id):
        try:
            page = Pages.objects.get(id = page_id)
            page.views += 1
            count = len(page.likes_set.all())
            commends = page.commends_set.all()[:20]
            like_up = 0
            like_down = 0
            page.comment_num = commends.count()
            page.save()
            for like in page.likes_set.all():
                if like.operation == 1:
                    like_up += 1
                else:
                    like_down += 1
            commend_like = {
                "like_up": 0,
                "like_down": 0,
            }
            return render(request, 'Forum/detail_page.html', {"page": page, "count": count, "commends": commends, "like_up": like_up, "like_down": like_down})
        except Exception as e:
            print(e.args)
        return render(request, 'Forum/detail_page.html')
    
    def post(self, request, page_id):
        try:
            page = Pages.objects.get(id = page_id)
            username = request.POST.get('username')
            content = request.POST.get('content')
            commend = Commends()
            commend.content = content
            commend.username = username
            commend.page = page
            commend.save()
            return JsonResponse({"status": "success"})
        except Exception as e:
            print(e.args)
        return JsonResponse({"commend": "", "status": "Fail"})

class new_page_View(View):
    def get(self, request):
        return render(request, 'Forum/set_new_page.html')
    
    def post(self, request):
        new_page_form = New_page_form(request.POST)
        if new_page_form.is_valid():    
            try:
                title = request.POST.get('title')
                area  = request.POST.get('area')
                page = Pages()
                page.title = title
                page.content = area
                page.save()
                return redirect('forum_index')
            except Exception as e:
                print(e.args)
        else:
            error = ""
            print(new_page_form.errors.items())
            for key, errors in new_page_form.errors.items():
                if key == "title":
                    error += "标题: %s " % errors[0]
                else:
                    error += "内容: %s" % errors[0]
            return render(request, 'Forum/set_new_page.html', {'error': error})


def page_up_View(request):
    if request.method == 'GET' or not request.user.is_authenticated:
        return JsonResponse({'status': 'Fail'})
    else:
        try:
            page_id = request.POST.get('page_id')
            operation = request.POST.get('operation')
            page = Pages.objects.get(id = page_id)
            if page.likes_set.filter(user = request.user).exists():
                like = page.likes_set.get(user = request.user)
                print(operation == "0", like.operation)
                if operation == "1" and like.operation == False:
                    like.operation = True
                    like.save()
                elif operation == "0" and like.operation == True:
                    like.operation = False
                    like.save()
                    print(like.operation)
                else:
                    return JsonResponse({'status': 'Fail'})
                return JsonResponse({"status": "change"})
            else:
                like = likes()
                like.user = request.user
                like.page = page
                if operation == "1" and like.operation == False:
                    like.operation = True
                    like.save()
                elif operation == "0" and like.operation == True:
                    like.operation = False
                    like.save()
                else:
                    return JsonResponse({'status': 'Fail'})
                return JsonResponse({'status': 'success'})
        except Exception as e:
            print(e.args)
            return JsonResponse({'status': 'Fail'})

