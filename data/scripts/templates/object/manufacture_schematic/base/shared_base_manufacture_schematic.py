#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/manufacture_schematic/base/shared_base_manufacture_schematic.iff"
	is_prototype = False
	
	def create(self, params):
		result = ManufactureSchematic()
	
		result.template = "object/manufacture_schematic/base/shared_base_manufacture_schematic.iff"
		result.attribute_template_id = -1
		result.stfName("unknown_schematic","obj_n")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())