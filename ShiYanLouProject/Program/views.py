from django.shortcuts import render, HttpResponse, redirect
from Program.models import *
import random
# Create your views here.
def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    return render(request,'index.html')

def andPlan(request):
    for i in range(10000):
        plan = Plan()
        plan_level = ['入门', '初级工程师', '中级工程师', '高级工程师']
        plan_project = ['python', 'php', 'java', 'linux', 'UI', '信息安全', 'c++', 'Nodejs']
        name = random.choice(plan_project) + random.choice(plan_level)
        plan.name = name
        plan.description = "%s 真的好" % name
        plan.image = "img/%s.png" % (random.randint(100, 999))
        plan.save()
    return HttpResponse('注册完成')
from pypinyin import lazy_pinyin
def addUser(request):
    for i in range(10000):
        first_name = '''澄邈、德泽、海超、海阳、海荣、海逸、海昌、瀚钰、瀚文、涵亮、涵煦、明宇、涵衍、浩皛、浩波、浩博、浩初、浩宕、浩歌、浩广、浩邈、浩气、浩思、浩言、鸿宝、鸿波、鸿博、鸿才、鸿畅、鸿畴、鸿达、鸿德、鸿飞、鸿风、鸿福、鸿光、鸿晖、鸿朗、鸿文、鸿轩、鸿煊、鸿骞、鸿远、鸿云、鸿哲、鸿祯、鸿志、鸿卓、嘉澍、光济、澎湃、彭泽、鹏池、鹏海、浦和、浦泽、瑞渊、越泽、博耘、德运、辰宇、辰皓、辰钊、辰铭、辰锟、辰阳、辰韦、辰良、辰沛、晨轩、晨涛、晨濡、晨潍、鸿振、吉星、铭晨、起运、运凡、运凯、运鹏、运浩、运诚、运良、运鸿、运锋、运盛、运升、运杰、运珧、运骏、运凯、运乾、维运、运晟、运莱、运华、耘豪、星爵、星腾、星睿、星泽、星鹏、星然、震轩、震博、康震、震博、振强、振博、振华、振锐、振凯、振海、振国、振平、昂然、昂雄、昂杰、昂熙、昌勋、昌盛、昌淼、昌茂、昌黎、昌燎、昌翰、晨朗、德明、德昌、德曜、范明、飞昂、高旻、晗日、昊然、昊天、昊苍、昊英、昊宇、昊嘉、昊明、昊伟、昊硕、昊磊、昊东、鸿晖、鸿朗、华晖、金鹏、晋鹏、敬曦、景明、景天、景浩、俊晖、君昊、昆琦、昆鹏、昆纬、昆宇、昆锐、昆卉、昆峰、昆颉、昆谊、昆皓、昆鹏、昆明、昆杰、昆雄、昆纶、鹏涛、鹏煊、曦晨、曦之、新曦、旭彬、旭尧、旭鹏、旭东、旭炎、炫明、宣朗、学智、轩昂、彦昌、曜坤、曜栋、曜文、曜曦、曜灿、曜瑞、智伟、智杰、智刚、智阳、昌勋、昌盛、昌茂、昌黎、昌燎、昌翰、晨朗、昂然、昂雄、昂杰、昂熙、范明、飞昂、高朗、高旻、德明、德昌、德曜、智伟、智杰、智刚、智阳、瀚彭、旭炎、宣朗、学智、昊然、昊天、昊苍、昊英、昊宇、昊嘉、昊明、昊伟、鸿朗、华晖、金鹏、晋鹏、敬曦、景明、景天、景浩、景行、景中、景逸、景彰、昆鹏、昆明、昆杰、昆雄、昆纶、鹏涛、鹏煊、景平、俊晖、君昊、昆琦、昆鹏、昆纬、昆宇、昆锐、昆卉、昆峰、昆颉、昆谊、轩昂、彦昌、曜坤、曜文、曜曦、曜灿、曜瑞、曦晨、曦之、新曦、鑫鹏、旭彬、旭尧、旭鹏、旭东、浩轩、浩瀚、浩慨、浩阔、鸿熙、鸿羲、鸿禧、鸿信、泽洋、泽雨、哲瀚、胤运、佑运、允晨、运恒、运发、云天、耘志、耘涛、振荣、振翱、中震、子辰、晗昱、瀚玥、瀚昂、瀚彭、景行、景中、景逸、景彰、绍晖、文景、曦哲、永昌、子昂、智宇、智晖、晗日、晗昱、瀚昂、昊硕、昊磊、昊东、鸿晖、绍晖、文昂、文景、曦哲、永昌、子昂、智宇、智晖、浩然、鸿运、辰龙、运珹、振宇、高朗、景平、鑫鹏、昌淼、炫明、昆皓、曜栋、文昂、澄邈、德泽、海超、海阳、海荣、海逸、海昌、瀚钰、瀚文、涵亮、涵煦、明宇、涵衍、浩皛、浩波、浩博、浩初、浩宕、浩歌、浩广、浩邈、浩气、浩思、浩言、鸿宝、鸿波、鸿博、鸿才、鸿畅、鸿畴、鸿达、鸿德、鸿飞、鸿风、鸿福、鸿光、鸿晖、鸿朗、鸿文、鸿轩、鸿煊、鸿骞、鸿远、鸿云、鸿哲、鸿祯、鸿志、鸿卓、嘉澍、光济、澎湃、彭泽、鹏池、鹏海、浦和、浦泽、瑞渊、越泽、博耘、德运、辰宇、辰皓、辰钊、辰铭、辰锟、辰阳、辰韦、辰良、辰沛、晨轩、晨涛、晨濡、晨潍、鸿振、吉星、铭晨、起运、运凡、运凯、运鹏、运浩、运诚、运良、运鸿、运锋、运盛、运升、运杰、运珧、运骏、运凯、运乾、维运、运晟、运莱、运华、耘豪、星爵、星腾、星睿、星泽、星鹏、星然、震轩、震博、康震、震博、振强、振博、振华、振锐、振凯、振海、振国、振平、昂然、昂雄、昂杰、昂熙、昌勋、昌盛、昌淼、昌茂、昌黎、昌燎、昌翰、晨朗、德明、德昌、德曜、范明、飞昂、高旻、晗日、昊然、昊天、昊苍、昊英、昊宇、昊嘉、昊明、昊伟、昊硕、昊磊、昊东、鸿晖、鸿朗、华晖、金鹏、晋鹏、敬曦、景明、景天、景浩、俊晖、君昊、昆琦、昆鹏、昆纬、昆宇、昆锐、昆卉、昆峰、昆颉、昆谊、昆皓、昆鹏、昆明、昆杰、昆雄、昆纶、鹏涛、鹏煊、曦晨、曦之、新曦、旭彬、旭尧、旭鹏、旭东、旭炎、炫明、宣朗、学智、轩昂、彦昌、曜坤、曜栋、曜文、曜曦、曜灿、曜瑞、智伟、智杰、智刚、智阳、昌勋、昌盛、昌茂、昌黎、昌燎、昌翰、晨朗、昂然、昂雄、昂杰、昂熙、范明、飞昂、高朗、高旻、德明、德昌、德曜、智伟、智杰、智刚、智阳、瀚彭、旭炎、宣朗、学智、昊然、昊天、昊苍、昊英、昊宇、昊嘉、昊明、昊伟、鸿朗、华晖、金鹏、晋鹏、敬曦、景明、景天、景浩、景行、景中、景逸、景彰、昆鹏、昆明、昆杰、昆雄、昆纶、鹏涛、鹏煊、景平、俊晖、君昊、昆琦、昆鹏、昆纬、昆宇、昆锐、昆卉、昆峰、昆颉、昆谊、轩昂、彦昌、曜坤、曜文、曜曦、曜灿、曜瑞、曦晨、曦之、新曦、鑫鹏、旭彬、旭尧、旭鹏、旭东、浩轩、浩瀚、浩慨、浩阔、鸿熙、鸿羲、鸿禧、鸿信、泽洋、泽雨、哲瀚、胤运、佑运、允晨、运恒、运发、云天、耘志、耘涛、振荣、振翱、中震、子辰、晗昱、瀚玥、瀚昂、瀚彭、景行、景中、景逸、景彰、绍晖、文景、曦哲、永昌、子昂、智宇、智晖、晗日、晗昱、瀚昂、昊硕、昊磊、昊东、鸿晖、绍晖、文昂、文景、曦哲、永昌、子昂、智宇、智晖、浩然、鸿运、辰龙、运珹、振宇、高朗、景平、鑫鹏、昌淼、炫明、昆皓、曜栋、文昂、'''.split('、')
        last_name = '''赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方'''
        nickname = random.choice(last_name)+random.choice(first_name)
        e_name = ' '.join(lazy_pinyin(nickname)).title().replace(' ','')
        email = '%sqq.com'%e_name
        password = e_name
        user = User()
        user.nickname = nickname
        user.email = email
        user.password = password
        user.plan = random.choice(Plan.objects.filter(id__lt=100))
        user.save()

    return HttpResponse('注册完成')

