from __future__ import print_function
import requests

bare_url = "http://api.crossref.org/"
#http://api.crossref.org/works/10.1038/NPHYS1270/transform/application/x-bibtex
def find_cross_info(bib, fields=["title"]):
    params = {}
    for field in fields:
        params[field] = bib[field]
    url = bare_url+"works"
    requested = requests.get(url, params=params)
    return requested

def get_bib_from_doi(doi):
    url = "{}works/{}/transform/application/x-bibtex"
    requested = requests.get(url)
    return requested

