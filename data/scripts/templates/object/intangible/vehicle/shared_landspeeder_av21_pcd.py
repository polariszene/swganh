#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Intangible()

	result.template = "object/intangible/vehicle/shared_landspeeder_av21_pcd.iff"
	result.attribute_template_id = -1
	result.stfName("monster_name","landspeeder_av21")		
	
	#### BEGIN MODIFICATIONS ####
	result.setStringAttribute("radial_filename", "radials.pcd_vehicle")
	result.setIntAttribute("is_mount", 1)
	####  END MODIFICATIONS  ####
	
	return result