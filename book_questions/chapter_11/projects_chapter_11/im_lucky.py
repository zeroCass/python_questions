import bs4, webbrowser, requests
import sys, os

# 'https://www.youtube.com/results?search_query=chapeus+de_palha'
headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    assert len(sys.argv) > 1, 'Error! The command cannot be empty'
    google_search = 'https://www.google.com/search?q='
    s = requests.Session()
    search = '+'.join(sys.argv[1:])
    query = {'q': ' '.join(sys.argv[1:])}
    print(search)

    # faz download da pagina web
    res = s.get('https://www.google.com/search?q=' + '+'.join(sys.argv[1:]))
    # gera erro caso de algo errado
    res.raise_for_status()
    links = bs4.BeautifulSoup(res.text).select('a')
    for item in links:
        print(item)

    # with open(os.path.join(os.getcwd(), 'html.txt'),'w') as file_text:
    #     file_text.write(str(bs4.BeautifulSoup(res.text, 'html.parser')))


if __name__ == '__main__':
    main()