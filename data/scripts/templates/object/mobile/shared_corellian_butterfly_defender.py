#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/mobile/shared_corellian_butterfly_defender.iff"
	is_prototype = False
	
	def create(self, params):
		result = Creature()
	
		result.template = "object/mobile/shared_corellian_butterfly_defender.iff"
		result.attribute_template_id = 9
		result.stfName("corellian_butterfly","monster_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())