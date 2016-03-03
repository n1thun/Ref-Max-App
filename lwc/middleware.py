from joins.models import Join


class ReferMiddleware():
	def process_request(self, request):
		print request.GET
		ref_id = request.GET.get("ref") # get reffering persons id
		request.session['join_id_ref'] = ref_id #assign to session variable


		# could not pass objects via session variables, original code from tutorial
		# try:
		# 	obj = Join.objects.get(ref_id = ref_id) # Assign reffering person to obj
		# except:
		# 	obj= None

		# if obj:		#If obj exists do following
		# 	request.session['join_id_ref'] = obj # Assign session variable to obj.id
