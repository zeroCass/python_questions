import bs4, webbrowser, requests
import sys, os



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #assert len(sys.argv) > 1, 'Error! The command cannot be empty'
    
    res = requests.get('https://www.google.com/search?q='+  ''.join(sys.argv[1:]), headers=headers)
    #res = requests.get('https://www.youtube.com/results?search_query=' + '+'.join(sys.argv[1:]))
    res.raise_for_status()


if __name__ == '__main__':
    main()