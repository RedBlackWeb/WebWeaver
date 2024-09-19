

#calss structure of return object of Crawl_site method
class UrlList:
    def __init__(self) -> None:
        self.urls = set()
        self.abnormal_urls = set()
        self.error_urls = set()


##Method to get domain and subdomain of a URL
def get_url_domain(url):
    domain_name = ""
    backslash_cnt = 0
    for ch in url:
        domain_name = domain_name + ch
        if(ch=="/"):
            backslash_cnt+=1
            if backslash_cnt==3:
                return domain_name[:-1]
    if domain_name[-1]=='/':
        domain_name = domain_name[:-1]
    return domain_name