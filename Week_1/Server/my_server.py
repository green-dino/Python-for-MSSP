import http.server
import socketserver
import argparse
import os
import sys

# Default port number
DEFAULT_PORT = 80
# Default directory to serve static files from
DEFAULT_STATIC_DIR = "static"

# Define the request handler
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Override the log message to avoid printing to stdout
    def log_message(self, format, *args):
        pass

def run_server(port, static_dir):
    # Change directory to the static content directory
    os.chdir(static_dir)
    
    # Create a socket server
    with socketserver.TCPServer(("", port), MyHttpRequestHandler) as httpd:
        print(f"Server started on port {port}, serving static content from {static_dir}")
        # Start the server and keep it running until interrupted
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Server is shutting down...")
            httpd.shutdown()

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Simple HTTP Server")
    parser.add_argument("-p", "--port", type=int, default=DEFAULT_PORT,
                        help=f"Port number to run the server on (default: {DEFAULT_PORT})")
    parser.add_argument("-d", "--static-dir", default=DEFAULT_STATIC_DIR,
                        help=f"Directory to serve static files from (default: {DEFAULT_STATIC_DIR})")
    args = parser.parse_args()

    # Validate the static directory
    if not os.path.isdir(args.static_dir):
        print(f"Error: Static directory '{args.static_dir}' does not exist.")
        sys.exit(1)

    # Run the server
    run_server(args.port, args.static_dir)
