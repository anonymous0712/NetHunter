"""ASCII art banner"""
from nethunter import __version__
from nethunter.utils.colors import PURPLE, CYAN, YELLOW, GREEN, RESET, BOLD

BANNER = f"""
{PURPLE}{BOLD}
 ███╗   ██╗███████╗████████╗██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
 ████╗  ██║██╔════╝╚══██╔══╝██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
 ██╔██╗ ██║█████╗     ██║   ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
 ██║╚██╗██║██╔══╝     ██║   ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
 ██║ ╚████║███████╗   ██║   ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
 ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{RESET}
{CYAN}          Ultimate CLI Pentesting Toolkit - Shodan Alternative (No API Keys){RESET}
{YELLOW}                    Version: {__version__} | Platform: Kali Linux{RESET}
{GREEN}               For authorized penetration testing and security research only{RESET}
"""

def print_banner() -> None:
    """Print the NetHunter ASCII art banner."""
    print(BANNER)
