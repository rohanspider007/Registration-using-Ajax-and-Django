from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from pro.models import registration


def index(request):
    obj = registration.objects.all()
    return render(request, 'pro/index.html', {'obj': obj})


i = 0
def load_fetchState(request):
    # global i
    name = request.GET.get('val1')
    val = request.GET.get('val2')

    # name = request.POST['val1']
    # val = request.POST['val2']
    #
    # print(name)
    # print(val)
    # i = i+1
    # if i > 5:
    #     i = 0

    if name != "" and val != "":
        obj = registration(First_name=name, Last_name=val)
        obj.save()
    else:
        obj = registration.objects.all()
    user = {'id': obj.id, 'First_name': obj.First_name, 'Last_name': obj.Last_name, 'len': i}
    # print(len(user))
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
