import json

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "body", "is_public"]

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect("/home")


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "body", "is_public"]
    template_name_suffix = "_update_form"


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("home")


def is_public(request, pk):
    # should use DRF, but this will do for the mean time
    if request.is_ajax and request.method == "POST":
        obj = Post.objects.get(pk=pk)
        obj.is_public = json.loads(request.POST["is_public"])
        obj.save()

        return JsonResponse({"status": "Success", "msg": "Saved!"})
