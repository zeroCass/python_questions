import http.client


def HTTPclient(host, port):
    conn = http.client.HTTPConnection(host, port)

    L = int(input())
    for i in range(0, L):
        content = input()
        conn.request('GET', '/' + content)
        res = conn.getresponse()
        print(res.read().decode()) 
    conn.close()

HTTPclient('localhost', 12000)