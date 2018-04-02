from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

'''
assignment_list_url = driver.current_url # url = "https://bigben-bongo.youseeu.com/spa/educator/class/39/activity-list"
assignment_title = driver.title # title is "Bongo"
'''
# new a project
# clcik + icon
def local_new_project(driver, project_type):
	add_new_item = driver.find_element_by_css_selector("[aria-label='Add New Item']")
	#add_new_item = driver.find_element_by_css_selector(".speed-dial-button button")
	add_new_item.click()

	project_type_icon = driver.find_element_by_css_selector(project_type) # "[aria-label='Create question & answer project']"
	project_type_show = ActionChains(driver).move_to_element(project_type_icon).perform()
	#print ("hoveriing show:", project_type_show) mouse hovering print method is incorrect.
	time.sleep(3) # for showing created project type
	project_type_icon.click()

'''
# local 3 project icon
question_answer = driver.find_element_by_css_selector("[aria-label='Create question & answer project']")
group = driver.find_element_by_css_selector("[aria-label='Create group project']")
individual = driver.find_element_by_css_selector("[aria-label='Create individual project']")

# hover to show
create question & answer project = ActionChains(driver).move_to_element(question_answer).perform()
Create group project = ActionChains(driver).move_to_element(group).perform()
Create individual project = ActionChains(driver).move_to_element(individual).perform()

# click icon to new project
question_answer.click()
group.click()
individual.click()
'''