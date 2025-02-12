import requests
import random
import pyfiglet
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

def show_banner():
    """Display the PassGen banner using ASCII art."""
    banner = pyfiglet.figlet_format("PassGen")
    print(f"{Fore.GREEN}{Style.BRIGHT}{banner}")

def fetch_joke():
    """Fetch a random joke from an API and return the setup text."""
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/general/random", timeout=5)
        joke = response.json()[0]  # Extract first joke
        return joke['setup']
    except:
        return "Why do programmers prefer dark mode"  # Default joke if API fails

def generate_password():
    """Generate a password using a joke's setup with random separators."""
    joke_text = fetch_joke()
    
    # Randomly choose a separator from the list for each space
    separators = ['#', '@', '_', '-']
    password = ''.join(random.choice(separators) if char == ' ' else char for char in joke_text)
    
    # Append a random special character for extra security
    password += random.choice(['?', '!', '$', '&'])
    
    return password

# Example Usage
if __name__ == "__main__":
    show_banner()  # Display the banner

    password = generate_password()

    # Display the password with colors
    print(f"\n{Fore.CYAN}{Style.BRIGHT}🔒 Generated Password: {Fore.YELLOW}{password}\n")