def addLesson(request):
    for i in range(10000):
        Lesson_level = ['入门', '初级工程师', '中级工程师', '高级工程师']
        Lesson_project = ['python', 'php', 'java', 'linux', 'UI', '信息安全', 'c++', 'Nodejs']
        lable = random.choice(Lesson_project)+random.choice(Lesson_level)
        lesson = Lesson()
        lesson.lable = lable
        lesson.picture = 'img/%s.png'%(random.randint(100,999))
        lesson.show_number = random.randint(1,9999999)
        lesson.save()
        for i in range(random.randint(2,7)):
            lesson.plan.add(
                random.choice(Plan.objects.filter(id__lt=100))
            )
        lesson.save()

    return HttpResponse('注册完成')

def select(request):
    # user_list = User.objects.all()
    # user = User.objects.get(id=5)
    # plan = Plan.objects.get(id=14).user_set.all()
    # lesson = Plan.objects.get(id=3).lesson_set.all()
    plan = User.objects.get(nickname='金昊宇').plan.name
    print(plan)
    print(type(plan))
    return HttpResponse('1111')

    # return render(request, 'empty.html', locals())


def Post(request):
    # if request.method == 'POST':
    #     name = request.POST.get('username')
    #     pwd = request.POST.get('pwd')
    #     print(name, pwd)
    nickname = User.objects.get(nickname='孙鸿文')
    print(nickname.id)
    return render(request,'empty1.html', locals())

import hashlib
def jiami(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


def Login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        picture = request.FILES.get('picture')

        user = LoginUser()
        user.name = name
        user.email = email
        user.password = jiami(password)
        user.picture = picture
        user.save()
        return redirect('/index/')
    return render(request,'login.html')



def index1(request):

    # ret = User.objects.raw('select * from Program_user ')
    # print(type(ret))
    # for i in ret:
    #     print(i)

    #
    # lesson = User.objects.get(nickname='柏子昂').plan.name
    # print(lesson)
    # lesson = Plan.objects.get(id=3).lesson_set.all()
    # print(lesson)

    return HttpResponse('xxxx')




