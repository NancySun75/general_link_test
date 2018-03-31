# create a qestion and answer project
from selenium import webdriver
import time

# get current data to name assignment
lt = time.localtime() #time.struct_time(tm_year=2018, tm_mon=3, tm_mday=29, tm_hour=6, tm_min=0, tm_sec=24, tm_wday=3, tm_yday=88, tm_isdst=0)
s_date = time.strftime("%m%d",lt) # turn date to string
input_name = s_date + "_Ren_QA"

assignment_name = driver.find_element_by_id("activity-name-textfield")
assignment_name.send_keys("input_name")
