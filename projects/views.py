from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.text import slugify
from .models import Project, Comment
from .forms import CommentForm, CreateProjectForm


# Project list view
class ProjectList(generic.ListView):
    model = Project
    queryset = Project.objects.all().order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


# Detail project view
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
            new_comment.name = request.user
            new_comment.project = project
            new_comment.save()
            messages.success(request, 'Comment has been successfully created')

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


# Create project view
@login_required
def CreateProject(request):
    form = CreateProjectForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.developer = request.user
            form.instance.slug = slugify(request.POST.get('title'))
            form.save()
            messages.success(request, 'Project successfully saved')
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'project_create.html', context)


# Edit project view
@login_required
def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    if project.developer != request.user:
        messages.error(request, 'Access denied, this is not your project')
        return redirect('home')
    if request.method == 'POST':
        form = CreateProjectForm(
            request.POST or None, request.FILES or None, instance=project)
        if form.is_valid():
            form.instance.developer = request.user
            form.instance.slug = slugify(request.POST.get('title'))
            form.save()
            messages.success(request, 'project successfully edited')
            return redirect('project_detail', project.id, project.slug)
        messages.error(request, 'An error has occured, please try again.')

    form = CreateProjectForm(instance=project)
    context = {
        'form': form,
        'project': project,
    }

    return render(request, 'project_edit.html', context)


# Delete project view
@login_required
def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    if project.developer != request.user:
        messages.error(request, 'Access denied, this is not your project')
        return redirect('home')
    project.delete()
    messages.success(request, 'Project successfully deleted')
    return redirect('home')


# Edit comment view
@login_required
def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if comment.name != request.user:
        messages.error(request, 'Access denied, this is not your comment')
        return redirect('home')
    if request.method == 'POST':
        form = CommentForm(request.POST or None, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment successfully edited')
            return redirect(
                'project_detail', comment.project.id, comment.project.slug)
        messages.error(request, 'An error has occured, please try again.')

    form = CommentForm(instance=comment)
    context = {
        'form': form,
        'comment': comment,
    }

    return render(request, 'comment_edit.html', context)


# Delete comment view
@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    project = get_object_or_404(Project, id=comment.project.id)
    if comment.name != request.user:
        messages.error(request, 'Access denied, this is not your comment')
        return redirect('home')
    comment.delete()
    messages.success(request, 'Comment successfully deleted')
    return redirect('project_detail', project.id, project.slug)


# Project like view
def project_like(request, id, slug):
    project = get_object_or_404(Project, id=id)
    if project.likes.filter(id=request.user.id).exists():
        project.likes.remove(request.user)
        messages.success(request, "Removed from your Likes")
    else:
        project.likes.add(request.user)
        messages.success(request, "Added to your Likes")

    return redirect('project_detail', project.id, project.slug)
