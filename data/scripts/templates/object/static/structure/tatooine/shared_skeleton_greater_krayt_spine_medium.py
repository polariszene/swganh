#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/static/structure/tatooine/shared_skeleton_greater_krayt_spine_medium.iff"
	is_prototype = False
	
	def create(self, params):
		result = Static()
	
		result.template = "object/static/structure/tatooine/shared_skeleton_greater_krayt_spine_medium.iff"
		result.attribute_template_id = -1
		result.stfName("unknown_object","obj_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())