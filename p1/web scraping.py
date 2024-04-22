import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


def main():
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver-win64\chromedriver.exe')
    driver.get("https://www.forbes.com/billionaires/")
    time.sleep(20)

    ranks = []
    names = []
    net_worths = []
    ages = []
    countries = []
    sources = []
    industries = []

    for k in range(14):
        elements = driver.find_elements(By.CLASS_NAME, "Table_tableRow__lF_cY") 
        for element in elements:
            details = element.text.split('\n')
            ranks.append(details[0])
            names.append(details[1])
            net_worths.append(details[2])
            ages.append(details[3])
            countries.append(details[4])
            sources.append(details[5])
            industries.append(details[6])

        button = driver.find_element(By.CSS_SELECTOR, ".arrow-right_svg__fs-icon.arrow-right_svg__fs-icon--arrow-right")
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        driver.execute_script("var evt = document.createEvent('MouseEvent'); evt.initMouseEvent('click',true,true,window,0,0,0,0,0,false,false,false,false,0,null); arguments[0].dispatchEvent(evt);", button)

    driver.close()

    # Create a DataFrame from the collected data
    df = pd.DataFrame({
        "Rank": ranks,
        "Name": names,
        "Net Worth": net_worths,
        "Age": ages,
        "Country": countries,
        "Source": sources,
        "Industry": industries
    })

    # Print the DataFrame
    print(df)
    df.to_csv("billionaires_data.csv", index=True)

if __name__ == "__main__":
    main()
