from requests import Request, Session


class URL(object):
    def __init__(self,url,response,status):
        self.url = url
        self.response = response
        self.status = status


class REQ(object):
    def __init__(self,req,url):
        self.req = req
        self.url = url


class Spy(object):
    """
    use for spider to web (html,xml)
    """
    sess = Session()
    timeout = 10
    headers = None
    proxies = None
    stream = None
    verify = None
    cert = None

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self):
        pass

    def __len__(self):
        return len(self.reqs)

    def __getitem__(self, item):
        return self.reqs[item].url

    def __repr__(self):
        return "Spy object"

    def composer(self, urls, method='GET', headers=None, data=None, **kwargs):
        self.headers = headers if headers else None
        self.method = method
        kwargs.setdefault('stream', self.stream)
        kwargs.setdefault('verify', self.verify)
        kwargs.setdefault('cert', self.cert)
        kwargs.setdefault('proxies', self.proxies)
        self.reqs = [REQ(self.__structure(u, data),(URL(u, None, None))) for u in urls]

    def __structure(self, url, data):
        req = Request(self.method, url, data=data, headers=self.headers)
        return self.sess.prepare_request(req)

    def start(self, req, **kwargs):
        if kwargs.get('verify'):
            self.verify = True
        resp = self.sess.send(req.req,
                              stream=self.stream,
                              verify=self.verify,
                              proxies=self.proxies,
                              cert=self.cert,
                              timeout=self.timeout
                              )
        req.url.status = resp.status_code
        if kwargs.get('content') :
            req.url.response = resp.content
            return req
        req.url.response = resp.text
        return req

    def run(self, **kwargs):
        for r in self.reqs:
            yield self.start(r, **kwargs).url

if __name__ == '__main__':
    a = Spy()
    a.composer(["https://www.baidu.com", "https://www.baidu.com"], method='GET', headers=None)
    for i in a.run(verify=True):
        print(i.url)
        print(i.response)
        print(i.status)

