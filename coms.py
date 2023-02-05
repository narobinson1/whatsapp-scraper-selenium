from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
time.sleep(25) # time needed to link device
for i in range(1, 16):
	time.sleep(0.5)
	title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div[{i}]/div/div/div/div[2]/div[1]/div[1]/span".format(i=i))
	clickonthis = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div[{i}]".format(i=i))
	clickonthis.click()
	divs = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div")
	divs_count = len(divs)
	group_check = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div[{i}]/div/div/div/div[2]/div[2]/div[1]/span/span".format(i=i))
	span_count = len(group_check)
	if span_count == 0:
		continue
		# span count 0 - strange occurence
		# print("Groups will be implemented in future versions.")
	elif span_count == 1:
		# span count 1 - individual
		divs = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div")
		divs_count = len(divs)
		try:
			identity_check = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[{divcount}]/div/div/div[1]/span[@aria-label='{title}:']".format(title=title.text, divcount=divs_count))
			
			# situation checking
			norepl_repl_check = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[{last_div}]/div/div/div[1]/div[1]/div[1]/div".format(last_div=divs_count))
			if len(norepl_repl_check) == 1: # no reply, emoji/no-emoji
				try:
					norepl_nomoji_check = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[{last_div}]/div/div/div[1]/div[1]/div[1]/div/span[1]/span".format(last_div=divs_count))
					body = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[{last_div}]/div/div/div[1]/div[1]/div[1]/div/span[1]/span".format(last_div=divs_count))                                       
					print("Message from: {title}, \n Message: {body}".format(title=title.text, body=body.text))
				except:
					body = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[2]/div[{last_div}]/div/div/div[1]/div[1]/div[1]/div/div/span".format(last_div=divs_count))
					print("Message from: {title}, \n Message: {body}".format(title=title.text, body=body.text))
			
			else: # reply, emoji/no-emoji
				try:
					repl_nomoji_check = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[{last_div}]/div/div/div[1]/div[1]/div[1]/div[2]/span[1]/span".format(last_div=divs_count))
					body= driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[{last_div}]/div/div/div[1]/div[1]/div[1]/div[2]/span[1]/span".format(last_div=divs_count))
					print("Message from: {title}, \n Message: {body}".format(title=title.text, body=body.text))
				except:
					body = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[2]/div[{last_div}]/div/div/div[1]/div[1]/div[1]/div[2]/div/span".format(last_div=divs_count))
					print("Message from: {title}, \n Message: {body}".format(title=title.text, body=body.text))
		except:
			continue
	elif span_count == 3:
		# span count 3 - group
		#print("Groups will be implemented in future versions.")
		# this is a group, groups are skipped for the moment 
		continue

# individual, reply, emoji - /html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[2]/div[7]/div/div/div[1]/div[1]/div[1]/div[2]/div/span
# individual, norepl, emoji - /html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[2]/div[8]/div/div/div[1]/div[1]/div[1]/div/div/span
# individual, reply, nomoji - /html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/span[1]/span
# individual, norepl, nomoji - /html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[3]/div[23]/div/div/div[1]/div[1]/div[1]/div/span[1]/span

# add support for group chats in the future
# group, reply, emoji - 
# group, norepl, emoji -
# group, reply, nomoji -
# group, norepl, nomoji -

# count divs for each situation......... if count(divs) = x then follow THIS path. Otherwise, follow THAT path.
# Need to find the div at which it deviates
