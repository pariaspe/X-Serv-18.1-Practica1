#!/usr/bin/python3

"""
Web recortadora de urls

 p.ariaspe @ alumnos.urjc.es
 SAT (Universidad Rey Juan Carlos)
"""

import webapp

class webShort(webapp.webApp):
    def parse(self, request):
        method = request.split()[0]
        if(method == "POST"):
            url = request.split("=")[-1]
        else:
            url = None
        resource = request.split()[1]
        return (method, resource, url)

    def process(self, parsedRequest):
        print(parsedRequest)
        if(parsedRequest[0] == "GET"):
            html_answer = """
                <html>
                    <body>
                        <h1>Formulario:</h1>
                        <form action="" method="POST">
                            <label for="url">Name:</label><br>
                            <input type="text" name="url" value="pepe"/><br>
                            <input type="submit" value="Send url">
                        </form>
                    </body>
                </html>"""
        elif(parsedRequest[0] == "POST"):
            html_answer = '<html><body><h1>URL: ' + parsedRequest[2] + '</h1></body></html>'
        else:
            html_answer = "Error"
        return ("200 OK", html_answer)

if __name__ == "__main__":
    testWebApp = webShort("localhost", 1234)
