from setuptools import setup, find_packages

setup(
    name="docs_crawler",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'docs-crawler=docs_crawler.main:main',
        ]
    },
    install_requires=[
        'aiohttp',
        'crawl4ai',
    ],
)
