"""Global configuration & constants"""
import pathlib

VERSION = "1.0.0"
AUTHOR = "NetHunter Team"
DEFAULT_THREADS = 100
DEFAULT_TIMEOUT = 3
DEFAULT_PORTS = "1-1000"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

WORDLISTS_DIR = pathlib.Path(__file__).parent / "wordlists"

COMMON_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995,
    1723, 3306, 3389, 5900, 8080, 8443, 8888, 9090, 27017
]

SERVICES = {
    21: "ftp", 22: "ssh", 23: "telnet", 25: "smtp", 53: "dns",
    80: "http", 110: "pop3", 111: "rpcbind", 135: "msrpc", 139: "netbios",
    143: "imap", 443: "https", 445: "smb", 993: "imaps", 995: "pop3s",
    1723: "pptp", 3306: "mysql", 3389: "rdp", 5432: "postgresql",
    5900: "vnc", 6379: "redis", 8080: "http-alt", 8443: "https-alt",
    8888: "http-alt", 9090: "http-alt", 27017: "mongodb",
}
