from bigben_driver import chrome_init
from bigben_login import login_bigben
from home_page import home_link
from delete_assignment import delete_asmt

driver = chrome_init()
login_bigben(driver)
asmt_list_url = home_link(driver, "bigbengenerallink", "bigbengenerallink: videoassignments")
delete_asmt(driver, asmt_list_url, "_Ren_", False)