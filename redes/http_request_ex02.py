import http.client


def HTTPclient(host, port):
    conn = http.client.HTTPConnection(host, port)

    contents_types = {'text/html': 'Brownsing:',
                     'audio/mpeg': 'Playing audio:',
                     'video/x-msvideo': 'Playing media:',
                     'application/json': 'Processing JSON:'}

    L = int(input())
    for i in range(0, L):
        content = input()
        conn.request('GET', content)
        res = conn.getresponse()
        
        if res.status > 400:
            print('Content not found')
            continue
            
        headers = res.getheaders()
        content_type = ''
        for header in headers:
            if header[0] == 'Content-type':
                content_type = header[1]

        if content_type in contents_types.keys(): 
            print(f'{contents_types[content_type]} {content}')
        else:
            print(f'Unknown file/media: {content_type}-{content}')

    conn.close()

HTTPclient('localhost', 12000)