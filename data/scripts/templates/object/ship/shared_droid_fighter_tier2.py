#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/ship/shared_droid_fighter_tier2.iff"
	is_prototype = False
	
	def create(self, params):
		result = Ship()
	
		result.template = "object/ship/shared_droid_fighter_tier2.iff"
		result.attribute_template_id = -1
		result.stfName("","")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())