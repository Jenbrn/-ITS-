from http.server import HTTPServer, BaseHTTPRequestHandler
import json, os, sys, logging

# Configure logging to ensure all output goes to stdout/stderr
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    stream = sys.stdout,

)
logger = logging.getLogger(__name__)


class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = json.dumps({"status": "ok"})
            logger.info(f"GET /health from {self.client_address[0]}")
        
        elif self.path == "/version":
            version = os.environ.get("APP_VERSION", "1.0")
            body = json.dumps({"version": os.environ.get("APP_VERSION", "Fatti i fatti tuoi")})
            logger.info(f"GET /version - {version}")
        else:
            body = "Hello from container!"
            logger.info(f"GET {self.path} from {self.client_address[0]}")

        self.send_response(200)
        self.end_headers(
            "Content-Type",
            (
                "application/json"
                if self.path.startswith("/") and self.path != "/"
                else "text/plain"
            ),
        )
        self.end_headers()
        self.wfile.write(body.encode())
    
    def log_message(self, format, *args):
        #print(f"{self.address_string()} {format % args}")  # ensure logs go to stdout
        logger.info(f"HTTP {self.address_string()}: {format % args}")

try:
    logger.info(f"APP_VERSION={os.environ.get('APP_VERSION', '1.0')}")
    logger.info("Server listening on port 9090")
    HTTPServer(("", 9090), H).serve_forever()
except Exception as e:
    logger.error(
        f"Server error: {e}", exc_info=True
    )  # exc_info=True includes traceback to stderr
    sys.exit(1)

        
# print("Server listening on port 9090")  # startup log (you'll see this in docker logs)
# HTTPServer(("", 9090), H).serve_forever()

