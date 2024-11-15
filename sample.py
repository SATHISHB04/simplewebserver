from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <body>
        <h1><b>DEVICE SPECIFICATION - SATHISH 24900077</b></h1>
        <b>Device name</b>  DESKTOP-TQPACUI<br>
        <b>Processor</b>  11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz   2.42 GHz<br>
        <b>Installed RAM</b>  8.00 GB (7.75 GB usable)<br>
        <b>Device ID</b>  72BFFA5C-A2CF-4550-A0C0-63B6EA6F8A11<br>
        <b>Product ID</b>  00331-10000-00001-AA223<br>
        <b>System type</b>  64-bit operating system, x64-based processor<br>
        <b>Pen and touch</b>  No pen or touch input is available for this display<br>
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
