#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Tangible()

	result.template = "object/tangible/wearables/pants/shared_pants_s28.iff"
	result.attribute_template_id = 11
	result.stfName("wearables_name","pants_s28")		
	
	#### BEGIN MODIFICATIONS ####
		result.max_condition = 1000
	####  END MODIFICATIONS  ####
	
	return result