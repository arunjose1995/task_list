from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# Load Home View
class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('Login')
        else:
            return render(request, self.template_name)
