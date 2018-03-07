#!/usr/bin/python3

"""
Web recortadora de urls

 p.ariaspe @ alumnos.urjc.es
 SAT (Universidad Rey Juan Carlos)
"""

import webapp
import os.path

urls = {}
nums = {}

FORM = """
    <form action="" method="POST">
        <label for="url">URL a acrotar:</label><br>
        <input type="text" name="url" value="gsyc.es"/><br>
        <input type="submit" value="Send url">
    </form>
"""


class WebShort(webapp.webApp):
    def parse(self, request):
        method = request.split()[0]
        if(method == 'POST'):
            url = request.split('=')[-1]
        else:
            url = None
        resource = request.split()[1].split('/')[1]  # Recurso sin barra
        return (method, resource, url)

    def url_style(self, url):
        print(url.encode().decode('ascii'))
        if url.startswith('http') or url.startswith('https'):
            return url.replace('%3A%2F%2F', '://')
        else:
            return 'http://' + url

    def print_urls(self, urls):
        url_string = ''
        for k, v in urls.items():
            url_string += str(k) + ': ' + str(v) + '<br>'

        return url_string

    def process(self, parsedRequest):
        print(parsedRequest)
        if(parsedRequest[0] == 'GET'):
            if(parsedRequest[1] == ''):
                code = '200 OK'
                html_answer = '<html><body><h1>Acortador de URLs</h1> ' + FORM
                html_answer += '<p>' + self.print_urls(nums)
                html_answer += '</p></body></html>'
            elif(parsedRequest[1] in nums):
                code = '302 Found\r\nLocation: ' + nums[parsedRequest[1]]
                html_answer = ''
            else:
                code = '404 Not Found'
                html_answer = '<html><body><h1>Not Found.</h1></body></html>'
        elif(parsedRequest[0] == 'POST'):
            url = self.url_style(parsedRequest[2])
            if url in urls:
                print('ya dentro')
            else:
                nums[str(len(nums))] = url
                urls[url] = str(len(urls))
                with open('file.txt', 'w') as file:
                    for k, v in urls.items():
                        file.write(str(k) + ' ' + str(v) + '\n')

            code = '200 OK'
            html_answer = '<html><body><h1>Acortador de URLs</h1> ' + FORM
            html_answer += '<p>' + self.print_urls(nums) + '</p></body></html>'
        else:
            code = '404 Not Found'
            html_answer = '<html><body><h1>Not Found.</h1></body></html>'

        return (code, html_answer)

if __name__ == '__main__':
    if(os.path.isfile('file.txt')):
        with open('file.txt') as f:
            for line in f:
                key, val = line.split()
                urls[key] = val
                nums[val] = key
    
    testWebApp = WebShort('localhost', 1234)
