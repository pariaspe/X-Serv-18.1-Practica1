#!/usr/bin/python3

"""
Web recortadora de urls

 p.ariaspe @ alumnos.urjc.es
 SAT (Universidad Rey Juan Carlos)
"""

import webapp

urls = {} # Hacer atributo?
nums = {}

FORM = """
    <form action="" method="POST">
        <label for="url">URL a acrotar:</label><br>
        <input type="text" name="url" value="gsyc.es"/><br>
        <input type="submit" value="Send url">
    </form>
"""

class webShort(webapp.webApp):
    def parse(self, request):
        method = request.split()[0]
        if(method == "POST"):
            url = request.split("=")[-1]
        else:
            url = None
        resource = request.split()[1].split('/')[1] # Recurso sin barra
        return (method, resource, url)

    def url_style(self, url): # Funciona mal
        print(url)
        if url.startswith('http://') or url.startswith('https://'):
            return url
        else:
            return 'http://' + url

    def print_urls(self, urls):
        url_string = ""
        for i in urls:
            if i <= len(urls):
                url_string += str(i) + ': ' + urls[i]

    def process(self, parsedRequest):
        print(parsedRequest)
        if(parsedRequest[0] == "GET"):
            if(parsedRequest[1] == ''):
                code = "200 OK"
                html_answer = '<html><body><h1>Acortador de URLs</h1> ' + FORM
                html_answer += '<p>' + self.print_urls(nums) + '</p></body></html>'
            elif(int(parsedRequest[1]) in nums):
                code = "302 Found\r\nLocation: " + nums[int(parsedRequest[1])]
                html_answer = ''
            else:
                code = "404 Not Found"
                html_answer = 'Error'
        elif(parsedRequest[0] == "POST"):
            url = self.url_style(parsedRequest[2])
            if url in urls:
                print("ya dentro")
            else:
                nums[len(nums)] = url
                urls[url] = len(urls)

            code = "200 OK"
            html_answer = '<html><body><h1>Acortador de URLs</h1> ' + FORM
            html_answer += '<p>' + self.print_urls(nums) + '</p></body></html>'
        else:
            code = "404 Not Found"
            html_answer = "Error"


        return (code, html_answer)

if __name__ == "__main__":
    testWebApp = webShort("localhost", 1234)
