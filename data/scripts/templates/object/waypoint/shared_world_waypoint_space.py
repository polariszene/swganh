#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/waypoint/shared_world_waypoint_space.iff"
	is_prototype = False
	
	def create(self, params):
		result = Waypoint()
	
		result.template = "object/waypoint/shared_world_waypoint_space.iff"
		result.attribute_template_id = -1
		result.stfName("waypoint","obj_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())