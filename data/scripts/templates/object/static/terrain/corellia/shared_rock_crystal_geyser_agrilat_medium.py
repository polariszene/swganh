#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/static/terrain/corellia/shared_rock_crystal_geyser_agrilat_medium.iff"
	is_prototype = False
	
	def create(self, params):
		result = Static()
	
		result.template = "object/static/terrain/corellia/shared_rock_crystal_geyser_agrilat_medium.iff"
		result.attribute_template_id = -1
		result.stfName("unknown_object","obj_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())