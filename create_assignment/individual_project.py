import time
import random
from selenium.common.exceptions import *
from assignment_hs import *

def individual_assignment(driver, asmt_list_url):
	name_input = asmt_name_new(driver, "_Ren_IP")
	select_due_date(driver)
	grade_types(driver, "Percentage")
	show_advanced(driver)
	instruction(driver)
	peer_review(driver)
	save_asmt(driver, name_input, asmt_list_url)
	return name_input	


	