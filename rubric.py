from selenium import webdriver
import time

def new_rubric(driver):
	add_icon = driver.find_element_by_css_selector('[aria-label="Add New Item"]')
	add_icon.click()
	time.sleep(1)
	create_rubric = driver.find_element_by_css_selector('[aria-label="Create rubric"]')
	create_rubric.click()

def import_rubric():
	add_icon = driver.find_element_by_css_selector('[aria-label="Add New Item"]')
	add_icon.click()
	time.sleep(1)
	import_rubric = driver.find_element_by_css_selector('[aria-label="Import rubric"]')
	import_rubric.click()
	time.sleep(1)
	#download template
	download_examplerubric = driver.find_element_by_css_selector('[download="examplerubric.csv"]')
	download_examplerubric.click()