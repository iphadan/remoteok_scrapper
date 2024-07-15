import requests 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
url = "http://10.1.249.44:9990/console/index.html#runtime;path=domain-browse-by~hosts!host~host-prodapp03!server~prodapp03-michutwo-server!rss~server-runtime-status"
username="zerihun"
password="zerihun"
response = requests.get(url,auth=(username,password))
soup= BeautifulSoup(response.content,'html.parser')
element = soup.find(id="server-runtime-status-heap-used")

print("=====> bs4  ",response.content)


chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

# Initialize Chrome driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the login page
    driver.get(url)

    # Find the username and password input fields and submit button
    username_field = driver.find_element_by_id('username')
    password_field = driver.find_element_by_id('password')
    submit_button = driver.find_element_by_id('login-button')

    # Enter username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the form
    submit_button.click()

    # Wait for the page to load (you may need to add more sophisticated waiting logic)
    driver.implicitly_wait(10)  # wait for up to 10 seconds

    # Now you can interact with the page, execute JavaScript, and scrape dynamic content
    # For example:
    print("=====> selenium started")
    element = driver.find_element_by_id("server-runtime-status-heap-used")
    print("=====> selenium", element.text)

finally:
    # Don't forget to close the driver when done
    driver.quit()