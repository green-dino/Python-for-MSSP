import http.server
import socketserver

# Define the port number
PORT = 80

# Define the request handler
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Override the log message to avoid printing to stdout
    def log_message(self, format, *args):
        pass

# Create a socket server
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("Server started on port", PORT)
    # Start the server and keep it running until interrupted
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server is shutting down...")
        httpd.shutdown()
