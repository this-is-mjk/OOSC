# Requirements

```
pip install selenium webdriver-manager
pip install bs4
```

# Scrape function

The Scrap function navigates to a given URL using Chrome WebDriver, parses the webpage content, and extracts text and links

## Input

Takes the URL of the page to be scraped.

### Example Use:
```
from scrape_module import Scrap

# Example URL to scrape
url = "https://example.com"
scraped_data = Scrap(url)
print(scraped_data)

```

## Output

The function returns a dictionary containing:

1. relevant_link: A list of dictionaries with URLs and their respective page titles.
2. data: A string concatenating all extracted text and interactive elements' information from the webpage.

### Example Output:
```
{
    "relevant_link": [
        {
            "url": "https://example.com/page1",
            "title": "Page 1 Title"
        },
        {
            "url": "https://example.com/page2",
            "title": "Page 2 Title"
        }
    ],
    "data": "h1: Example Heading p: This is an example paragraph. links to: https://example.com/page1 ..."
}
```

