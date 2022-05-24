from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json


data_base = []



class MyHTTPServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info(f'GET request,\nPath: {self.path}\nHeaders: {self.headers}\n')
        self._set_response()

        data = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(data)

        if self.path == '/user':
            logging.info('GET user function processing...\n')
            user = self._getusers(data['id'])
            self.wfile.write(f'GET request data: {user}'.encode('utf-8'))

        self.wfile.write('GET request for {}'.format(self.path).encode('utf-8'))
    
    def do_POST(self):
        #content_lenght = int(self.headers.get('content_length', 0))
        #post_data = self.rfile.read(content_lenght)
        data = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(data)

        if self.path == '/adduser':
            logging.info('POST user processing...\n')
            self._adduser(data)

        logging.info(f'POST request,\nPath: {self.path}\nHeaders: {self.headers}')
        logging.info('Body: {}\n'.format(data))
        self._set_response()
        self.wfile.write('POST request for {}'.format(self.path).encode('utf-8'))
    

    def _adduser(self, data):
        data['id'] = len(data_base) + 1
        data_base.append(data)
    
    def _getusers(self, id):
        for user in data_base:
            if user['id'] == id:
                return user
        return 'Not found'



def run(server_class=HTTPServer, handler_class=MyHTTPServer, port=12000):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    server_adress = ('', port)
    httpd = server_class(server_adress, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    run()