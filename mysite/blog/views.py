#coding=utf-8
from django.shortcuts import render_to_response,HttpResponseRedirect,HttpResponse
from blog.models import Article,Comment



def comment_add(request):

    

    if request.method == 'POST':
        article_id = request.POST.get('article','')

        detail = request.POST.get('detail','')

        if article_id and detail :

            comment = Comment()
            comment.Article = Article(id=article_id)
            comment.detail = detail
            comment.save()


        return HttpResponseRedirect('/view/%s'%article_id)


def list(request):

    
    articles = Article.objects.order_by("-id").all()




    return render_to_response('list.html',{'articles':articles})


def view(request,id):
    article = Article.objects.get(id=id)

    comments = Comment.objects.filter(Article=id).order_by("-id").all()

    print len(comments)
    
    return render_to_response('view.html', {'article': article,'comments':comments})



def add(request):

    #判断是否是form表单提交上来
    if request.method == 'POST':

        #获取form提交的内容
        content = request.POST.get('content',None)
        title = request.POST.get('title',None)

        #写入
        new = Article(content=content,title=title)
        new.save()

        #跳转
        return HttpResponseRedirect('/list')


    return render_to_response('add.html',{'method_str':request.method})