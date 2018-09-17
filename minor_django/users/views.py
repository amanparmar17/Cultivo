from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import is_safe_url
from django.shortcuts import resolve_url
from django.views.generic.base import View
from django.template.response import TemplateResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import redirect
from django.db import IntegrityError
from user.models import Profile
from mentor.models import Mentor
from center.models import Center
from utils.general import ( create_activation_key, get_uid)
from post_office import mail
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.views import logout
from utils.general import (pagination, check_authentication)
from django.utils.decorators import method_decorator



@login_required
# def render_main_page(request, next_url=None):
# 	user = request.user
# 	if user.is_authenticated():
# 		if user.profile.flags.is_mentor:
# 			return render_to_response(
# 				'dashboard/dashboard_mentor.html',
# 				context_instance=RequestContext(request))
# 		elif user.profile.flags.is_mentee:
# 			return render_to_response(
# 				'dashboard/dashboard_mentee.html',
# 				context_instance=RequestContext(request))
# 		elif user.profile.flags.is_staff:
# 			return render_to_response(
# 				'dashboard/dashboard_staff.html',
# 				context_instance=RequestContext(request))
# 		elif user.profile.flags.is_center:
# 			return redirect('center_dashboard')
# 		else:
# 			raise Http404
			

# def login(request, template_name='registration/login.html',
# 		redirect_field_name=REDIRECT_FIELD_NAME,
# 		authentication_form=AuthenticationForm,
# 		current_app=None, extra_context=None):
# 	error = ''
# 	context = {}
# 	redirect_to = request.GET.get(redirect_field_name, '')
# 	if request.user.is_authenticated():
# 		if not redirect_to:
# 			return redirect('dashboard')
# 		return HttpResponseRedirect(redirect_to)
# 	if request.method == "POST":
# 		try:
# 			username = request.POST.get('username', '')
# 			password = request.POST.get('password', '')
# 			username = username.split('@')[0] 
# 		except Exception as  e:
# 			error = 'username cant be empty'
		
# 			# Ensure the user-originating redirection url is safe.
# 		if not is_safe_url(url=redirect_to, host=request.get_host()):
# 			redirect_to = resolve_url(
# 				settings.LOGIN_REDIRECT_URL)


# 		# Okay, security check complete. Log the user in.    
		
# 		user = authenticate(
# 			username=username, password=password)
# 		if user is not None:
# 			if (user.profile.is_email_verified==False):
# 				return render_to_response(
# 					'registration/unverified_user.html', 
# 					context_instance=RequestContext(request))
# 			else:
# 				user = auth_login(request, user)

# 				return HttpResponseRedirect(redirect_to)
# 		else:
# 			error = 'username or password is incorrect'

# 	current_site  = get_current_site(request)
# 	form = authentication_form(request)
# 	context.update({
# 		'form': form,
# 		redirect_field_name: redirect_to,
# 		'site': current_site,
# 		'site_name': current_site.name,
# 		'login_attempt': False,
# 		'error': error
# 	})
# 	if extra_context is not None:
# 		context.update(extra_context)

# 	return TemplateResponse(
# 		request, template_name, context,
# 		current_app=current_app)

# @login_required
def login(requests,template_name='users/login.html'):




def register()