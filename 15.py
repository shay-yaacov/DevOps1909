from pandas import value_counts
from selenium import webdriver
from time import sleep

d = webdriver.Chrome()

def my_test (value_to_check,expected):
    d.get("file:///C:/Users/shayy/Downloads/tip_calc/tip_calc/index.html")
    d.find_element(by="id", value="billamt").send_keys("100")
    d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[3]').click()
    d.find_element(by="id", value="peopleamt").send_keys("5")
    d.find_element(by="id", value="musicquallity").send_keys("2")
    d.find_element(by="id", value="calculate").click()

    expected ="6.00"
    actual = d.find_element(by="id", value="tip").text
    is_visible =d.find_element(by="id", value="tip").is_displayed()
# if expected != actual:
#     print ("bad")
# else:
#      print ("good")
# print (is_visible)

    assert actual == expected
    assert is_visible

first_values=["100","5","2"]
my_test (first_values,"6")
sleep (10)
