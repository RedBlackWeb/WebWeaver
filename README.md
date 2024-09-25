
# WebWeaver

WebWeaver is a Python package for crawling and extracting URLs from web pages. It provides an easy-to-use interface for crawling a single page or an entire site, while handling errors and incomplete URLs gracefully. All crawling functionality is encapsulated within the `WebWeaver` class.

## Features
- **`crawl_url(url)`**: Given a URL, this method returns a list of all URLs found on the page.
- **`crawl_site(urls, limit, timeout)`**: Crawls multiple URLs with the ability to limit the number of pages and set a timeout for each page to load. It returns an object of the `UrlList` class containing information about successfully crawled URLs, incomplete URLs, and error-causing URLs.
- **`crawl_site_multiThreading(urls, limit, timeout, no_of_threads)`**: Crawls multiple URLs using multithreading for faster performance, allowing you to control the number of threads. It returns an object of the `UrlList` class.

## Installation

Install the package using `pip`:

```bash
pip install WebWeaver
```

## Usage

### `WebWeaver` Class

The `WebWeaver` class provides methods for URL extraction and site crawling.

#### `crawl_url(url)`
Extracts all URLs found on a given web page.

**Parameters**:
- `url (str)`: The URL of the page you want to crawl.

**Returns**:
- `list`: A list of URLs found on the page.

**Example**:
```python
from WebWeaver import WebWeaver

# Instantiate the WebWeaver class
weaver = WebWeaver()

# Crawl a single URL
urls = weaver.crawl_url("https://example.com")
print(urls)
```

#### `crawl_site(urls, limit, timeout)`
Crawls multiple web pages and returns an `UrlList` object that categorizes URLs into three sets: successfully crawled URLs, incomplete URLs, and URLs that caused errors.

**Parameters**:
- `urls (list)`: A list of URLs to start crawling.
- `limit (int)`: The maximum number of pages to crawl.
- `timeout (int)`: The time limit (in seconds) for each page to load.

**Returns**:
- `UrlList`: An object containing three sets:
  - `urls`: A set of all successfully crawled and retrieved URLs.
  - `abnormal_urls`: A set of incomplete or malformed URLs extracted from the web pages.
  - `error_urls`: A set of URLs that caused errors when trying to make a request.

**Example**:
```python
from WebWeaver import WebWeaver

# Instantiate the WebWeaver class
weaver = WebWeaver()

# Crawl multiple URLs
urls_to_crawl = ["https://example.com", "https://anotherexample.com"]
result = weaver.crawl_site(urls_to_crawl, limit=10, timeout=5)

# Accessing the sets from the result
print("Crawled URLs:", result.urls)
print("Abnormal URLs:", result.abnormal_urls)
print("Error URLs:", result.error_urls)
```

#### `crawl_site_multiThreading(urls, limit, timeout, no_of_threads)`
Crawls multiple web pages using multithreading, allowing for faster crawling by specifying the number of threads. Returns an `UrlList` object categorizing URLs into successfully crawled, incomplete, and error-causing URLs.

**Parameters**:
- `urls (list)`: A list of URLs to start crawling.
- `limit (int)`: The maximum number of pages to crawl.
- `timeout (int)`: The time limit (in seconds) for each page to load.
- `no_of_threads (int)`: The number of threads to use for crawling.

**Returns**:
- `UrlList`: An object containing three sets:
  - `urls`: A set of all successfully crawled and retrieved URLs.
  - `abnormal_urls`: A set of incomplete or malformed URLs extracted from the web pages.
  - `error_urls`: A set of URLs that caused errors when trying to make a request.

**Example**:
```python
from WebWeaver import WebWeaver

# Instantiate the WebWeaver class
weaver = WebWeaver()

# Crawl multiple URLs using multithreading
urls_to_crawl = ["https://example.com", "https://anotherexample.com"]
result = weaver.crawl_site_multiThreading(urls_to_crawl, limit=10, timeout=5, no_of_threads=16)

# Accessing the sets from the result
print("Crawled URLs:", result.urls)
print("Abnormal URLs:", result.abnormal_urls)
print("Error URLs:", result.error_urls)
```

### `UrlList` Class
The `crawl_site` and `crawl_site_multiThreading` methods return an object of the `UrlList` class, which contains the following sets:

- `urls (set)`: A set of all successfully crawled URLs.
- `abnormal_urls (set)`: A set of incomplete or malformed URLs found during the crawl.
- `error_urls (set)`: A set of URLs that caused errors when attempting to access them.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

---

Happy crawling!
