# -*- coding=utf8 -*-
import pymysql
from django.shortcuts import HttpResponse,render,redirect
import json
from app import models

def get_str_btw(s, f, b):
    par = s.partition(f)
    return (par[2].partition(b))[0][:]

def demo(request):
    article_list = models.Article_Path.objects.all()
    if request.method == 'GET':
        # models.UserType.objects.create(type="普通游客")
        # models.UserType.objects.create(type="管理员")
        # models.UserType.objects.create(type="游客")
        # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='sr139.com', db='MDN', charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute('select id,title,path from article')
        # article_list = cursor.fetchall()
        # cursor.close()
        # conn.close()

        return render(request, 'demo.html',{'article_list':article_list})
    else:
        obj = render(request,'demo.html',{'article_list':article_list})
        name = request.COOKIES.get('name')
        if name:
            obj.delete_cookie('name')
            obj.delete_cookie('juris')
        return obj

def register(request):

    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        res = request.POST.get('res')
        nm = request.POST.get('user_name')
        pwd = request.POST.get('user_psw')
        rpsw = request.POST.get('user_rpsw')
        if res == "success":
            if rpsw == password:
                # conn = pymysql.connect(host = 'localhost',port = 3306,user='root',passwd='sr139.com',db='MDN',charset='utf8')
                # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
                # cursor.execute('insert into user(name,password,sex,point,juris,status,head_portrait) values(%s,%s,%s,%s,%s,%s,%s)',[name,password,'U','0','1','0','333',])
                # conn.commit()
                # cursor.close()
                # conn.close()
                models.UserInfo.objects.create(name=nm,password=pwd,sex="U",point=0,status=0,head_portrait=123123,juris_id=1)
                return render(request,'register.html',{'msg':'注册成功'})
            else:
                return render(request,'register.html',{'msg':"密码不一样"})
        else:
            return render(request,'register.html',{'msg':"验证码错误"})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('psw')
        # conn = pymysql.connect(host = 'localhost',port = 3306,user='root',passwd='sr139.com',db='MDN',charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute('select * from user')
        # user_info = cursor.fetchall()
        # cursor.close()
        # conn.close()
        user_info = models.UserInfo.objects.all()
        obj1 = redirect('/demo/')
        obj2 = redirect('/manager_menu/')
        for row in user_info:
            if name == row.name and password == row.password:
                if row.juris_id == 1:
                    obj1.set_cookie('juris',"1",max_age=60)
                    obj1.set_cookie('name' , name, max_age=60)
                    return obj1
                elif row.juris_id == 2:
                    obj2.set_cookie('juris',"2",max_age= 200)
                    obj2.set_cookie("name", name, max_age= 200)
                    return obj2
        return redirect('/login/')

def manager_menu(request):
    juris = request.COOKIES.get('juris')
    if juris == "2":
        # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='sr139.com', db='MDN', charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute('select * from user')
        # user_info = cursor.fetchall()
        # cursor.close()
        # conn.close()
        user_info = models.UserInfo.objects.all()
        if request.method == 'GET':
            return render(request,'manager_menu.html',{'user_info':user_info})
    else:
        return redirect("/login/")

def manager_add_user(request):
    juris = request.COOKIES.get('juris')
    if juris == "2":
        if request.method == 'GET':
            return render(request,'manager_add_user.html')
        else:
            nm = request.POST.get('name')
            pwd = request.POST.get('password')
            sex = request.POST.get('sex')
            point = request.POST.get('point')
            juris = request.POST.get('juris')
            status = request.POST.get('status')
            head_pt = request.POST.get('head_portrait')


            # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='sr139.com', db='MDN', charset='utf8')
            # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            # cursor.execute('insert into user(name,password,sex,point,juris,status,head_portrait) values(%s,%s,%s,%s,%s,%s,%s)',
            #                [name,password,sex,point,juris,status,head_portrait,])
            # conn.commit()
            # cursor.close()
            # conn.close()
            models.UserInfo.objects.create(name=nm, password=pwd, sex=sex, point=point, juris_id=juris, status=status,
                                           head_portrait=head_pt)
            return redirect('/manager_menu/')
    else:
        return redirect("/login/")

