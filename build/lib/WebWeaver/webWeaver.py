import requests
from collections import deque 
from .util import get_url_domain
from .util import UrlList
import re
import threading

import time



#Class structure for web weaver logic
class WebWeaver:

    ##Method to crawl single page and extract all the links in that page
    def crawl_url(self, url, timeout=2):
        try:
            reqs = requests.get(url,timeout=timeout)
        except:
            return [None]
        url_pattern = r'\shref=\"\s*(?!.*favicon)(?!#)([^\'\"<>\s]+)\s*\"'
        matching_tags = re.findall(url_pattern, reqs.text)
        return matching_tags

    #Method to crawl single page and extract all the links in that page with session
    def crawl_url_sitemap(self, url, timeout, session, url_list):
        try:
            reqs = session.get(url,timeout=timeout)
        except:
            return [None]
        url_list.urls.add(url)
        url_pattern = r'\shref=\"\s*(?!.*favicon)(?!#)([^\'\"<>\s]+)\s*\"'
        matching_tags = re.findall(url_pattern, reqs.text)
        return matching_tags


    #Method to get site map
    def crawl_site(self, urls, timeout = 2, limit = 5):
        q = deque()
        url_list = UrlList()
        session = requests.Session()
        for url in urls:
            q.append(url)
        count_urls_crawlled = 0
        while(q and count_urls_crawlled<=limit):
            url = q.popleft()
            count_urls_crawlled+=1
            extracted_urls = self.crawl_url_sitemap(url, timeout, session,url_list)
            domain_name = get_url_domain(url)
            if len(extracted_urls)!=0 and extracted_urls[0]==None:
                url_list.error_urls.add(url)
                continue
            for extracted_url_i in extracted_urls:
                extracted_url = extracted_url_i
                if extracted_url==None:
                    continue
                extracted_url = extracted_url.strip()
                if(extracted_url[:4]!="http"):
                    url_list.abnormal_urls.add(extracted_url)
                    if extracted_url[0]!='/':
                        extracted_url = '/' + extracted_url
                    extracted_url = domain_name + extracted_url
                extracted_url.rstrip('/')
                if((extracted_url not in url_list.urls) and (extracted_url not in url_list.error_urls)):
                    q.append(extracted_url)
                    url_list.urls.add(extracted_url)
        session.close()
        return url_list
    

    #Method to crawl single page and extract all the links in that page with session along with multiThreading
    def crawl_url_sitemap_multiThreading(self, url, timeout, session, url_list,q):
        try:
            reqs = session.get(url,timeout=timeout)
        except:
            url_list.error_urls.add(url)
            return 
        url_list.urls.add(url)
        url_pattern = r'\shref=\"\s*(?!.*favicon)(?!#)([^\'\"<>\s]+)\s*\"'
        #url_pattern = r'\shref=\"\s*(?!#)(?!.*(favicon|\.pdf|\.jpg|\.png|\.gif|\.css|\.js|\.ico|\.svg|utm_|sort=|page=|order=|logout|wp-admin|admin|profile|delete-account))([^\'\"<>\s]+)\s*\"'
        extracted_urls = re.findall(url_pattern, reqs.text)
        
        domain_name = get_url_domain(url)
        for extracted_url_i in extracted_urls:
            extracted_url = extracted_url_i
            if extracted_url==None:
                continue
            extracted_url = extracted_url.strip()
            if(extracted_url[:4]!="http"):
                url_list.abnormal_urls.add(extracted_url)
                if extracted_url[0]!='/':
                    extracted_url = '/' + extracted_url
                extracted_url = domain_name + extracted_url
            extracted_url.rstrip('/')
            if((extracted_url not in url_list.urls) and (extracted_url not in url_list.error_urls)):
                q.append(extracted_url)
                url_list.urls.add(extracted_url)


    #Method to get site map with multiThreading
    def crawl_site_multiThreading(self, urls, timeout = 2, limit = 5, no_of_threads = 16):
        q = deque()
        url_list = UrlList()
        session = requests.Session()
        for url in urls:
            q.append(url)
        count_urls_crawlled = 0
        while(q and count_urls_crawlled<=limit):
            threads = []
            for _ in range(no_of_threads):
                if not q or count_urls_crawlled>limit:
                    break
                url = q.popleft()
                count_urls_crawlled+=1
                thread = threading.Thread(target=self.crawl_url_sitemap_multiThreading, args=(url, timeout, session,url_list,q))
                threads.append(thread)
                thread.start()  # Start the thread
            
            # Join threads to ensure all threads complete before starting new ones
            for thread in threads:
                thread.join()
            #extracted_urls = self.crawl_url_sitemap(url, timeout, session,url_list)
            
        session.close()
        return url_list



