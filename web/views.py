# 文件：myapp/views.py 文件代码
import json

from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from web.models import CustomUser, Comic

User = get_user_model()


# Create your views here.
# {"username":"wen","password":"23","permission":0}
@csrf_exempt
def login(request):
    if request.method == 'POST':
        json_str = request.body.decode('utf-8')
        data = json.loads(json_str)
        username = data.get('userName')
        password = data.get('password')
        print(username)
        print(password)
        user = CustomUser.objects.filter(username=username, password=password).values('id', 'username', 'password',
                                                                                      'permission')

        if user.exists():
            user_list = []
            user_dict = {
                'id': user[0]['id'],
                'username': user[0]['username'],
                'password': user[0]['password'],
                'permission': user[0]['permission']
                # 将其他属性也加入字典中
            }
            user_list.append(user_dict)
            return JsonResponse({'data': user_list})
        else:
            return HttpResponse("400")
        # return HttpResponse('用户不存在')


@csrf_exempt
def find_userid(request):
    userid = request.GET.get('id')
    user = CustomUser.objects.filter(id=userid).values('id', 'username', 'password', 'permission')
    if user.exists():
        user_list = []
        user_dict = {
            'id': user[0]['id'],
            'username': user[0]['username'],
            'password': user[0]['password'],
            'permission': user[0]['permission']
            # 将其他属性也加入字典中
        }
        user_list.append(user_dict)
        return JsonResponse({'data': user_list})
    else:
        return HttpResponse("400")
        # return HttpResponse('用户不存在')


# {"username":"wen","password":"23","permission":0}
@csrf_exempt
def register(request):
    if request.method == 'POST':
        json_str = request.body.decode('utf-8')
        data = json.loads(json_str)
        username = data.get('userName')
        user1 = CustomUser.objects.filter(username=username)
        if user1.exists():
            return HttpResponse("400")
        else:
            password = data.get('password')
            permission = data.get('permission')
            CustomUser.objects.create(username=username, password=password, permission=permission)
            return HttpResponse("200")


@csrf_exempt
def mod(request):
    if request.method == 'POST':
        json_str = request.body.decode('utf-8')
        data = json.loads(json_str)
        user = CustomUser(id=data.get('id'), username=data.get('username'), password=data.get('password'),
                          permission=data.get("permission"))
        user.save()
        return HttpResponse("200")


@csrf_exempt
def delete(request):
    userid = request.GET.get('id')
    print(userid)
    user = CustomUser.objects.get(id=userid)
    user.delete()
    return HttpResponse("200")


@csrf_exempt
def find(request):
    if request.method == 'POST':
        json_str = request.body.decode('utf-8')
        data = json.loads(json_str)
        print(data)
        lists = CustomUser.objects.all()
        count = CustomUser.objects.all().count()
        # 当前页数
        page_number = data.get('currentPage')
        page_size = data.get('pageSize')
        paginator = Paginator(lists, page_size)
        page_list = paginator.get_page(page_number)
        print(page_list)
        user_list = []
        for user in page_list:
            user_dict = {
                'id': user.id,
                'username': user.username,
                'password': user.password,
                'permission': user.permission
                # 将其他属性也加入字典中
            }
            user_list.append(user_dict)
    return JsonResponse({'data': user_list, 'total': count})


# def stu(request):
#     # 获取所有stu表信息
#     lists = Login.objects.all()
#     print(lists)
#     # 获取单条学生信息
#     print(Login.objects.get(id=1))
#     return HttpResponse(lists)
@csrf_exempt
def find_comic(request):
    if request.method == 'POST':
        json_str = request.body.decode('utf-8')
        data = json.loads(json_str)
        print(data)
        lists = Comic.objects.all()
        count = Comic.objects.all().count()
        print(count)
        # 当前页数
        page_number = data.get('currentPage')
        page_size = data.get('pageSize')
        print(page_number)
        paginator = Paginator(lists, page_size)
        page_list = paginator.get_page(page_number)
        comic_list = []
        for comic in page_list:
            user_dict = {
                'id': comic.id,
                'comicName': comic.comicName,
                'nickname': comic.nickname,
                'cover': comic.cover,
                'region': comic.region,
                'label': comic.label,
                'description': comic.description,
                'remark': comic.remark,
                'year': comic.year,
                'updateTime': comic.updateTime,
                'number': comic.number,
                'popularity': comic.popularity,
                'url': comic.url
                # 将其他属性也加入字典中
            }
            comic_list.append(user_dict)
    return JsonResponse({'data': comic_list, 'total': count})


@csrf_exempt
def find_index(request):
    lists = Comic.objects.all()
    # 当前页数
    paginator = Paginator(lists, 5)
    page_list = paginator.get_page(1)
    comic_list = []
    for comic in page_list:
        user_dict = {
            'id': comic.id,
            'comicName': comic.comicName,
            'nickname': comic.nickname,
            'cover': comic.cover,
            'region': comic.region,
            'label': comic.label,
            'description': comic.description,
            'remark': comic.remark,
            'year': comic.year,
            'updateTime': comic.updateTime,
            'number': comic.number,
            'popularity': comic.popularity,
            'url': comic.url
            # 将其他属性也加入字典中
        }
        comic_list.append(user_dict)
    return JsonResponse({'data': comic_list})


