import requests
import time
import os
import sys

# ANSI Color Codes
class Color:
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def typing_print(text, color=Color.WHITE, speed=0.03):
    colored_text = color + text + Color.RESET
    for char in colored_text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_credit():
    credit = [
        "",
        "──────────────────────────────────────────────────",
        f"{Color.CYAN}Created by: @a_lonely_ooo{Color.RESET}",
        f"{Color.MAGENTA}Github: github.com/a-lonely-ooo{Color.RESET}",
        "──────────────────────────────────────────────────",
        ""
    ]
    for line in credit:
        print(line)
        time.sleep(0.1)

# 1. LOOKUP animation (will be cleared)
def display_lookup():
    for i in range(3):
        clear()
        print("LOOKUP...")
        time.sleep(0.5)
        clear()
        print("LOOKUP")
        time.sleep(0.5)
    clear()

# 2. DOSTS with logo animation (will be cleared)
def display_dosts():
    for i in range(3):
        clear()
        print("DOSTS...")
        time.sleep(0.5)
        clear()
        print("DOSTS")
        time.sleep(0.5)
    show_logo_animation()
    clear()

def show_logo_animation():
    frames = [
        r"""
          _____
         /     \
        | O   O |
         \  ▽  /
          ─────
        LOADING...
        """,
        r"""
          _____
         /     \
        | ◐   ◐ |
         \  ▽  /
          ─────
        LOADING...
        """,
        r"""
          _____
         /     \
        | ◓   ◓ |
         \  ▽  /
          ─────
        LOADING...
        """,
        r"""
          _____
         /     \
        | ◑   ◑ |
         \  ▽  /
          ─────
        LOADING...
        """,
        r"""
          _____
         /     \
        | ◒   ◒ |
         \  ▽  /
          ─────
        LOADING...
        """
    ]
    
    end_time = time.time() + 2
    while time.time() < end_time:
        for frame in frames:
            clear()
            print(Color.CYAN + frame + Color.RESET)
            time.sleep(0.1)

# 3. Fade-in ASCII art (only final frame remains)
def fade_in_ascii_art():
    ascii_art = [
        " ___________ _____ _____   _             _                ",
        "|_   _|  ___/  ___/  __ \\ | |           | |               ",
        "  | | | |_  \\ `--.| /  \\/ | | ___   ___ | | ___   _ _ __  ",
        "  | | |  _|  `--. \\ |     | |/ _ \\ / _ \\| |/ / | | | '_ \\ ",
        " _| |_| |   /\\__/ / \\__/\\ | | (_) | (_) |   <| |_| | |_) |",
        " \\___/\\_|   \\____/ \\____/ |_|\\___/ \\___/|_|\\_\\/__,_| .__/ ",
        "                                                   | |    ",
        "                                                   |_|    ",
        "                          Github: @a-lonely-ooo",
        "                          insta: @a_lonely_ooo",
        "                          telegram: @a_lonely_ooo",
        "                          twitter: @a_lonely_ooo",
        "                          discord: @a_lonely_ooo",
        "Yah I am addicted to this username😅"
    ]
    
    steps = 15
    delay = 0.03
    
    # Show fade-in animation
    for i in range(steps + 1):
        clear()
        ratio = i / steps
        for line in ascii_art:
            visible_chars = int(len(line) * ratio)
            faded_line = Color.MAGENTA + line[:visible_chars] + Color.RESET
            print(faded_line)
        time.sleep(delay)
    
    # Keep only the final frame
    clear()
    for line in ascii_art:
        print(Color.MAGENTA + line + Color.RESET)
    
    # Show credit line after fade-in
    display_credit()

# IFSC API functions
IFSC_API_URL = "https://ifsc.razorpay.com/{ifsc_code}"

def get_ifsc_info(ifsc_code):
    try:
        response = requests.get(IFSC_API_URL.format(ifsc_code=ifsc_code))
        if response.status_code == 200:
            data = response.json()
            bank_info = {
                "IFSC Code": data.get("IFSC", "Not Available"),
                "Bank": data.get("BANK", "Not Available"),
                "Branch": data.get("BRANCH", "Not Available"),
                "Address": data.get("ADDRESS", "Not Available"),
                "City": data.get("CITY", "Not Available"),
                "District": data.get("DISTRICT", "Not Available"),
                "State": data.get("STATE", "Not Available"),
                "Contact": data.get("CONTACT", "Not Available"),
                "UPI Available": data.get("UPI", "Not Available"),
                "IMPS Available": data.get("IMPS", "Not Available"),
                "RTGS Available": data.get("RTGS", "Not Available"),
                "NEFT Available": data.get("NEFT", "Not Available"),
                "MICR Code": data.get("MICR", "Not Available")
            }
            return bank_info
        else:
            return f"{Color.RED}⚠️ Failed to fetch details. Please check the IFSC code.{Color.RESET}"
    except Exception as e:
        return f"{Color.RED}❌ Error: {str(e)}{Color.RESET}"

