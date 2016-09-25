from django.shortcuts import render, HttpResponseRedirect, Http404
from .forms import EmailForm, JoinForm
from .models import Join

# Create your views here.

def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")

	except:
		ip = ""

	return ip



import uuid

def get_ref_id():

	ref_id = str(uuid.uuid4())[:11].replace('-','').lower()
	try:
		id_exist = Join.objects.get(ref_id=ref_id)

		if id_exist:
			get_ref_id()

	except:
		return ref_id



def share(request, ref_id):
	#print  (ref_id)

	try:
		join_obj = Join.objets.get(ref_id=ref_id)
		friends_referred = Join.objects.filter(friend=join_obj)
		#count = obj.count()
		count = join_obj.referral.all().count()
		print (count)

		ref_url ="http://google.fi/?ref=%s" %(join_obj.ref_id)
		context = {"ref_id": ref_id}
		#context = {"ref_id": join_obj.ref_id, "count": count, "ref_url": ref_url}
		template = "share.html"
		return render(request, template, context)

	except:
		raise Http404


def home(request):

	try:
		join_id = request.session['join_id_ref']
		obj = Join.objects.get(id=join_id)
		print ("the obj id is %s" %obj.email)
		print ("the obj id is %s" %obj)

	except:
		obj = None	


	form = JoinForm(request.POST or None)
	form.fields["ip_adress"].initial = get_ip(request)

	if form.is_valid():

		new_join = form.save(commit = False)
		#new_join.ref_id = get_ref_id()
		#new_join.ip_adress = get_ip(request)

		email = form.cleaned_data['email']
		ip_adress = form.cleaned_data['ip_adress']
		new_join_old, created = Join.objects.get_or_create(email=email, ip_adress=ip_adress)
		
		if created:
				new_join_old.ref_id = get_ref_id()
				#add our frienbd who reffered us to our join model or related
				if not obj == None:
					new_join_old.friend = obj


				new_join_old.ip_adress = get_ip(request)
				new_join_old.save()

		print (Join.objects.filter(friend=obj).count())
		#print (obj.referral.all().count())

		#redirect here
		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
		
		
		#new_join_old = Join.objects.get_or_create(email=email, ip_adress=ip_adress)
		

		#new_join.save()

	context = {"CustomForm1": form}
	template = "home.html"
	return render(request, template, context)