#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/mobile/shared_death_watch_battle_droid_03.iff"
	is_prototype = False
	
	def create(self, params):
		result = Creature()
	
		result.template = "object/mobile/shared_death_watch_battle_droid_03.iff"
		result.attribute_template_id = 9
		result.stfName("battle_droid","droid_name")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())