def ifsc_info():
    # Show animations in exact order
    display_lookup()     # 1. LOOKUP (cleared after)
    display_dosts()      # 2. DOSTS with logo (cleared after)
    fade_in_ascii_art()  # 3. Fade-in ASCII (only final frame remains)
    
    # Then start IFSC lookup
    while True:
        typing_print(Color.YELLOW + Color.BOLD + "Enter IFSC code (or 'q' to quit): " + Color.RESET, speed=0)
        ifsc_code = input().strip().upper()
        
        if not ifsc_code:
            print(f"{Color.RED}⚠️ Please enter a valid IFSC code.{Color.RESET}")
            continue
        elif ifsc_code.lower() == 'q':
            clear()
            print(Color.MAGENTA + " ___________ _____ _____   _             _                " + Color.RESET)
            print(Color.MAGENTA + "|_   _|  ___/  ___/  __ \\ | |           | |               " + Color.RESET)
            print(Color.MAGENTA + "  | | | |_  \\ `--.| /  \\/ | | ___   ___ | | ___   _ _ __  " + Color.RESET)
            print(Color.MAGENTA + "  | | |  _|  `--. \\ |     | |/ _ \\ / _ \\| |/ / | | | '_ \\ " + Color.RESET)
            print(Color.MAGENTA + " _| |_| |   /\\__/ / \\__/\\ | | (_) | (_) |   <| |_| | |_) |" + Color.RESET)
            print(Color.MAGENTA + " \\___/\\_|   \\____/ \\____/ |_|\\___/ \\___/|_|\\_\\/__,_| .__/ " + Color.RESET)
            print(Color.MAGENTA + "                                                   | |    " + Color.RESET)
            print(Color.MAGENTA + "                                                   |_|    " + Color.RESET)
            display_credit()
            typing_print(f"{Color.GREEN}👋 Goodbye!{Color.RESET}")
            break
            
        typing_print(f"{Color.CYAN}🔍 Fetching details for {ifsc_code}...{Color.RESET}")
        bank_info = get_ifsc_info(ifsc_code)
        
        if isinstance(bank_info, dict):
            message = "\n".join([f"{Color.GREEN}{key}: {Color.BLUE}{value}{Color.RESET}" 
                               for key, value in bank_info.items()])
            print(f"\n{Color.BOLD}📋 IFSC Details:{Color.RESET}\n\n{message}\n")
        else:
            print(f"\n{bank_info}\n")

if __name__ == "__main__":
    try:
        ifsc_info()
    except KeyboardInterrupt:
        clear()
        print(Color.MAGENTA + " ___________ _____ _____   _             _                " + Color.RESET)
        print(Color.MAGENTA + "|_   _|  ___/  ___/  __ \\ | |           | |               " + Color.RESET)
        print(Color.MAGENTA + "  | | | |_  \\ `--.| /  \\/ | | ___   ___ | | ___   _ _ __  " + Color.RESET)
        print(Color.MAGENTA + "  | | |  _|  `--. \\ |     | |/ _ \\ / _ \\| |/ / | | | '_ \\ " + Color.RESET)
        print(Color.MAGENTA + " _| |_| |   /\\__/ / \\__/\\ | | (_) | (_) |   <| |_| | |_) |" + Color.RESET)
        print(Color.MAGENTA + " \\___/\\_|   \\____/ \\____/ |_|\\___/ \\___/|_|\\_\\/__,_| .__/ " + Color.RESET)
        print(Color.MAGENTA + "                                                   | |    " + Color.RESET)
        print(Color.MAGENTA + "                                                   |_|    " + Color.RESET)
        display_credit()
        typing_print(f"\n{Color.RED}🚫 Program interrupted. Exiting...{Color.RESET}")
        sys.exit(0)
