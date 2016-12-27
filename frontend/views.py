from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import BusStopForm

from core.models import Profile, BusStop

def index(request):
    if request.user.is_authenticated():
      return render(request, "frontend/profile.html")
    else:
      return render(request, "frontend/index.html")


class BusStopCreate(LoginRequiredMixin, CreateView):
  model = BusStop
  form_class = BusStopForm
  # why doesn't this template work?
  template_name = 'frontend/addstop.html'
  login_url = '/login'
  redirect_field_name = None

  # todo - S.O. note
  def form_valid(self, form):
      stop = form.save(commit=False)
      stop.owner = Profile.objects.get(user=self.request.user)  # use your own profile here
      stop.save()
      return HttpResponseRedirect(reverse_lazy('index'))


