from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Project, Comment
from .forms import CommentForm, CreateProjectForm
from django.contrib.auth.models import User


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

            new_comment = comment_form.save(commit=False)
            new_comment.project = project
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


def CreateProject(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('account_signup')

    form = CreateProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Project.objects.filter(developer=user).first()
        obj.author = author
        obj.save()
        form = CreateProjectForm()

    context['form'] = form

    return render(request, 'project_create.html', context)
