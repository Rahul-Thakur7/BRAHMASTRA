#!/usr/bin/env python3
import requests
import argparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
import atexit

init(autoreset=True)

BANNER = r"""
   _____            __                  __________               .__                             __                 
  /  _  \   _______/  |_____________    \______   \____________  |  |__   _____ _____    _______/  |_____________   
 /  /_\  \ /  ___/\   __\_  __ \__  \    |    |  _/\_  __ \__  \ |  |  \ /     \\__  \  /  ___/\   __\_  __ \__  \  
/    |    \\___ \  |  |  |  | \// __ \_  |    |   \ |  | \// __ \|   Y  \  Y Y  \/ __ \_\___ \  |  |  |  | \// __ \_
\____|__  /____  > |__|  |__|  (____  /  |______  / |__|  (____  /___|  /__|_|  (____  /____  > |__|  |__|  (____  /
        \/     \/                   \/          \/             \/     \/      \/     \/     \/                   \/  
               🔥 BRAHMASTRA - Digital Annihilation Protocol 🔥
"""

PLATFORMS = {
    "GitHub": "https://github.com/{username}",
    "GitLab": "https://gitlab.com/{username}",
    "Bitbucket": "https://bitbucket.org/{username}",
    "CodePen": "https://codepen.io/{username}",
    "Dev.to": "https://dev.to/{username}",
    "Repl.it": "https://repl.it/@{username}",
    "Stack Overflow": "https://stackoverflow.com/users/{username}",
    "Docker Hub": "https://hub.docker.com/u/{username}",
    "Kaggle": "https://www.kaggle.com/{username}",
    "LeetCode": "https://leetcode.com/{username}",
    "HackerRank": "https://www.hackerrank.com/{username}",
    "HackerEarth": "https://www.hackerearth.com/@{username}",
    "CodeChef": "https://www.codechef.com/users/{username}",
    "TopCoder": "https://www.topcoder.com/members/{username}",
    "Codeforces": "https://codeforces.com/profile/{username}",
    "GeeksforGeeks": "https://auth.geeksforgeeks.org/user/{username}",
    "Coderbyte": "https://coderbyte.com/profile/{username}",
    "Codewars": "https://www.codewars.com/users/{username}",
    "Behance": "https://www.behance.net/{username}",
    "Dribbble": "https://dribbble.com/{username}",
    "ArtStation": "https://www.artstation.com/{username}",
    "DeviantArt": "https://{username}.deviantart.com",
    "Flickr": "https://www.flickr.com/people/{username}",
    "500px": "https://500px.com/{username}",
    "Adobe Portfolio": "https://{username}.myportfolio.com",
    "YouTube": "https://www.youtube.com/user/{username}",
    "Twitch": "https://www.twitch.tv/{username}",
    "Vimeo": "https://vimeo.com/{username}",
    "DailyMotion": "https://www.dailymotion.com/{username}",
    "TikTok": "https://www.tiktok.com/@{username}",
    "Facebook": "https://www.facebook.com/{username}",
    "Twitter": "https://twitter.com/{username}",
    "Instagram": "https://www.instagram.com/{username}",
    "LinkedIn": "https://www.linkedin.com/in/{username}",
    "Reddit": "https://www.reddit.com/user/{username}",
    "Pinterest": "https://www.pinterest.com/{username}",
    "Tumblr": "https://{username}.tumblr.com",
    "VK": "https://vk.com/{username}",
    "Weibo": "https://www.weibo.com/{username}",
    "Quora": "https://www.quora.com/profile/{username}",
    "Medium": "https://medium.com/@{username}",
    "Steam": "https://steamcommunity.com/id/{username}",
    "XDA Developers": "https://forum.xda-developers.com/member.php?username={username}",
    "Freelancer": "https://www.freelancer.com/u/{username}",
    "Fiverr": "https://www.fiverr.com/{username}",
    "Upwork": "https://www.upwork.com/freelancers/~{username}",
    "Gravatar": "https://en.gravatar.com/{username}",
    "Blogger": "https://{username}.blogspot.com",
    "WordPress": "https://{username}.wordpress.com",
    "Slideshare": "https://www.slideshare.net/{username}",
    "Wikipedia": "https://en.wikipedia.org/wiki/User:{username}",
}

HEADERS = {"User-Agent": "Mozilla/5.0"}
TIMEOUT = 7
THREADS = 50

def check_platform(name, url, username):
    full_url = url.format(username=username)
    try:
        response = requests.get(full_url, headers=HEADERS, timeout=TIMEOUT)
        if response.status_code == 200:
            return f"{Fore.GREEN}[+] {name}: {full_url}"
    except requests.RequestException:
        pass
    return None

def run_beeast(username):
    print(f"\n[*] Checking username '{Fore.CYAN + username + Style.RESET_ALL}' on:\n")
    results = []

    try:
        with ThreadPoolExecutor(max_workers=THREADS) as executor:
            future_to_platform = {
                executor.submit(check_platform, name, url, username): name
                for name, url in PLATFORMS.items()
            }
            for future in as_completed(future_to_platform):
                result = future.result()
                if result:
                    results.append(result)
                    print(result)

        print(f"\n{Fore.YELLOW}[✓] Search completed with {len(results)} result(s)")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Scan interrupted by user. Exiting gracefully...")
        exit_handler()
        exit()

def exit_handler():
    print(f"\n[+] Exiting... Thank you for using {Fore.RED}🔥 BRAHMASTRA 🔥{Style.RESET_ALL}\n")

atexit.register(exit_handler)

def main():
    parser = argparse.ArgumentParser(description="Beeast 🐝 - Advanced Username Hunter")
    parser.add_argument("username", help="Username to search for")
    args = parser.parse_args()

    print(Fore.MAGENTA + BANNER)
    start = time.time()
    run_beeast(args.username)
    print(f"{Fore.CYAN}[*] Completed in {round(time.time() - start, 2)} seconds\n")

if __name__ == "__main__":
    main()