@csrf_exempt
def find_key(request):
    if request.method == 'POST':
        json_str = request.body.decode('utf-8')
        data = json.loads(json_str)
        print(data)
        lists = Comic.objects.order_by('id').filter(
            Q(comicName__icontains=data.get('keyword')) | Q(label__icontains=data.get('keyword')) |
            Q(region__icontains=data.get('keyword')))
        print(lists)
        count = Comic.objects.filter(
            Q(comicName__icontains=data.get('keyword')) | Q(label__icontains=data.get('keyword')) |
            Q(region__icontains=data.get('keyword'))).count()
        # 当前页数
        page_number = data.get('currentPage')
        print(page_number)
        paginator = Paginator(lists, 10)
        page_list = paginator.get_page(page_number)
        comic_list = []
        for comic in page_list:
            user_dict = {
                'id': comic.id,
                'comicName': comic.comicName,
                'nickname': comic.nickname,
                'cover': comic.cover,
                'region': comic.region,
                'label': comic.label,
                'description': comic.description,
                'remark': comic.remark,
                'year': comic.year,
                'updateTime': comic.updateTime,
                'number': comic.number,
                'popularity': comic.popularity,
                'url': comic.url
                # 将其他属性也加入字典中
            }
            comic_list.append(user_dict)
    return JsonResponse({'data': comic_list, 'total': count})


@csrf_exempt
def find_id(request):
    comicId = request.GET.get('id')
    print(comicId)
    comic = Comic.objects.filter(id=comicId).values('id', 'comicName', 'nickname', 'cover',
                                                    'region', 'label', 'description', 'remark',
                                                    'year', 'updateTime', 'number', 'popularity', 'url')
    if comic.exists():
        comic1 = []
        comic_dict = {
            'id': comic[0]['id'],
            'comicName': comic[0]['comicName'],
            'nickname': comic[0]['nickname'],
            'cover': comic[0]['cover'],
            'region': comic[0]['region'],
            'label': comic[0]['label'],
            'description': comic[0]['description'],
            'remark': comic[0]['remark'],
            'year': comic[0]['year'],
            'updateTime': comic[0]['updateTime'],
            'number': comic[0]['number'],
            'popularity': comic[0]['popularity'],
            'url': comic[0]['url']
        }
        comic1.append(comic_dict)
        return JsonResponse({'data': comic1})
    else:
        return HttpResponse("400")


@csrf_exempt
def delete_comic(request):
    comicId = request.GET.get('id')
    print(comicId)
    comic = Comic.objects.get(id=comicId)
    comic.delete()
    return HttpResponse("200")


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        # 获取上传的图片
        uploaded_image = request.FILES['image']
        # 创建文件系统存储对象
        fs = FileSystemStorage(location='static/photo')
        # 将文件保存到指定文件夹中
        filename = fs.save(uploaded_image.name, uploaded_image)
        # 获取保存的文件的URL并将其传递到模板中进行渲染
        filename1 = "/static/photo" + fs.url(filename)
        return JsonResponse({'data': filename1, 'code': 200})


# {"id":"31","comicName":"测试的","nickname":"测试的","cover":"/static/image/19925177615373f1a1c94ff121df3273_5gL2mN1.png","region":"测试的","label":"Ces1d1","description":"sssssd","remark":"sfsfsfsfs","year":"sfsfafasfas","updateTime":"sfafasfas","number":"1221","popularity":"155515","url":"asfasfasf"}
@csrf_exempt
def add_comic(request):
    if request.method == 'POST':
        json_str = request.body.decode('utf-8')
        data = json.loads(json_str)
        if data.get('id') == 0:
            comic = Comic(comicName=data.get('comicName'),
                          nickname=data.get('nickname'),
                          cover=data.get('cover'),
                          region=data.get('region'),
                          label=data.get('label'),
                          description=data.get('description'),
                          remark=data.get('remark'),
                          year=data.get('year'),
                          updateTime=data.get('updateTime'),
                          number=data.get('number'),
                          popularity=data.get('popularity'),
                          url=data.get('url')
                          )
        else:
            comic = Comic(id=data.get('id'),
                          comicName=data.get('comicName'),
                          nickname=data.get('nickname'),
                          cover=data.get('cover'),
                          region=data.get('region'),
                          label=data.get('label'),
                          description=data.get('description'),
                          remark=data.get('remark'),
                          year=data.get('year'),
                          updateTime=data.get('updateTime'),
                          number=data.get('number'),
                          popularity=data.get('popularity'),
                          url=data.get('url')
                          )
        comic.save()
        return HttpResponse("200")
