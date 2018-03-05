#!/usr/bin/python3

"""
Web recortadora de urls

 p.ariaspe @ alumnos.urjc.es
 SAT (Universidad Rey Juan Carlos)
"""

import webapp

urls = {}
nums = {}
cont = 0

class webShort(webapp.webApp):
    def parse(self, request):
        method = request.split()[0]
        if(method == "POST"):
            url = request.split("=")[-1]
        else:
            url = None
        resource = request.split()[1]
        return (method, resource, url)

    def new_num(self):
        global cont
        cont += 1
        return cont

    def process(self, parsedRequest):
        print(parsedRequest)
        if(parsedRequest[0] == "GET"):
            html_answer = """
                <html>
                    <body>
                        <h1>Acortador de URLs</h1>
                        <form action="" method="POST">
                            <label for="url">URL a acrotar:</label><br>
                            <input type="text" name="url" value=""/><br>
                            <input type="submit" value="Send url">
                        </form>
                    </body>
                </html>"""
        elif(parsedRequest[0] == "POST"):
            url = parsedRequest[2]
            if url in urls:
                print("ya dentro")
            else:
                urls[url] = self.new_num()

            html_answer = '<html><body><h1>URL: ' + str(urls) + '</h1></body></html>'
        else:
            html_answer = "Error"
        return ("200 OK", html_answer)

if __name__ == "__main__":
    testWebApp = webShort("localhost", 1234)
