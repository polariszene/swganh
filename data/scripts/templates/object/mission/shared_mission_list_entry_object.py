#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/mission/shared_mission_list_entry_object.iff"
	is_prototype = False
	
	def create(self, params):
		result = Mission()
	
		result.template = "object/mission/shared_mission_list_entry_object.iff"
		result.attribute_template_id = -1
		result.stfName("","")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())