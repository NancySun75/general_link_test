import time
import random
from selenium.common.exceptions import *
from assignment_hs import *

def group_assignment(driver, asmt_list_url):
	name_input = asmt_name_new(driver, "_Ren_GP")
	select_due_date(driver)
	grade_types(driver, "Five Star")
	show_advanced(driver)
	instruction(driver)
	group_formeds(driver, "System Formed")
	peer_review(driver)
	save_asmt(driver, name_input, asmt_list_url)
	return name_input	
	