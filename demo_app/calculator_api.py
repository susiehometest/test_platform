from django.http import JsonResponse
from django.shortcuts import render


def add(request):
    """
    计算加法
    """
    if request.method == "POST":
        # 拿到post请求里的a,b
        a = request.POST.get("number_a", "")
        b = request.POST.get("number_b", "")
        if a == "" or b == "":
            return JsonResponse({"success": False, "message": "请求错误，参数为空"})
        print(a, b)
        count = int(a)+int(b)
        return JsonResponse({"success": True, "message": "", "data": {"count": count}})
    else:
        return JsonResponse({"success": False, "message": "请求方法错误"})
