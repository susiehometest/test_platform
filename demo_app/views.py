from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.


def hello(request):
    # return HttpResponse("hello,django")
    # 设置字体大小及红色
    # return HttpResponse('<h1 style="color:red">hello,django</h1>')
    # 设置字居中
    # return HttpResponse('<h1 style="color:red;text-align:center;margin-top:50px;">hello,django</h1>')
    # 添加文本框
    # 所有
    print(request.scheme)
    print(request.method)
    if request.method == "GET":
        return render(request, "demo_app/hello.html")
    if request.method == "POST":
        # 拿到post请求里的用户名密码
        user = request.POST.get("username")
        pswd = request.POST.get("password")
        print(user, pswd)
        if user == "admin" and pswd == "123":
            # return render(request, "demo_app/hello.html", {"hint":"登录成功"})
            return JsonResponse({"success": True, "message": "登录成功"})
        else:
            # return render(request, "demo_app/hello.html", {"hint": "登录失败"})
            return JsonResponse({"success": False, "message": "登录失败"})


def calculator(request):
    print(request.scheme)
    print(request.method)
    if request.method == "GET":
        return render(request, "demo_app/calculator.html")
    if request.method == "POST":
        # 拿到post请求里的a,b
        a = request.POST.get("number_a")
        b = request.POST.get("number_b")
        print(a, b)
        count = int(a)+int(b)
        return render(request, "demo_app/calculator.html", {"result": count})
