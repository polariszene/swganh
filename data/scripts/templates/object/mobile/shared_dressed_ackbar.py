#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/mobile/shared_dressed_ackbar.iff"
	is_prototype = False
	
	def create(self, params):
		result = Creature()
	
		result.template = "object/mobile/shared_dressed_ackbar.iff"
		result.attribute_template_id = 9
		result.stfName("admiral_ackbar","theme_park_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())