# docs_crawler

A simple Python tool to crawl a single web page or all pages listed in a sitemap.xml, and convert their HTML content into Markdown files using the crawl4ai library.

## Features
- Accepts either a single URL or a sitemap.xml URL as a command-line argument
- Crawls the page(s) and saves the raw Markdown output to the `scraped_markdowns/` directory
- Automatically generates unique filenames for each crawled page

## Requirements
- Python 3.8+
- [crawl4ai](https://pypi.org/project/crawl4ai/)
- [aiohttp](https://pypi.org/project/aiohttp/)

Install dependencies:
```bash
pip install crawl4ai aiohttp
```

## Usage

Run the script from the command line:

### Crawl a single URL
```bash
python main.py https://example.com
```

### Crawl all URLs in a sitemap
```bash
python main.py https://example.com/sitemap.xml
```

Markdown files will be saved in the `scraped_markdowns/` directory, with filenames based on the domain and path of each URL.

## Output
- Each crawled page is saved as a Markdown file with the suffix `_raw.md`.
- Example: `example_com_root_raw.md` for `https://example.com/`.

## Notes
- Only the raw Markdown output is saved (no content filtering or fitting is applied).
- Make sure you have permission to crawl the target site and respect its robots.txt.

## License
MIT
