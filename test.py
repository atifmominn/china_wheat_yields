from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import csv

# Path to chromedriver.exe
PATH = "atifmomin/Downloads/chromedriver_mac64/chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

# setting up arrays
provinces = ["hebei", "henan", "shandong", "anhui", "jiangsu", "xinjiang", "shaanxi", "hubei", "gansu", "sichuan"]
years = [str(year) for year in range(2010, 2021)]
months = [
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december'
]


# Column names
columns = [
    'province',
    'year',
    'Jan - Temp',
    'Feb - Temp',
    'Mar - Temp',
    'Apr - Temp',
    'May - Temp',
    'Jun - Temp',
    'Jul - Temp',
    'Aug - Temp',
    'Sep - Temp',
    'Oct - Temp',
    'Nov - Temp',
    'Dec - Temp',
    'Jan - Precip',
    'Feb - Precip',
    'Mar - Precip',
    'Apr - Precip',
    'May - Precip',
    'Jun - Precip',
    'Jul - Precip',
    'Aug - Precip',
    'Sep - Precip',
    'Oct - Precip',
    'Nov - Precip',
    'Dec - Precip',
    'Jan - Wind',
    'Feb - Wind',
    'Mar - Wind',
    'Apr - Wind',
    'May - Wind',
    'Jun - Wind',
    'Jul - Wind',
    'Aug - Wind',
    'Sep - Wind',
    'Oct - Wind',
    'Nov - Wind',
    'Dec - Wind'
]

# Open the CSV file in write mode
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)

print('Columns have been written to the CSV file.')

# web scraping
# opens google sheet

for province in provinces:
    for year in years:
        temp = []
        water = []
        wind = []
        for month in months:
            #opens tcktcktck website
            driver.get("https://tcktcktck.org/" + province + "/" + month + "-" + year)

            # grabs table of province data
            elements = driver.find_elements(By.CLASS_NAME, "tb8")
            table = elements[0]

            # Find the <tbody> element within the table
            tbody = table.find_element(By.TAG_NAME, "tbody")

            # Find the third <tr> element within the <tbody> element
            tr = tbody.find_elements(By.TAG_NAME, "tr")[2]  # Index 2 represents the third <tr> element

            # Find the first <td> element within the <tr> element (average temp data)
            td = tr.find_elements(By.TAG_NAME, "td")[2]  # Index 2 represents the third <td> element

            # grabs text from <td> element
            average = td.text
            index = average.index("°C")
            average = average[:index]
            temp.append(average)
            print(average)

            tr = tbody.find_elements(By.TAG_NAME, "tr")[7]  # Index 2 represents the third <tr> element
            td = tr.find_elements(By.TAG_NAME, "td")[4]

            total = td.text
            index = total.index("m")
            total = total[:index]
            water.append(total)
            print(total)

            tr = tbody.find_elements(By.TAG_NAME, "tr")[10] 
            td = tr.find_elements(By.TAG_NAME, "td")[2]

            windy = td.text
            index = windy.index("k")
            windy = windy[:index]
            wind.append(windy)
            print(windy)

        data = []
        data.append(province)
        data.append(year)
        data.extend(temp)
        data.extend(water)
        data.extend(wind)

        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)




time.sleep(10)
