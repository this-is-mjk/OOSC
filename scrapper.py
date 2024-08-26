# pip install selenium webdriver-manager
# pip install bs4

import json
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from bs4 import BeautifulSoup
from collections import defaultdict

# URL
url = 'https://www.w3schools.com/tags/ref_byfunc.asp'

def Scrap(url):
    # set up Chrome WebDriver using ChromeDriverManager 
    driver = webdriver.Chrome(service=ChromeService( 
        ChromeDriverManager().install())) 

    # open the specified URL in the browser 
    driver.get(url) 

    # extract info into soup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # links
    links = set() 

    # human_useful_tags = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a', 'div', 'span', 'li', 'ol', 'ul', 'head', 'body', 'footer', 'title', }
    not_to_use = {'script', 'noscript', 'applet', 'embed', 'object', 'param', 'link', 'style'}
    data = ""
    links = set() 

    for tag in soup.find_all(True):  # True finds all tags
        tag_name = tag.name
        # Skip tags that are not useful
        if tag_name in  not_to_use:
            continue

        # Extract text
        text = tag.get_text(strip=True)
        if text:  # Only add if there's text
            data += f"{tag_name}: {text} "

        # Collect links
        if tag_name == 'a' and tag.get('href'):
            href = tag["href"]
            if href.startswith('http') and not any(ext in href for ext in ['.jpg', '.png', '.gif', 'advertisement', 'ads']):
                links.add(href)
                data += "links to:" + href + " "
        # Extract attributes from interactive elements
        if tag_name in {'input', 'button', 'select', 'textarea'}:
            attributes = []
            if tag_name == 'input':
                attributes.append(f"placeholder: {tag.get('placeholder', '')}")
                attributes.append(f"value: {tag.get('value', '')}")
                attributes.append(f"type: {tag.get('type', '')}")
            elif tag_name == 'button':
                attributes.append(f"type: {tag.get('type', '')}")
                attributes.append(f"value: {tag.get('value', '')}")
            elif tag_name == 'select':
                attributes.append(f"options: {', '.join([option.get_text(strip=True) for option in tag.find_all('option')])}")
            elif tag_name == 'textarea':
                attributes.append(f"placeholder: {tag.get('placeholder', '')}")
                attributes.append(f"value: {tag.get('value', '')}")

            if attributes:
                data += f"{tag_name} attributes: {', '.join(attributes)} "

    # get the titile for the links
    relevant_links = []
    for url in links:
        try:
            # Send an HTTP request to fetch the webpage content
            response = driver.get(url) 
            # Parse the content using BeautifulSoup
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            title = soup.title.string if soup.title else 'No Title Found'

            # Append the URL and title to the result list
            relevant_links.append({
                "url": url,
                "title": title
            })
        except Exception as e:
            print(f"Failed to fetch {url}: {str(e)}")

    # close the browser
    driver.quit()

    result = {
        'relevant_link': relevant_links,
        'data': data 
    }
    # write the scrapped data
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    return result


## word_count 
# word_count = len(str(data).split())
#  print("Word count:", word_count)