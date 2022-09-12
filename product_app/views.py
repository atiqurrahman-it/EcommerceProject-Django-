from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404

from product_app.models import CommentForm,Comment


# Create your views here.


def comment_Add(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        post = CommentForm(request.POST)
        if post.is_valid():
            data = Comment()
            data.subject = post.cleaned_data['subject']
            data.comment = post.cleaned_data['comment']
            data.rating_review = post.cleaned_data['rating_review']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
