from selenium import webdriver
import tldextract


class Test:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    print(driver.title)

# tld = tldextract.extract('http://www.baidu.com')
# print(tld.domain)
# print(tld.subdomain)
# print(tld.suffix)

# str = [i ** 2 for i in range(2, 101, 2)]
# print(str)
