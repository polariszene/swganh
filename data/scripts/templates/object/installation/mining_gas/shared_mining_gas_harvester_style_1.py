#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/installation/mining_gas/shared_mining_gas_harvester_style_1.iff"
	is_prototype = False
	
	def create(self, params):
		result = Installation()
	
		result.template = "object/installation/mining_gas/shared_mining_gas_harvester_style_1.iff"
		result.attribute_template_id = -1
		result.stfName("gas_mine_small","installation_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())