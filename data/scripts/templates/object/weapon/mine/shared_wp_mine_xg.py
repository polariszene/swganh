#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Weapon()

	result.template = "object/weapon/mine/shared_wp_mine_xg.iff"
	result.attribute_template_id = 10
	result.stfName("weapon_name","mine_xg")		
	
	#### BEGIN MODIFICATIONS ####
	####  END MODIFICATIONS  ####
	
	return result