from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pro/index.html')


i = 0
def load_fetchState(request):
    global i
    name = request.GET.get('val1')
    val = request.GET.get('val2')
    print(name)
    print(val)
    i = i+1
    if i > 5:
        i = 0
    user = {'name': name, 'val': val, 'len': i}
    print(len(user))
    data = {
        'user': user
    }
    return JsonResponse(data)

# wihtout json
# def load_fetchState(request):
#     name = request.GET.get('val1')
#     val = request.GET.get('val2')
#     print(name)
#     print(val)
#
#     return render(request, 'pro/index.html', {'name': name, 'val': val})
