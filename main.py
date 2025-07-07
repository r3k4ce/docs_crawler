import asyncio
import os
import sys
import aiohttp
from crawl4ai import AsyncWebCrawler
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai import CrawlerRunConfig
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

async def fetch_sitemap_urls(sitemap_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(sitemap_url) as resp:
            text = await resp.text()
    root = ET.fromstring(text)
    urls = []
    for url in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        urls.append(url.text)
    return urls

async def crawl_and_save(url):
    md_generator = DefaultMarkdownGenerator()
    config = CrawlerRunConfig(markdown_generator=md_generator)
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url, config=config)
        os.makedirs("scraped_markdowns", exist_ok=True)
        parsed = urlparse(url)
        # Make filename unique per URL
        path_part = parsed.path.replace('/', '_').strip('_')
        if not path_part:
            path_part = 'root'
        filename = f"{parsed.netloc.replace('.', '_')}_{path_part}_raw.md"
        filepath = os.path.join("scraped_markdowns", filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(result.markdown.raw_markdown)
        print(f"Raw markdown saved to {filepath}")

async def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <URL or sitemap.xml>")
        sys.exit(1)
    arg = sys.argv[1]
    if arg.endswith("sitemap.xml"):
        urls = await fetch_sitemap_urls(arg)
        print(f"Found {len(urls)} URLs in sitemap.")
        for url in urls:
            await crawl_and_save(url)
    else:
        await crawl_and_save(arg)

if __name__ == "__main__":
    asyncio.run(main())
