### Requirements

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

## Example Output:
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

# Semantic Chunking and Question Generation with Llama 3.1 8B Instruct
This project leverages various NLP techniques, including semantic chunking, question generation, and clustering, to process textual data and generate relevant questions. The goal is to produce meaningful questions that focus on the most important parts of the content provided.

## Overview
This project automates the process of extracting data from a JSON file, applying semantic chunking, and generating questions that focus on key themes, details, and implications of the content. The generated questions are then clustered using K-means and linked to relevant online resources.

## Dependencies
To run this project, you need the following Python libraries:

* semantic-split
* nltk
* beautifulsoup4
* unsloth
* transformers
* torch
* sklearn
* sentence-transformers
* numpy
* requests

!pip install semantic-split nltk beautifulsoup4 unsloth sentence-transformers transformers torch sklearn numpy requests

## Data Source
1. The main content is loaded from a JSON file located at: https://raw.githubusercontent.com/this-is-mjk/OOSC/main/dataSet/data.json.
2. An additional webpage is scraped from: https://medium.com/@bijit211987/chunking-strategies-for-fine-tuning-llms-30d2988c3b7a.

## Workflow
1. Data Loading: The content is loaded from a JSON file and a webpage is scraped for additional data.
2. Semantic Chunking: The text data is split into smaller, meaningful chunks using sentence similarity techniques.
3. Question Generation: Questions are generated based on the chunked text, focusing on various aspects such as general understanding, specific details, and critical thinking.
4. Clustering: The questions are grouped into clusters to identify the most representative questions.
5. Link Identification: The most relevant online resources are identified based on the generated questions.
5. Validation: The relevance of the questions is validated by comparing them with the original text using cosine similarity.

# Output
* Questions: A list of generated questions focusing on different aspects of the content.
* Relevant Links: Top 5 matching links from the provided resources based on the generated questions.
* Cosine Similarity Score: A score indicating how closely the generated questions match the original content.

# Acknowledgements
* Llama 3.1 8B Instruct: For question generation.
* Semantic-Split: For text chunking.
* K-means Clustering: For grouping similar questions.
* Sentence Transformers: For link identification based on sentence embeddings.