def manager_edit_user(request):
    juris = request.COOKIES.get('juris')
    if juris == "2":
        if request.method == 'GET':
            nid = request.GET.get('nid')
            # conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='sr139.com',db='MDN',charset='utf8')
            # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            # cursor.execute("select * from user where id=%s",[nid,])
            # result = cursor.fetchone()
            # cursor.close()
            # conn.close()
            result = models.UserInfo.objects.all()
            return render(request,'manager_edit_user.html',{'result':result})
        else:
            nid = request.POST.get('id')
            name = request.POST.get('name')
            sex = request.POST.get('sex')
            point = request.POST.get('point')
            juris = request.POST.get('juris')
            status = request.POST.get('status')
            head_pt = request.POST.get('head_portrait')

            # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='sr139.com', db='MDN',
            #                        charset='utf8')
            # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            # cursor.execute("update user set name=%s,sex=%s,point=%s,juris=%s,status=%s,head_portrait=%s where id=%s",
            # [name,sex,point,juris,status,head_portrait,nid, ])
            # conn.commit()
            # cursor.close()
            # conn.close()
            models.UserInfo.objects.filter(id=nid).update(name=name, sex=sex, point=point, juris_id=juris, status=status,
                                                          head_portrait=head_pt)
            return redirect('/manager_menu/')
    else:
        return redirect("/login/")

def manager_del_user(request):
    juris = request.COOKIES.get('juris')
    if juris=="2":
        nid = request.GET.get('nid')
        # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='sr139.com', db='MDN', charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute('delete from user where id=%s',[nid,])
        # conn.commit()
        # cursor.close()
        # conn.close()
        models.UserInfo.objects.filter(id=nid).delete()
        return redirect('/manager_menu/')
    else:
        return redirect("/login/")

def show_article(request):
    nid = request.GET.get('nid')
    # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='sr139.com', db='mdn', charset='utf8')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute('select title,path from article where id=%s',[nid,])
    # article = cursor.fetchone()
    # cursor.close()
    # conn.close()
    article = models.Article_Path.objects.filter(id=nid).first()

    title = article.title
    path = article.path
    with open(path,encoding='utf-8') as file_obj:
        content = file_obj.read()

    return render(request,'show_article.html',{'content':content,'title':title})

def write(request):
    if request.method == 'GET':
        juris = request.COOKIES.get('juris')
        if juris=="1":
            return render(request,'write.html')
        else:
            return redirect('/login/')
    else:
        article = request.POST.get('content')
        class1 = request.POST.get('class')
        #print(class1)
        title = get_str_btw(article, '>', '<')
        content = article.replace(title+"<br>","",1)
        file_name = title+".txt"
        path = "C:\\Users\\29164\\Desktop\\MDN\\article\\" + file_name

        with open('C:\\Users\\29164\\Desktop\\MDN\\article\\'+file_name,'w') as file_obj:
            file_obj.write(content)

        # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='sr139.com', db='MDN', charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute('insert into article(title,path,class) values(%s,%s,%s)',[title,path,class1,])
        # conn. commit()
        # cursor.close()
        # conn.close()
        models.Article_Path.objects.create(title=title,path=path,classes=class1)
        return redirect('/demo/')

def modal_add_user(request):        #模态对话框与ajax
    name = request.POST.get('name')
    password = request.POST.get("psw")
    if len(name)>0 and len(password)>0:
        # conn = pymysql.connect(host='localhost', port=3306, user='root', password='sr139.com', db='MDN', charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute(
        #     'insert into user(name,password,sex,point,juris,status,head_portrait) values(%s,%s,%s,%s,%s,%s,%s)',
        #     [name, password, 'U', '0', '1', '0', '333', ])
        # conn.commit()
        # cursor.close()
        # conn.close()
        models.UserInfo.objects.create(name=name,password=password,juris_id=1)
        return HttpResponse("ok")
    else:
        return HttpResponse("信息不能为空")

def modal_edit_user(request):
    ret = {'status':True,'msg':None}
    try:
        nid = request.POST.get('nid')
        name = request.POST.get('content')
        psw = request.POST.get('psw')

        # conn = pymysql.connect(host='localhost', port=3306, user='root', password='sr139.com', db='MDN', charset='utf8')
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # cursor.execute('update user set name=%s,password=%s where id=%s',[name,psw,nid,])
        # conn.commit()
        # cursor.close()
        # conn.close()
        models.UserInfo.objects.filter(id=nid).update(name=name,password=psw )
    except Exception as e:
        ret['status'] = False
        ret['msg'] = "处理异常"

    return HttpResponse(json.dumps(ret))

def mother_modal(request):
    return render(request,'mother_modal.html')



