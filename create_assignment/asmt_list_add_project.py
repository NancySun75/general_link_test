from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


# url = "https://bigben-bongo.youseeu.com/spa/educator/class/39/activity-list"

# new a project
# clcik + icon
def local_new_project(driver, project_type):
	add_new_item = driver.find_element_by_css_selector("[aria-label='Add New Item']")
	#add_new_item = driver.find_element_by_css_selector(".speed-dial-button button")
	add_new_item.click()

	# local 3 project icon
	project_dics = {
		"question_answer":"[aria-label='Create question & answer assignment']",
		"group":"[aria-label='Create group assignment']",
		"individual":"[aria-label='Create individual assignment']"
	}
	
	project_type_icon = driver.find_element_by_css_selector(project_dics[project_type]) 
	project_type_show = ActionChains(driver).move_to_element(project_type_icon).perform()
	#print ("hoveriing show:", project_type_show) mouse hovering print method is incorrect.
	time.sleep(3) # for showing created project type
	project_type_icon.click()

