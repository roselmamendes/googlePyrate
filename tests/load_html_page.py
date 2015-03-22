searches = {
    'python crawler': 'tests/searches/python_crawler_search.html'
}


def load_html(search):
    html_file = open(searches.get(search), 'r')
    html_content = html_file.read()
    html_file.close()
    return html_content
