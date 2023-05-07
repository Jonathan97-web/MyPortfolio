from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Project
from .forms import CommentForm


class ProjectList(generic.ListView):
    model = Project
    queryset = Project.objects.all().order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


def ProjectDetail(request, id, slug):
    template_name = 'project_detail.html'
    project = get_object_or_404(Project, id=id)
    comments = project.comments.filter(approved=True)
    new_comment = None
    liked = False
    if project.likes.filter(id=request.user.id).exists():
        liked = True
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.project = project
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "project": project,
            "comments": comments,
            "liked": liked,
            "new_comment": new_comment,
            "comment_form": comment_form,
        })
