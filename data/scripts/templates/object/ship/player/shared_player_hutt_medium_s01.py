#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/ship/player/shared_player_hutt_medium_s01.iff"
	is_prototype = False
	
	def create(self, params):
		result = Ship()
	
		result.template = "object/ship/player/shared_player_hutt_medium_s01.iff"
		result.attribute_template_id = -1
		result.stfName("player_hutt_medium_s01","space_ship")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())