import time
import random
from selenium.common.exceptions import *
from assignment_hs import *

def individual_assignment(driver, asmt_list_url):
	name_input = asmt_name_new(driver, "_Ren_IP")
	due_date = select_due_date(driver)
	grade_types(driver, "Percentage")
	show_advanced(driver)
	instruction(driver)
	peer_review(driver)
	save_asmt(driver, name_input, asmt_list_url)
	return {'ip_name': name_input, 'due_date': due_date }		


	