from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from comments.models import Comment

class MyCommentsView(ListView):
    model = Comment
    template_name = "comments/my_comments.html"
    context_object_name = "comments"

    def get_queryset(self):
        comments = super().get_queryset()
        comments = comments.filter(author=self.request.user)
        return comments
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Мои комментарии"
        return context
    
def commentDelete(request, pk):
    Comment.objects.filter(id=pk).delete()
    return redirect(reverse(request.get_full_path()))