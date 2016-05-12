def app(environ, start_response):
    data = ''
    query = environ['QUERY_STRING'].split('&')
    for item in query:
        data += item + "\n"
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return [data]