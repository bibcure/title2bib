from __future__ import print_function
import requests
from builtins import input
import difflib
from doitobib.crossref import get_bib_from_doi
bare_url = "http://api.crossref.org/"


def find_cross_info(params):
    url = bare_url+"works"
    requested = requests.get(url, params=params)
    return requested


def ask_which_is(title, items):
    found = False
    result = {}
    question = "\t It is >>'{}' article?y(yes)|n(no)|q(quit)"
    for item in items:
        w = input(question.format(
            item["title"][0].encode("ascii", "ignore"), title))
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


def get_bib_from_title(title, get_first=False, abbrev_journal=False):
    found = False
    bib = ""
    found, item = get_from_title(title, get_first)
    if found:
        if "DOI" in item:
            doi = item["DOI"]##aqui pode acontecer de realizar a chamada para
            found, bib = get_bib_from_doi(doi)
            if "short-container-title" in item:
                abbreviated_journal = item["short-container-title"][0]##aqui pode acontecer de realizar a chamada para

        #pegar journal contraido e contrair autores
        # depois fazer um replace no bib com  o nome do journal e o
        #contraido, ou usar o bibtexparser(ultima melhor)

    return found, bib
