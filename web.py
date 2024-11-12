from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<html lang="en">
    <body>
<heading>
<h1><b>maniyarasan</b></h1>
<h2>CONFIGURATION;24900020</h2>
 <ol>
            <li>Device name	LAPTOP-TD1STGLV</li>
             <li>Processor      AMD Ryzen 5 5600H with Radeon Graphics         3.30 GHz</li>
<li>Installed RAM	16.0 GB (15.3 GB usable)</li>
<li>Device ID	A065CAEE-3011-4CD9-9075-76073AE60796</li>
<li>Product ID	00342-42591-34244-AAOEM</li>
<li>System type	64-bit operating system, x64-based processor</li>
<li>Pen and touch	No pen or touch input is available for this display</li>

        </ol>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()