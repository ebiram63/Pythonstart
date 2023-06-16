cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_form_server(url)
        cache[url] = data
        return data