from django.shortcuts import render
from utils import retrieve_gh, retrieve_gl, retrieve_bw


# Create your views here.
def index(request):
    return render(request, "home.html")


def repos(request):
    repos_gh = retrieve_gh.get_gh_repos()
    repos_gl = retrieve_gl.get_gl_repos()

    return render(request, "repos.html", {"repos_gh": repos_gh, "repos_gl": repos_gl})


def passwords(request):
    return render(request, "passwords.html", {"passwords": ["pass1", "pass2", "pass3"]})
