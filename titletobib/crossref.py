from __future__ import print_function
import requests
from builtins import input
import difflib

bare_url = "http://api.crossref.org/"


def find_cross_info(params):
    url = bare_url+"works"
    requested = requests.get(url, params=params)
    return requested


def get_bib_from_doi(doi):
    url = "{}works/{}/transform/application/x-bibtex"
    url = url.format(bare_url, doi)
    r = requests.get(url)
    found = False if r.status_code != 200 else True
    bib = r.content
    return found, bib


def ask_which_is(title, items):
    found = False
    result = {}
    question = "\t It is >>'{}' article?y(yes)|n(no)|q(quit)"
    for item in items:
        w = input(question.format(
            item["title"][0].encode("ascii", "ignore"), title))
        # pdb.set_trace()
        if w == "y":
            found = True
            result = item
            break
        if w == "q":
            break
    return found, result


def sort_items_by_title(items, title):
    return sorted(
        items,
        key=lambda x: difflib.SequenceMatcher(
            None,
            x["title"][0],
            title
        ).ratio(),
        reverse=True
    )


def get_from_title(title, get_first=False):
    found = False
    params = {"query.title": title, "rows": 10}
    r = find_cross_info(params)
    items = r.json()["message"]["items"]
    if r.status_code == 200 and len(items) > 0:
        items = sort_items_by_title(items, title)
        if get_first:
            found = True
            item = items[0]
        else:
            print("\nOriginal title: "+title+"\n")
            found, item = ask_which_is(title, items)
    return found, item


def get_bib_from_title(title, get_first=False):
    found = False
    bib = ""
    found, item = get_from_title(title, get_first)
    if found:
        doi = item["DOI"]
        found, bib = get_bib_from_doi(doi)
    else:
        found = False

    return found, bib
