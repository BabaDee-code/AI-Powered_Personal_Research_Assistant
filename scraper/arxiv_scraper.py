import requests
from scrapy.selector import Selector
from database import store_papers

def fetch_recent_papers():
    url = "https://arxiv.org/list/cs.AI/recent"
    response = requests.get(url)
    selector = Selector(text=response.text)
    
    papers = []
    # arXiv uses a <dl> list; each paper's metadata is inside <dd>
    for dd in selector.css("dl > dd"):
        title_parts = dd.css("div.list-title.mathjax::text").getall()
        # Clean up title text (remove "Title:" and extra spaces)
        title = " ".join([t.strip() for t in title_parts if t.strip() and t.strip() != "Title:"])
        # The listing page typically doesn't include the abstract; using a placeholder.
        abstract = "Abstract not available on listing page."
        if title:
            papers.append({"title": title, "abstract": abstract})
    
    # Store these papers in the database with "arxiv" as the source.
    store_papers(papers, source="arxiv")
    
    return papers
