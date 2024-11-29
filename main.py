
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(by=By.ID, value="cookie")

# Get upgrade item ids.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        # print(item_prices)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
        # print(cookie_upgrades)
        # Get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        # print(affordable_upgrades)

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

#         # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break




















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import datetime

# chrome_option=webdriver.ChromeOptions()
# chrome_option.add_experimental_option("detach",True)
# now=datetime.datetime.now()
# now_sec=now.second
# timeout = time.time() + 5
# five_min = time.time() + 60*5  # 5 minutes
# driver=webdriver.Chrome(options=chrome_option)
# driver.get("http://orteil.dashnet.org/experiments/cookie")
# cookie=driver.find_element(By.XPATH,value="//*[@id='cookie']")
# while True:
#     cookie.click()
    
#     clicked_Cookies=driver.find_element(By.XPATH,value="//*[@id='money']")
#     money=int(clicked_Cookies.text)

#     right_value=driver.find_elements(By.CSS_SELECTOR,value="#rightPanel div div b")
#     each_value=[i for i in right_value]
#     # clicking_values=[i for i in right_value]
#     # print(each_value)
#     cursor_value=each_value[0].text.split()[2]
#     grandma_value=each_value[1].text.split()[2]
#     # print(cursor_value,grandma_value)
#     product=[int(cursor_value),int(grandma_value)]
#     print(product)
#     if time.time() > timeout:
#         if money>=max(product):
#             index=product.index(max(product))
#             grandma=right_value[index]
#             grandma.click()
#         if money>=min(product):
#                 i2=product.index(min(product))
#                 cursor=right_value[i2]
#                 cursor.click()
#         timeout = time.time() + 5
    # if time.time()>five_min:
    #     total_cookies=driver.find_element(By.XPATH,value="//*[@id='cps']")
    #     print(total_cookies.text)


    




































# time.sleep(10)
# # lang=driver.find_element(By.ID,value="#langSelect-EN")
# lang=driver.find_element(By.XPATH,value="//*[@id='langSelect-EN']")
# print(lang.text)
# lang.click()
# # time.sleep(10)
# cookies=driver.find_element(By.XPATH,value="//*[@id='bigCookie']")
# # for i in range(100):
# tap=True
# while tap:
#     cookies.click()
#     no_of_coookies=driver.find_element(By.XPATH,value="//*[@id='cookies']")
#     # print()
#     if no_of_coookies.text.split()[0] =="101":
#         grandma=driver.find_element(By.XPATH,value="//*[@id='product1']")
#         grandma.click()
#     elif no_of_coookies.text.split()[0] == "15":
        
#         cursor=driver.find_element(By.XPATH,value="//*[@id='productIconOff0']")
#         # time.sleep(5)
#         # cursor=driver.find_element(By.CSS_SELECTOR,value="#product0 div")
#         cursor.click()
    
#     elif no_of_coookies.text.split()[0] == "125":
#         tap=False
