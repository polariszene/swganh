#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/ship/shared_ykl37r_tier4.iff"
	is_prototype = False
	
	def create(self, params):
		result = Ship()
	
		result.template = "object/ship/shared_ykl37r_tier4.iff"
		result.attribute_template_id = -1
		result.stfName("ykl37r","ship_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())