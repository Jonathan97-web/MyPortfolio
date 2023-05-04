from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Project


class ProjectList(generic.ListView):
    model = Project
    queryset = Project.objects.all().order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ProjectDetail(View):

    def get(self, request, id, slug, *args, **kwargs):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, id=id)
        comments = project.comments.filter(approved=True).order_by('created_on')
        liked = False
        if project.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "project_detail.html",
            {
                "project": project,
                "comments": comments,
                "liked": liked
            },
        )
