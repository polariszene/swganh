#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/intangible/ship/shared_bwing_pcd.iff"
	is_prototype = False
	
	def create(self, params):
		result = Intangible()
	
		result.template = "object/intangible/ship/shared_bwing_pcd.iff"
		result.attribute_template_id = 8
		result.stfName("bwing_pcd","space_item_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())